#!/usr/bin/env python

from config import config
import requests, json

fields = {
    'token': config['api_token'],
    'content': 'userRole',
    'action': 'delete',
    'format': 'json',
    'roles[0]': 'U-522RX7WM49'
}

r = requests.post(config['api_url'],data=fields)
print('HTTP Status: ' + str(r.status_code))
print(r.text)