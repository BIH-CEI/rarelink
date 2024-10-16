#!/usr/bin/env python

from config import config
import requests, json

record = {
    'event_name': 'Event 1',
    'arm_num': 1,
    'day_offset': 0,
    'offset_min': 0,
    'offset_max': 0,
    'unique_event_name': 'event_1_arm_1'
}

data = json.dumps([record])

fields = {
    'token': config['api_token'],
    'content': 'event',
    'action': 'import',
    'format': 'json',
    'override': 0,
    'data': data,
}

r = requests.post(config['api_url'],data=fields)
print('HTTP Status: ' + str(r.status_code))
print(r.text)