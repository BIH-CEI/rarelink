#!/usr/bin/env python

from config import config
import requests

fields = {
    'token': config['api_token'],
    'content': 'participantList',
    'instrument': 'test_instrument',
    'event': 'event_1_arm_1',
    'format': 'json'
}

r = requests.post(config['api_url'],data=fields)
print('HTTP Status: ' + str(r.status_code))
print(r.text)