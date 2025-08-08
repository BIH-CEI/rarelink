.. _3_3:

REDCap API
================

The REDCap API for RareLink is a RESTful web service that allows users to 
interact with REDCap programmatically. The API is designed to provide a simple 
and secure way to access REDCap data and metadata. The API is built on top of 
the REDCap API and provides a set of endpoints that allow users to perform 
various operations on REDCap data.


API Set Up
------------

>>> config = dict(
>>>    api_token       = 'your_api_token',
>>>    api_url         = 'http://example.com/redcap/api/',
>>>    api_super_token = 'your_super_token'
>>> ) 


API Endpoints
-------------

Export Records
~~~~~~~~~~~~~~

The Export Records endpoint allows users to export records from REDCap.

#!/usr/bin/env python

>>> .config import config
>>> import requests
>>> 
>>> fields = {
>>>     'token': config['api_token'],
>>>     'content': 'record',
>>>     'format': 'json',
>>>     'type': 'flat'
>>> }
>>> 
>>> r = requests.post(config['api_url'],data=fields)
>>> print('HTTP Status: ' + str(r.status_code))
>>> print(r.text)


Export Project
~~~~~~~~~~~~~~

The Export Project endpoint allows users to export the entire project from REDCap.


>>> from .config import config
>>> import requests
>>> 
>>> fields = {
>>>     'token': config['api_token'],
>>>     'content': 'project_xml',
>>>     'returnMetadataOnly': 'false',
>>>     'exportSurveyFields': 'false',
>>>     'exportDataAccessGroups': 'false',
>>>     'returnFormat': 'json'
>>> }
>>> 
>>> r = requests.post(config['api_url'],data=fields)
>>> print('HTTP Status: ' + str(r.status_code))
>>> print(r.text)

Export Field Names
~~~~~~~~~~~~~~~~~~

The Export Field Names endpoint allows users to export field names from REDCap.

>>> from .config import config
>>> import requests
>>> 
>>> fields = {
>>>    'token': config['api_token'],
>>>    'content': 'exportFieldNames',
>>>    'format': 'json',
>>>    'field': 'first_name'
>>> }
>>> 
>>> r = requests.post(config['api_url'],data=fields)
>>> print('HTTP Status: ' + str(r.status_code))
>>> print(r.text)


Import Records
~~~~~~~~~~~~~~

The Import Records endpoint allows users to import records into REDCap.
tba.


Import Project
~~~~~~~~~~~~~~

The Import Project endpoint allows users to import a project into REDCap.

>>> from .config import config
>>> import requests
>>> import json
>>>
>>> record = {
>>>    'project_title': 'Project ABC',
>>>    'purpose': 0,
>>>    'purpose_other': '',
>>>    'project_notes': 'Some notes about the project'
>>> }
>>> 
>>> data = json.dumps(record)
>>> 
>>> fields = {
>>>     'token': config['api_super_token'],
>>>     'content': 'project',
>>>     'format': 'json',
>>>     'data': data,
>>> }
>>> 
>>> r = requests.post(config['api_url'],data=fields)
>>> print('HTTP Status: ' + str(r.status_code))
>>> print(r.text)



