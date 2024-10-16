#!/usr/bin/env python
from config import config
import requests, json

fields = {
    'token': config['api_token'],
    'action': 'delete',
    'content': 'record',
    'records[0]': '1',
    'arm': '1',
    'instrument': 'demographics',
    'event': 'visit_1_arm_1',
    'returnFormat': 'json'
}
r = requests.post(config['api_url'],data=fields)
print('HTTP Status: ' + str(r.status_code))
print(r.text)