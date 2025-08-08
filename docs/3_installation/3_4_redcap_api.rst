.. _3_4:

Set up the REDCap API
======================



The REDCap API for RareLink is a RESTful web service that allows users to 
interact with REDCap programmatically. The API is designed to provide a simple 
and secure way to access REDCap data and metadata. The API is built on top of 
the REDCap API and provides a set of commands that allow users to perform 
various operations on REDCap data.

.. note::
    The REDCap API for RareLink is designed for developers and researchers who 
    are familiar with programming and web services. If you are not familiar 
    with these topics, seek help from someone who is.

API Set Up
----------

In your terminal, write:

.. code-block:: bash

    rarelink setup keys

This command guides you through setting up the REDCap API for RareLink. 
You will be prompted to enter:
- Your REDCap instance URL.
- Your REDCap API token.

To view your current configuration:

.. code-block:: bash

    rarelink setup view

To reset your REDCap API configuration:

.. code-block:: bash

    rarelink setup reset

.. tip:: 
   For help on any command, run:

.. code-block:: bash

    rarelink --help
