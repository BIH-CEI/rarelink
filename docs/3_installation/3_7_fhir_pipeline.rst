.. _3_7: 

FHIR Pipeline Installation
==========================

.. attention::
   To use your local REDCap project, you will need to set up a local REDCap 
   instance. For this please contact your local REDCap administratior. A project
   name could for example be "RareLink - Your local REDCap location". 

The RareLink CDM to FHIR will be preconfigured and executable via the RareLink 
CLI creating FHIR resources based on the International Patient Summary (IPS) and 
its RareLink CDM extension profiles. These profiles will be published on
Simplifier.

.. note::
    This section is still to be implemented in the docuemntation and the RareLink
    command line interface.


Via the RareLink CLI type:  

.. code-block:: bash

    rarelink setup -pipeline toFHIR

