#!/usr/bin/env python

from config import config
import requests, json

record = {
    'data_access_group_name': 'Group API',
    'unique_group_name': ''
}

data = json.dumps([record])

fields = {
    'token': config['api_token'],
    'content': 'dag',
    'action': 'import',
    'format': 'json',
    'data': data,
}

r = requests.post(config['api_url'],data=fields)
print('HTTP Status: ' + str(r.status_code))
print(r.text)