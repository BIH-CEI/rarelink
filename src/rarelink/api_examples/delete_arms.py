#!/usr/bin/env python

from config import config
import requests, json

fields = {
    'token': config['api_token'],
    'content': 'arm',
    'action': 'delete',
    'format': 'json',
    'arms[0]': '1'
}

r = requests.post(config['api_url'],data=fields)
print('HTTP Status: ' + str(r.status_code))
print(r.text)