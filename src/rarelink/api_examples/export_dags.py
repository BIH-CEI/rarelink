#!/usr/bin/env python

from config import config
import requests

fields = {
    'token': config['api_token'],
    'content': 'dag',
    'format': 'json'
}

r = requests.post(config['api_url'],data=fields)
print('HTTP Status: ' + str(r.status_code))
print(r.text)