#!/usr/bin/env python

from config import config
import requests, json

record = {
    'arm_num': 1,
    'name': 'Arm 1'
}

data = json.dumps([record])

fields = {
    'token': config['api_token'],
    'content': 'arm',
    'action': 'import',
    'format': 'json',
    'override': 0,
    'data': data,
}

r = requests.post(config['api_url'],data=fields)
print('HTTP Status: ' + str(r.status_code))
print(r.text)