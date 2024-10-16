#!/usr/bin/env python

from config import config
import requests, json

fields = {
    'token': config['api_token'],
    'content': 'dag',
    'action': 'delete',
    'format': 'json',
    'dags[0]': 'group_api'
}

r = requests.post(config['api_url'],data=fields)
print('HTTP Status: ' + str(r.status_code))
print(r.text)