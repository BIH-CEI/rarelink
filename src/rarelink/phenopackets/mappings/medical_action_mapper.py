# src/rarelink/phenopackets/mappings/medical_action_mapper.py
from typing import Any, Dict, List, Optional
import logging

from phenopackets import (
    Age,
    MedicalAction,
    OntologyClass,
    Procedure,
    Quantity,
    TimeElement,
    Treatment,
)

from rarelink.phenopackets.mappings.base_mapper import BaseMapper

logger = logging.getLogger(__name__)


class MedicalActionMapper(BaseMapper[MedicalAction]):
    """
    Mapper for MedicalAction entities in the Phenopacket schema.

    Always returns a list of MedicalAction objects for consistency.
    Supports both procedure and treatment data models.
    """

    def map(self, data: Dict[str, Any], **kwargs) -> List[MedicalAction]:
        # Force multi-entity mapping
        self.processor.mapping_config["multi_entity"] = True
        return super().map(data, **kwargs)

    def _map_single_entity(
        self,
        data: Dict[str, Any],
        instruments: List[str],
        **kwargs,
    ) -> Optional[MedicalAction]:
        logger.warning(
            "MedicalActionMapper._map_single_entity called, but this mapper "
            "returns multiple entities"
        )
        return None

    def _map_multi_entity(
        self,
        data: Dict[str, Any],
        instruments: List[str],
        **kwargs,
    ) -> List[MedicalAction]:
        dob = kwargs.get("dob")
        mapping_config = self.processor.mapping_config

        is_treatment = (
            "agent_field_1" in mapping_config
            or "cumulative_dose" in mapping_config
        )

        if is_treatment:
            logger.debug("Mapping treatment-based medical actions")
            return self._map_treatments(data, dob)

        logger.debug("Mapping procedure-based medical actions")
        return self._map_procedures(data, dob)

    def _map_procedures(
        self,
        data: Dict[str, Any],
        dob: Optional[str],
    ) -> List[MedicalAction]:
        actions: List[MedicalAction] = []
        instrument = self.processor.mapping_config.get("redcap_repeat_instrument")

        repeated = data.get("repeated_elements", [])
        if not repeated and instrument and instrument in data:
            repeated = [data]

        elements = [
            el for el in repeated
            if el.get("redcap_repeat_instrument") == instrument
        ]
        if not elements and instrument and instrument in data:
            elements = [data]

        proc_fields = {
            k: v
            for k, v in self.processor.mapping_config.items()
            if (
                k.startswith("procedure_field_")
                and not k.endswith("_date")
                and isinstance(v, str)
            )
        }
        logger.debug("Found procedure fields: %s", proc_fields)

        for element in elements:
            for proc_key, field_path in proc_fields.items():
                code_val = self._get_field_value(element, field_path)
                if not code_val:
                    logger.debug(
                        "No procedure details found for %s (field: %s)",
                        proc_key,
                        field_path,
                    )
                    continue

                performed_field = self.processor.mapping_config.get("performed")
                if performed_field is not None:
                    performed_val = self._get_field_value(
                        element,
                        performed_field,
                    )
                    if performed_val is None:
                        logger.debug(
                            "Procedure %s not performed; skipping",
                            proc_key,
                        )
                        continue

                proc = self._create_procedure(
                    procedure_key=proc_key,
                    procedure_code=str(code_val),
                    element=element,
                    dob=dob,
                )
                if not proc:
                    continue

                actions.append(MedicalAction(procedure=proc))
                logger.debug(
                    "Created medical action with procedure for field %s",
                    proc_key,
                )

        logger.debug("Generated %d medical actions", len(actions))
        return actions

    def _create_procedure(
        self,
        procedure_key: str,
        procedure_code: str,
        element: Dict[str, Any],
        dob: Optional[str],
    ) -> Optional[Procedure]:
        if not procedure_code:
            return None

        processed_code = self.processor.process_code(procedure_code)

        procedure_label = self.processor.fetch_label(procedure_code)
        if not procedure_label and processed_code != procedure_code:
            procedure_label = self.processor.fetch_label(processed_code)

        code = OntologyClass(
            id=processed_code,
            label=procedure_label or "Unknown Procedure",
        )

        performed = None
        date_field = self.processor.mapping_config.get(f"{procedure_key}_date")
        if date_field and dob:
            date_val = self._get_field_value(element, date_field)
            if date_val:
                try:
                    iso_age = self.processor.convert_date_to_iso_age(
                        str(date_val),
                        str(dob),
                    )
                    if iso_age:
                        performed = TimeElement(
                            age=Age(iso8601duration=iso_age),
                        )
                except Exception as e:
                    logger.warning(
                        "Could not calculate age at procedure: %s",
                        e,
                    )

        return Procedure(code=code, performed=performed)

    def _map_treatments(
        self,
        data: Dict[str, Any],
        dob: Optional[str],
    ) -> List[MedicalAction]:
        medical_actions: List[MedicalAction] = []
        mapping_config = self.processor.mapping_config
        instrument_name = mapping_config.get("redcap_repeat_instrument")
        if not instrument_name:
            logger.debug("No instrument name found in mapping configuration")
            return []

        repeated_elements = data.get("repeated_elements", [])
        if not repeated_elements:
            logger.debug("No repeated elements found in data")
            return []

        instrument_elements = [
            element for element in repeated_elements
            if element.get("redcap_repeat_instrument") == instrument_name
        ]
        logger.debug(
            "Found %d treatment elements for instrument %s",
            len(instrument_elements),
            instrument_name,
        )

        processed_instances = set()
        seen_agents = set()
        for element in instrument_elements:
            try:
                instance_id = element.get("redcap_repeat_instance")
                element_key = f"{instrument_name}:{instance_id}"
                if element_key in processed_instances:
                    logger.debug("Skipping duplicate instance: %s", element_key)
                    continue
                processed_instances.add(element_key)

                instrument_data = element.get(instrument_name)
                if not instrument_data:
                    logger.debug(
                        "No instrument data found for element %s",
                        element_key,
                    )
                    continue

                agent_field_1 = mapping_config.get("agent_field_1")
                if not agent_field_1:
                    continue
                agent_field_name = (
                    agent_field_1.split(".")[-1]
                    if "." in agent_field_1
                    else agent_field_1
                )
                agent_id = instrument_data.get(agent_field_name)
                if agent_id in seen_agents:
                    logger.debug("Skipping duplicate agent: %s", agent_id)
                    continue
                seen_agents.add(agent_id)

                treatment = self._create_treatment(
                    instrument_data,
                    dob,
                    instrument_name,
                    element,
                )
                if not treatment:
                    continue

                medical_action = MedicalAction(treatment=treatment)
                adverse_events = self._extract_adverse_events(instrument_data)
                if adverse_events:
                    medical_action.adverse_events.extend(adverse_events)

                responses = self._extract_treatment_response(instrument_data)
                if responses:
                    if isinstance(responses, list) and responses:
                        medical_action.response_to_treatment.CopyFrom(
                            responses[0]
                        )
                    elif hasattr(responses, "id") and hasattr(responses, "label"):
                        medical_action.response_to_treatment.CopyFrom(responses)

                target_field = mapping_config.get("treatment_target_field")
                if target_field:
                    field_name = (
                        target_field.split(".")[-1]
                        if "." in target_field
                        else target_field
                    )
                    target_value = instrument_data.get(field_name)
                    if target_value:
                        target_id = self.processor.process_code(target_value)
                        target_label = (
                            self.processor.fetch_label(target_value)
                            or "Unknown Target"
                        )
                        target = OntologyClass(
                            id=target_id,
                            label=target_label,
                        )
                        medical_action.treatment_target.CopyFrom(target)

                intent_field = mapping_config.get("treatment_intent_field")
                if intent_field:
                    field_name = (
                        intent_field.split(".")[-1]
                        if "." in intent_field
                        else intent_field
                    )
                    intent_value = instrument_data.get(field_name)
                    if intent_value:
                        intent_id = self.processor.process_code(intent_value)
                        intent_label = (
                            self.processor.fetch_label(intent_value)
                            or "Unknown Intent"
                        )
                        intent = OntologyClass(
                            id=intent_id,
                            label=intent_label,
                        )
                        medical_action.treatment_intent.CopyFrom(intent)

                medical_actions.append(medical_action)
                logger.debug(
                    "Created medical action with treatment for instance %s",
                    instance_id,
                )
            except Exception as e:
                logger.error(
                    "Error processing treatment element for %s: %s",
                    instrument_name,
                    e,
                )

        logger.debug("Generated %d medical actions", len(medical_actions))
        return medical_actions

    def _create_treatment(
        self,
        instrument_data: Dict[str, Any],
        dob: Optional[str],
        instrument_name: str = "",
        full_element: Optional[Dict[str, Any]] = None,
    ) -> Optional[Treatment]:
        # (unchanged) ...
        mapping_config = self.processor.mapping_config
        agent_field_1 = mapping_config.get("agent_field_1")
        agent_field_2 = mapping_config.get("agent_field_2")
        agent_id = None
        if agent_field_1:
            agent_field_name = (
                agent_field_1.split(".")[-1]
                if "." in agent_field_1
                else agent_field_1
            )
            agent_id = instrument_data.get(agent_field_name)
        if agent_id == "other" and agent_field_2:
            other_field_name = (
                agent_field_2.split(".")[-1]
                if "." in agent_field_2
                else agent_field_2
            )
            agent_id = instrument_data.get(other_field_name)
        if not agent_id:
            logger.debug("No agent ID found for treatment")
            return None

        processed_id = self.processor.process_code(agent_id)
        agent_label = self.processor.fetch_label(agent_id)
        if not agent_label and processed_id != agent_id:
            agent_label = self.processor.fetch_label(processed_id)
        if not agent_label:
            label_dicts = mapping_config.get("label_dicts", {})
            agent_label_dict = label_dicts.get("agent_field_1")
            if agent_label_dict and agent_id in agent_label_dict:
                agent_label = agent_label_dict[agent_id]
        if not agent_label and hasattr(self.processor, "enum_classes"):
            for prefix, enum_class in self.processor.enum_classes.items():
                if agent_id.lower().startswith(prefix.lower()):
                    agent_label = self.processor.fetch_label_from_enum(
                        agent_id,
                        enum_class,
                    )
                    if agent_label:
                        break
        if not agent_label:
            agent_label = "Unknown Agent"
            logger.debug("Using default 'Unknown Agent' label")

        agent = OntologyClass(id=processed_id, label=agent_label)

        cumulative_dose = None
        dose_field = mapping_config.get("cumulative_dose")
        if dose_field:
            dose_field_name = (
                dose_field.split(".")[-1]
                if "." in dose_field
                else dose_field
            )
            dose_value = instrument_data.get(dose_field_name)
            if dose_value:
                try:
                    dose_value = float(dose_value)
                    cumulative_dose = Quantity(
                        value=dose_value,
                        unit=OntologyClass(
                            id="UO:0000307",
                            label="dose unit",
                        ),
                    )
                except (ValueError, TypeError):
                    logger.warning(
                        "Could not convert dose value '%s' to float",
                        dose_value,
                    )

        return Treatment(
            agent=agent,
            cumulative_dose=cumulative_dose,
        )

    def _extract_adverse_events(
        self,
        instrument_data: Dict[str, Any],
    ) -> List[OntologyClass]:
        # (unchanged) ...
        adverse_events: List[OntologyClass] = []
        mapping_config = self.processor.mapping_config
        adverse_event_field = mapping_config.get("adverse_event_field")
        adverse_event_other_field = mapping_config.get("adverse_event_other_field")
        if adverse_event_field:
            field_name = (
                adverse_event_field.split(".")[-1]
                if "." in adverse_event_field
                else adverse_event_field
            )
            ae_value = instrument_data.get(field_name)
            if ae_value and not str(ae_value).endswith("_exluded"):
                ae_id = self.processor.process_code(ae_value)
                ae_label = (
                    self.processor.fetch_label(ae_value)
                    or "Unknown Adverse Event"
                )
                adverse_events.append(OntologyClass(id=ae_id, label=ae_label))
        if adverse_event_other_field:
            field_name = (
                adverse_event_other_field.split(".")[-1]
                if "." in adverse_event_other_field
                else adverse_event_other_field
            )
            ae_other_value = instrument_data.get(field_name)
            if ae_other_value:
                ae_other_id = self.processor.process_code(ae_other_value)
                ae_other_label = (
                    self.processor.fetch_label(ae_other_value)
                    or "Unknown Adverse Event"
                )
                adverse_events.append(
                    OntologyClass(id=ae_other_id, label=ae_other_label)
                )
        return adverse_events

    def _extract_treatment_response(
        self,
        instrument_data: Dict[str, Any],
    ) -> List[OntologyClass]:
        # (unchanged) ...
        responses: List[OntologyClass] = []
        mapping_config = self.processor.mapping_config
        response_fields: Dict[int, str] = {}

        for key, value in mapping_config.items():
            if key.startswith("response_field_") and value:
                try:
                    response_fields[int(key.split("_")[-1])] = value
                except ValueError:
                    logger.warning(
                        "Invalid response field key format: %s",
                        key,
                    )

        for field_num in sorted(response_fields.keys()):
            response_field = response_fields[field_num]
            field_name = (
                response_field.split(".")[-1]
                if "." in response_field
                else response_field
            )
            response_value = instrument_data.get(field_name)
            if not response_value:
                continue

            processed_id = self.processor.process_code(response_value)
            response_label = self.processor.fetch_label(response_value)
            if not response_label and processed_id != response_value:
                response_label = self.processor.fetch_label(processed_id)

            if not response_label:
                label_dicts = mapping_config.get("label_dicts", {})
                response_label_dict = label_dicts.get(
                    f"response_field_{field_num}"
                )
                if response_label_dict and response_value in response_label_dict:
                    response_label = response_label_dict[response_value]

            responses.append(
                OntologyClass(
                    id=processed_id,
                    label=response_label or "Unknown Response",
                )
            )
        return responses

    def _get_field_value(self, data: Dict[str, Any], field_path: str) -> Any:
        if not data or not field_path:
            return None

        if "." in field_path:
            instrument, field = field_path.split(".", 1)
            inner = data.get(instrument)
            if isinstance(inner, dict):
                return inner.get(field)
            return data.get(field_path)

        return data.get(field_path)
