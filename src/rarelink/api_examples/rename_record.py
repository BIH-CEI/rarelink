#!/usr/bin/env python
from config import config
import requests, json

fields = {
    'token': config['api_token'],
    'action': 'rename',
    'content': 'record',
    'record': '1',
    'new_record_name': 'record_1',
    'arm': '1',
    'returnFormat': 'json'
}
r = requests.post(config['api_url'],data=fields)
print('HTTP Status: ' + str(r.status_code))
print(r.text)