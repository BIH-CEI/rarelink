#!/usr/bin/env python

from config import config
import requests, json

record = {
    'project_title': 'Project ABC',
    'purpose': 0,
    'purpose_other': '',
    'project_notes': 'Some notes about the project'
}

data = json.dumps(record)

fields = {
    'token': config['api_super_token'],
    'content': 'project',
    'format': 'json',
    'data': data,
}

r = requests.post(config['api_url'],data=fields)
print('HTTP Status: ' + str(r.status_code))
print(r.text)