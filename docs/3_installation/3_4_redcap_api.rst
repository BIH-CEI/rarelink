.. _3_3:

REDCap API
================

.. attention::
   To use your local REDCap project, you will need to set up a local REDCap 
   instance. For this please contact your local REDCap administratior. A project
   name could for example be "RareLink - Your local REDCap location". 

The REDCap API for RareLink is a RESTful web service that allows users to 
interact with REDCap programmatically. The API is designed to provide a simple 
and secure way to access REDCap data and metadata. The API is built on top of 
the REDCap API and provides a set of endpoints that allow users to perform 
various operations on REDCap data.

.. attention::
    The RareLink Terminal Command Line Interface (CLI) is currently still under 
    development. Below you find some API endpoints that will be available in the
    RareLink CLI.

.. note::
    The REDCap API for RareLink is designed to be used by developers and 
    researchers who are familiar with programming and web services. If you are 
    not familiar with programming or web services, you may want to seek help 
    from someone who is.

API Set Up
------------

In your terminal write... 

.. code-block:: bash

   rarelink setup -api


.. code-block:: bash

    rarelink setup -api enable
    rarelink setup -api test


.. tip:: 
    run 
    .. code-block:: bash
        
        rarelink -help <command>

    to get more help on all commands.


API Endpoints
-------------

Export Records
~~~~~~~~~~~~~~

The Export Records endpoint allows users to export records from REDCap.

.. code-block:: bash

    rarelink api -export -records


Export Project
~~~~~~~~~~~~~~

.. code-block:: bash

    rarelink api -export -project


Import Records
~~~~~~~~~~~~~~

The Import Records endpoint allows users to import records into REDCap.
tba.

.. code-block:: bash

    rarelink api -import -records


Import Project
~~~~~~~~~~~~~~

The Import Project endpoint allows users to import the preconfigured RareLink 
project into your local REDCap. 

.. code-block:: bash
    
    rarelink api -import -project       


.. note::
    alternatively you can also download the .toml file here:
    :download:`Download RareLink REDCap Project <../_static/res/rarelink_redcap_project.toml>`


