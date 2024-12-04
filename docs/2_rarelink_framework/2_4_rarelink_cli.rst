.. _2_4:

RareLink CLI
=============

The RareLink Command Line Interface (CLI) is a tool that allows you to interact
 with the RareLink framework. The CLI provides a set of commands that allow you
  to set up and manage the RareLink framework, as well as to interact with the 
  data stored in the framework. The CLI is designed to be user-friendly and
   intuitive, and it provides a simple and efficient way to work with the
    RareLink framework.



General CLI Command Groups
--------------------------


Framework Setup (`framework-setup`)
_________________________________

Commands related to setting up and managing the overall RareLink framework:

- `install`
- `reset`
- `status`
- `update`

REDCap Setup (redcap-setup)
___________________________

Commands focused on configuring REDCap, setting up projects, and initializing API access:
redcap-project-setup (guided project setup, documentation links, admin instructions)
redcap-api-setup (API token configuration and management)
download-data-dictionary (download the REDCap data dictionary)
upload-data-dictionary (upload a custom data dictionary)
REDCap Tools (redcap-tools)

Commands for interacting with an already-configured REDCap instance:
download-records (fetch records as JSON files)
upload-records (upload records from JSON files)
fetch-metadata (download metadata such as field labels and configurations)