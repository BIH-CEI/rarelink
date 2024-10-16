#!/usr/bin/env python

from config import config
import requests, json

record = {
    'arm': {
        'number': 1,
        'event': [
            {
                'unique_event_name': 'event_1_arm_1',
                'form': ['instr_1', 'instr_2',]
            },
            {
                'unique_event_name': 'event_2_arm_1',
                'form': ['instr_1',]
            },
        ]
    }
}

data = json.dumps([record])

fields = {
    'token': config['api_token'],
    'content': 'formEventMapping',
    'format': 'json',
    'data': data,
}

r = requests.post(config['api_url'],data=fields)
print('HTTP Status: ' + str(r.status_code))
print(r.text)