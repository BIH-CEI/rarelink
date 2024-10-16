#!/usr/bin/env python

from config import config
import requests, json

fields = {
    'token': config['api_token'],
    'content': 'user',
    'action': 'delete',
    'format': 'json',
    'users[0]': 'test_user_47'
}

r = requests.post(config['api_url'],data=fields)
print('HTTP Status: ' + str(r.status_code))
print(r.text)