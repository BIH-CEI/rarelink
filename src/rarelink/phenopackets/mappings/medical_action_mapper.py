# src/rarelink/phenopackets/mappings/medical_action_mapper.py
from typing import Dict, Any, List, Optional
import logging
from phenopackets import (
    MedicalAction,
    Procedure,
    Treatment,
    OntologyClass,
    TimeElement,
    Age,
    Quantity
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
        """
        Map data to a list of MedicalAction entities.

        Args:
            data (Dict[str, Any]): Input data.
            **kwargs: Additional parameters (e.g., dob)

        Returns:
            List[MedicalAction]: List of mapped MedicalAction entities.
        """
        # Force multi-entity mapping
        self.processor.mapping_config["multi_entity"] = True
        return super().map(data, **kwargs)

    def _map_single_entity(
        self, data: Dict[str, Any], instruments: List[str], **kwargs
    ) -> Optional[MedicalAction]:
        logger.warning(
            "MedicalActionMapper._map_single_entity called, but this mapper returns multiple entities"
        )
        return None

    def _map_multi_entity(
        self, data: Dict[str, Any], instruments: List[str], **kwargs
    ) -> List[MedicalAction]:
        dob = kwargs.get("dob")
        medical_actions: List[MedicalAction] = []
        mapping_config = self.processor.mapping_config

        # Determine processor type based on treatment-specific fields
        is_treatment_processor = (
            "agent_field_1" in mapping_config or "cumulative_dose" in mapping_config
        )
        if is_treatment_processor:
            logger.debug("Mapping treatment-based medical actions")
            medical_actions.extend(self._map_treatments(data, dob))
        else:
            logger.debug("Mapping procedure-based medical actions")
            medical_actions.extend(self._map_procedures(data, dob))

        logger.debug(f"Generated {len(medical_actions)} medical actions")
        return medical_actions

    def _map_procedures(
        self, data: Dict[str, Any], dob: Optional[str]
    ) -> List[MedicalAction]:
        medical_actions: List[MedicalAction] = []
        instrument_name = self.processor.mapping_config.get("redcap_repeat_instrument")
        repeated_elements = data.get("repeated_elements", [])
        if not repeated_elements and instrument_name in data:
            repeated_elements = [data]

        # Filter elements for this instrument
        procedure_elements = [
            element
            for element in repeated_elements
            if element.get("redcap_repeat_instrument") == instrument_name
        ]
        if not procedure_elements and instrument_name in data:
            procedure_elements = [data]

        # Find procedure fields defined in the configuration
        procedure_fields = {
            k: v
            for k, v in self.processor.mapping_config.items()
            if k.startswith("procedure_field_") and isinstance(v, str)
        }
        logger.debug(f"Found procedure fields: {procedure_fields}")

        for element in procedure_elements:
            for proc_key, field_path in procedure_fields.items():
                procedure_details = self._get_field_value(element, field_path)
                if not procedure_details:
                    logger.debug(
                        f"No procedure details found for {proc_key} (field: {field_path})"
                    )
                    continue

                performed_field = self.processor.mapping_config.get("performed")
                is_performed = (
                    performed_field is None
                    or self._get_field_value(element, performed_field) is not None
                )
                if not is_performed:
                    logger.debug(f"Procedure {proc_key} not performed; skipping")
                    continue

                procedure = self._create_procedure({proc_key: procedure_details}, dob)
                if procedure:
                    medical_action = MedicalAction(procedure=procedure)
                    medical_actions.append(medical_action)
                    logger.debug(
                        f"Created medical action with procedure for field {proc_key}"
                    )
        return medical_actions

    def _map_treatments(
        self, data: Dict[str, Any], dob: Optional[str]
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

        # Filter elements for the given instrument
        instrument_elements = [
            element
            for element in repeated_elements
            if element.get("redcap_repeat_instrument") == instrument_name
        ]
        logger.debug(
            f"Found {len(instrument_elements)} treatment elements for instrument {instrument_name}"
        )

        processed_instances = set()
        seen_agents = set()
        for element in instrument_elements:
            try:
                instance_id = element.get("redcap_repeat_instance")
                element_key = f"{instrument_name}:{instance_id}"
                if element_key in processed_instances:
                    logger.debug(f"Skipping duplicate instance: {element_key}")
                    continue
                processed_instances.add(element_key)

                instrument_data = element.get(instrument_name)
                if not instrument_data:
                    logger.debug(
                        f"No instrument data found for element {element_key}"
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
                    logger.debug(f"Skipping duplicate agent: {agent_id}")
                    continue
                seen_agents.add(agent_id)

                treatment = self._create_treatment(
                    instrument_data, dob, instrument_name, element
                )
                if treatment:
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
                            target = OntologyClass(id=target_id, label=target_label)
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
                            intent = OntologyClass(id=intent_id, label=intent_label)
                            medical_action.treatment_intent.CopyFrom(intent)
                    medical_actions.append(medical_action)
                    logger.debug(
                        f"Created medical action with treatment for instance {instance_id}"
                    )
            except Exception as e:
                logger.error(
                    f"Error processing treatment element for {instrument_name}: {e}"
                )
        return medical_actions

    def _create_treatment(
        self,
        instrument_data: Dict[str, Any],
        dob: Optional[str],
        instrument_name: str = "",
        full_element: Optional[Dict[str, Any]] = None,
    ) -> Optional[Treatment]:
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
                    agent_label = self.processor.fetch_label_from_enum(agent_id, enum_class)
                    if agent_label:
                        break
        if not agent_label:
            agent_label = "Unknown Agent"
            logger.debug("Using default 'Unknown Agent' label")
        agent = OntologyClass(id=processed_id, label=agent_label)

        # Extract cumulative dose
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
                    quantity = Quantity(
                        value=dose_value,
                        unit=OntologyClass(id="UO:0000307", label="dose unit"),
                    )
                    cumulative_dose = quantity
                except (ValueError, TypeError):
                    logger.warning(f"Could not convert dose value '{dose_value}' to float")

        treatment = Treatment(
            agent=agent,
            cumulative_dose=cumulative_dose,
            
        )
        return treatment

    def _extract_adverse_events(self, instrument_data: Dict[str, Any]) -> List[OntologyClass]:
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
                ae_label = self.processor.fetch_label(ae_value) or "Unknown Adverse Event"
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
                ae_other_label = self.processor.fetch_label(ae_other_value) or "Unknown Adverse Event"
                adverse_events.append(OntologyClass(id=ae_other_id, label=ae_other_label))
        return adverse_events

    def _extract_treatment_response(self, instrument_data: Dict[str, Any]) -> List[OntologyClass]:
        responses: List[OntologyClass] = []
        mapping_config = self.processor.mapping_config
        response_fields = {}
        for key, value in mapping_config.items():
            if key.startswith("response_field_") and value:
                try:
                    field_num = int(key.split("_")[-1])
                    response_fields[field_num] = value
                except ValueError:
                    logger.warning(f"Invalid response field key format: {key}")
        for field_num in sorted(response_fields.keys()):
            response_field = response_fields[field_num]
            field_name = (
                response_field.split(".")[-1]
                if "." in response_field
                else response_field
            )
            response_value = instrument_data.get(field_name)
            if not response_value:
                logger.debug(f"No value found for response field {field_num}")
                continue
            processed_response_id = self.processor.process_code(response_value)
            response_label = self.processor.fetch_label(response_value)
            if not response_label and processed_response_id != response_value:
                response_label = self.processor.fetch_label(processed_response_id)
            if not response_label:
                label_dicts = mapping_config.get("label_dicts", {})
                response_label_dict = label_dicts.get(f"response_field_{field_num}")
                if response_label_dict and response_value in response_label_dict:
                    response_label = response_label_dict[response_value]
            if not response_label:
                response_label = "Unknown Response"
            response = OntologyClass(id=processed_response_id, label=response_label)
            responses.append(response)
            logger.debug(f"Added response {response.id} - {response.label}")
        return responses

    def _create_procedure(self, procedure_data: Dict[str, Any], dob: Optional[str]) -> Optional[Procedure]:
        procedure_code = None
        procedure_key = None
        # Expect a single key/value pair in procedure_data
        for key, value in procedure_data.items():
            procedure_code = value
            procedure_key = key
            break
        if not procedure_code:
            logger.debug("No procedure code found in data")
            return None

        mapping_config = self.processor.mapping_config
        enum_classes = mapping_config.get("enum_classes", {})
        procedure_label = None
        for prefix, enum_class_path in enum_classes.items():
            if procedure_code.startswith(prefix):
                try:
                    module_path, class_name = enum_class_path.rsplit('.', 1)
                    module = __import__(module_path, fromlist=[class_name])
                    enum_class = getattr(module, class_name)
                    procedure_label = self.processor.fetch_label_from_enum(procedure_code, enum_class)
                    if procedure_label:
                        break
                except Exception as e:
                    logger.warning(f"Could not fetch label from enum class {enum_class_path}: {e}")
        processed_code = self.processor.process_code(procedure_code)
        code = OntologyClass(id=processed_code, label=procedure_label or "Unknown Procedure")
        performed = None
        procedure_date_field = self.processor.mapping_config.get(f"{procedure_key}_date")
        if procedure_date_field:
            procedure_date = self._get_field_value(procedure_data, procedure_date_field)
            if procedure_date and dob:
                try:
                    iso_age = self.processor.convert_date_to_iso_age(procedure_date, dob)
                    if iso_age:
                        performed = TimeElement(age=Age(iso8601duration=iso_age))
                except Exception as date_error:
                    logger.warning(f"Could not calculate age at procedure: {date_error}")
        procedure = Procedure(code=code, performed=performed)
        return procedure

    def _get_field_value(self, data: Dict[str, Any], field_path: str) -> Any:
        if not data or not field_path:
            return None
        if "." in field_path:
            parts = field_path.split(".", 1)
            instrument, field = parts
            if instrument in data and isinstance(data[instrument], dict):
                return data[instrument].get(field)
            return data.get(field_path)
        return data.get(field_path)
