#!/usr/bin/env python

from example_config import config
import requests

fields = {
    'token': config['api_token'],
    'content': 'instrument',
    'format': 'json'
}

r = requests.post(config['api_url'],data=fields)
print('HTTP Status: ' + str(r.status_code))
print(r.text)