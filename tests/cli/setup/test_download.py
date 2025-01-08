# from typer.testing import CliRunner
# from rarelink.cli.redcap_setup.download import app as download_app
# from pathlib import Path
# from unittest.mock import patch

# runner = CliRunner()

# def test_rarelink_cdm_datadictionary_download():
#     """
#     Test the `rarelink-cdm-datadictionary` command.
#     """
#     with patch("rarelink.cli.redcap_setup.downloads.download_file") as mock_download_file:
#         mock_download_file.return_value = None  # Simulate successful download

#         result = runner.invoke(download_app, ["rarelink-cdm-datadictionary"])
#         print(result.stdout)  # Debug output

#         assert result.exit_code == 0
#         assert "RareLink RD-CDM Data Dictionary Download" in result.stdout
#         assert "Learn more about the RD-CDM here:" in result.stdout
#         assert "Use the `rarelink redcap-setup upload-data-dictionary` command to upload the dictionary." in result.stdout

#         mock_download_file.assert_called_once_with(
#             "https://rarelink.readthedocs.io/en/latest/_downloads/97061f8438c4a3bb907919a76a5ab2c6/rarelink_v2_0_0_dev0_datadictionary.csv",
#             Path.home() / "rarelink_rd_cdm_v2_0_0_dev0_data_dictionary_.csv",
#         )


# def test_rarelink_cdm_instruments_download():
#     """
#     Test the `rarelink-cdm-instruments` command.
#     """
#     with patch("rarelink.cli.redcap_setup.downloads.download_file") as mock_download_file:
#         mock_download_file.return_value = None  # Simulate successful download

#         result = runner.invoke(download_app, ["rarelink-cdm-instruments"])
#         print(result.stdout)  # Debug output

#         assert result.exit_code == 0
#         assert "RareLink RD-CDM Instruments Download" in result.stdout
#         assert "Learn more about the RD-CDM here:" in result.stdout

#         mock_download_file.assert_called_once_with(
#             "https://rarelink.readthedocs.io/en/latest/_downloads/8bb7dfc55de14eb8984091463842254e/rarelink_cdm_single_instruments.zip",
#             Path.home() / "rarelink_rd_cdm_v2_0_0_dev0_instruments.zip",
#         )


# def test_rarelink_template_project_download():
#     """
#     Test the `rarelink-template-project` command.
#     """
#     with patch("rarelink.cli.redcap_setup.downloads.download_file") as mock_download_file:
#         mock_download_file.return_value = None  # Simulate successful download

#         result = runner.invoke(download_app, ["rarelink-template-project"])
#         print(result.stdout)  # Debug output

#         assert result.exit_code == 0
#         assert "RareLink REDCap Project Download" in result.stdout
#         assert "Learn more about the RD-CDM here:" in result.stdout

#         mock_download_file.assert_called_once_with(
#             "http://127.0.0.1:8000/_downloads/25122ebc11409a8a4420e1a9dbd69fd8/rarelink_v2_0_0_redcap_project.xml",
#             Path.home() / "rarelink_redcap_project.xml",
#         )
