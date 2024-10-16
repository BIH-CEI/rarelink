#!/usr/bin/env python

from config import config
import requests, json

fields = {
    'token': config['api_token'],
    'content': 'event',
    'action': 'delete',
    'format': 'json',
    'events[0]': 'event_1_arm_1'
}

r = requests.post(config['api_url'],data=fields)
print('HTTP Status: ' + str(r.status_code))
print(r.text)