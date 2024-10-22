#!/usr/bin/env python

from example_config import config
import requests

fields = {
    'token': config['api_token'],
    'content': 'surveyLink',
    'record': 'f21a3ffd37fc0b3c',
    'instrument': 'test_instrument',
    'event': 'event_1_arm_1',
    'format': 'json'
}

r = requests.post(config['api_url'],data=fields)
print('HTTP Status: ' + str(r.status_code))
print(r.text)