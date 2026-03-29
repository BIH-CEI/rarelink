# tests/integration/test_redcap_to_phenopacket_workflow.py
import unittest
import tempfile
import json
from pathlib import Path
from unittest.mock import patch, MagicMock

from rarelink.phenopackets import phenopacket_pipeline


class TestRedcapToPhenopacketWorkflow(unittest.TestCase):
    """Integration test for the complete REDCap to Phenopacket workflow."""

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.output_dir = Path(self.temp_dir.name)

        self.redcap_records = [
            {
                "record_id": "101",
                "redcap_repeat_instrument": "",
                "redcap_repeat_instance": "",
                "snomedct_184099003": "2020-01-05",
                "snomedct_263495000": "snomedct_394743007",
            },
            {
                "record_id": "101",
                "redcap_repeat_instrument": "rarelink_5_disease",
                "redcap_repeat_instance": "1",
                "snomedct_64572001_mondo": "MONDO:0019499",
                "snomedct_298059007": "2022-10-14",
            },
            {
                "record_id": "101",
                "redcap_repeat_instrument": "rarelink_6_2_phenotypic_feature",
                "redcap_repeat_instance": "1",
                "snomedct_8116006": "HP:0001059",
                "snomedct_8116006_onset": "2022-10-14",
            },
        ]

        self.linkml_records = [
            {
                "record_id": "101",
                "personal_information": {
                    "snomedct_184099003": "2020-01-05",
                    "snomedct_263495000": "snomedct_394743007",
                },
                "repeated_elements": [
                    {
                        "redcap_repeat_instrument": "rarelink_5_disease",
                        "redcap_repeat_instance": 1,
                        "disease": {
                            "snomedct_64572001_mondo": "MONDO:0019499",
                            "snomedct_298059007": "2022-10-14",
                        },
                    },
                    {
                        "redcap_repeat_instrument": "rarelink_6_2_phenotypic_feature",
                        "redcap_repeat_instance": 1,
                        "phenotypic_feature": {
                            "snomedct_8116006": "HP:0001059",
                            "snomedct_8116006_onset": "2022-10-14",
                        },
                    },
                ],
            }
        ]

        self.env_values = {
            "REDCAP_API_TOKEN": "a" * 32,
            "REDCAP_URL": "https://redcap.example.com/api/",
            "REDCAP_PROJECT_ID": "12345",
            "REDCAP_PROJECT_NAME": "Test Project",
            "BIORTAL_API_TOKEN": "b" * 32,
            "CREATED_BY": "Test User",
        }

        self.records_file = self.output_dir / "Test_Project-records.json"
        with open(self.records_file, "w") as f:
            json.dump(self.redcap_records, f)

        self.linkml_file = self.output_dir / "Test_Project-linkml-records.json"
        with open(self.linkml_file, "w") as f:
            json.dump(self.linkml_records, f)

        self.mapping_configs = {
            "individual": {
                "mapping_block": {
                    "id_field": "record_id",
                    "date_of_birth_field": "personal_information.snomedct_184099003",
                    "gender_field": "personal_information.snomedct_263495000",
                }
            },
            "vitalStatus": {
                "mapping_block": {
                    "status_field": "_default_",
                    "default_status": "ALIVE",
                }
            },
            "diseases": {
                "mapping_block": {
                    "redcap_repeat_instrument": "rarelink_5_disease",
                    "term_field_1": "snomedct_64572001_mondo",
                    "onset_date_field": "snomedct_298059007",
                }
            },
            "phenotypicFeatures": {
                "mapping_block": {
                    "redcap_repeat_instrument": "rarelink_6_2_phenotypic_feature",
                    "type_field": "snomedct_8116006",
                    "onset_date_field": "snomedct_8116006_onset",
                }
            },
            "metadata": {"code_systems": {}},
        }

        from typer.testing import CliRunner

        self.runner = CliRunner()

    def tearDown(self):
        self.temp_dir.cleanup()

    @patch("rarelink.cli.redcap.download_records.validate_env")
    @patch("rarelink.cli.redcap.download_records.dotenv_values")
    @patch("rarelink.cli.redcap.download_records.fetch_redcap_data")
    @patch("rarelink.cli.redcap.download_records.redcap_to_linkml")
    @patch("rarelink.cli.redcap.download_records.validate_linkml_data")
    def test_download_records_step(
        self, mock_validate_linkml, mock_redcap_to_linkml, mock_fetch_redcap,
        mock_dotenv, mock_validate_env,
    ):
        """REDCap download step calls all expected functions."""
        mock_dotenv.return_value = self.env_values
        mock_validate_env.return_value = None
        mock_fetch_redcap.return_value = self.records_file
        mock_redcap_to_linkml.return_value = None
        mock_validate_linkml.return_value = True

        import typer
        from rarelink.cli.redcap.download_records import app as download_records_command

        download_records_app = typer.Typer()
        download_records_app.command()(download_records_command)

        result = self.runner.invoke(
            download_records_app,
            ["--output-dir", str(self.output_dir), "--rarelink-cdm", "--records", ""],
            input="y\n",
        )
        self.assertEqual(result.exit_code, 0)
        mock_validate_env.assert_called()
        mock_fetch_redcap.assert_called_once()
        mock_redcap_to_linkml.assert_called_once()
        mock_validate_linkml.assert_called_once()

    @patch("rarelink.phenopackets.pipeline.write_phenopackets")
    @patch("rarelink.phenopackets.pipeline.create_phenopacket")
    def test_phenopacket_pipeline_step(self, mock_create, mock_write):
        """Pipeline creates phenopackets and calls write."""
        mock_phenopacket = MagicMock()
        mock_phenopacket.id = "101"
        mock_create.return_value = mock_phenopacket

        result = phenopacket_pipeline(
            input_data=self.linkml_records,
            output_dir=str(self.output_dir),
            created_by="Test User",
            mapping_configs=self.mapping_configs,
            timeout=10,
            debug=True,
        )
        self.assertIsNotNone(result)
        self.assertEqual(result.n_created, 1)
        self.assertEqual(result.n_failed_creation, 0)
        mock_create.assert_called_once()
        mock_write.assert_called_once()

    def test_validate_phenopackets_step(self):
        """Python-native validation passes for a well-formed phenopacket."""
        phenopacket_file = self.output_dir / "101.json"
        phenopacket_content = {
            "id": "101",
            "subject": {
                "id": "101",
                "taxonomy": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
            },
            "phenotypicFeatures": [
                {"type": {"id": "HP:0001059", "label": "Pterygium"}}
            ],
            "diseases": [
                {"term": {"id": "MONDO:0019499", "label": "Test Disease"}}
            ],
            "metaData": {
                "created": "2023-09-08T12:00:00Z",
                "createdBy": "Test User",
                "phenopacketSchemaVersion": "2.0",
            },
        }
        with open(phenopacket_file, "w") as f:
            json.dump(phenopacket_content, f)

        from rarelink.phenopackets.validate import validate_phenopackets

        success, _ = validate_phenopackets(phenopacket_file)
        self.assertTrue(success)

    @patch("rarelink.phenopackets.pipeline.write_phenopackets")
    @patch("rarelink.phenopackets.pipeline.create_phenopacket")
    @patch("rarelink.cli.redcap.download_records.validate_linkml_data")
    @patch("rarelink.cli.redcap.download_records.redcap_to_linkml")
    @patch("rarelink.cli.redcap.download_records.fetch_redcap_data")
    @patch("rarelink.cli.redcap.download_records.dotenv_values")
    @patch("rarelink.cli.redcap.download_records.validate_env")
    def test_full_workflow_integration(
        self, mock_env_validate, mock_dotenv, mock_fetch, mock_convert,
        mock_validate_linkml, mock_create, mock_write,
    ):
        """Full workflow: download, create phenopackets, validate."""
        mock_dotenv.return_value = self.env_values
        mock_env_validate.return_value = None
        mock_fetch.return_value = self.records_file
        mock_convert.return_value = None
        mock_validate_linkml.return_value = True

        mock_phenopacket = MagicMock()
        mock_phenopacket.id = "101"
        mock_create.return_value = mock_phenopacket

        import typer
        from rarelink.cli.redcap.download_records import app as download_records_command

        download_app = typer.Typer()
        download_app.command()(download_records_command)
        result = self.runner.invoke(
            download_app,
            ["--output-dir", str(self.output_dir), "--rarelink-cdm", "--records", ""],
            input="y\n",
        )
        self.assertEqual(result.exit_code, 0)

        pipeline_result = phenopacket_pipeline(
            input_data=self.linkml_records,
            output_dir=str(self.output_dir),
            created_by="Test User",
            mapping_configs=self.mapping_configs,
            timeout=10,
            debug=True,
        )
        self.assertEqual(pipeline_result.n_created, 1)

        phenopacket_file = self.output_dir / "101.json"
        phenopacket_content = {
            "id": "101",
            "subject": {
                "id": "101",
                "taxonomy": {"id": "NCBITaxon:9606", "label": "Homo sapiens"},
            },
            "metaData": {
                "created": "2023-09-08T12:00:00Z",
                "createdBy": "Test User",
                "phenopacketSchemaVersion": "2.0",
            },
        }
        with open(phenopacket_file, "w") as f:
            json.dump(phenopacket_content, f)

        from rarelink.phenopackets.validate import validate_phenopackets

        valid, _ = validate_phenopackets(phenopacket_file)
        self.assertTrue(valid)

        mock_fetch.assert_called_once()
        mock_convert.assert_called_once()
        mock_validate_linkml.assert_called_once()
        mock_create.assert_called_once()
        mock_write.assert_called_once()


if __name__ == "__main__":
    unittest.main()