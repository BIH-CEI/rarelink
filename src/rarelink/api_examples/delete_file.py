#!/usr/bin/env python

from config import config
import requests

fields = {
    'token': config['api_token'],
    'content': 'file',
    'action': 'delete',
    'record': 'f21a3ffd37fc0b3c',
    'field': 'file_upload',
    'event': 'event_1_arm_1',
}

fields['returnFormat'] = 'json'

r = requests.post(config['api_url'],data=fields)
print('HTTP Status: ' + str(r.status_code))
print(r.text)