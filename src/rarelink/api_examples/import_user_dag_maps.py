#!/usr/bin/env python

from config import config
import requests, json

record = {
    'username': 'testuser',
    'redcap_data_access_group': 'api_testing_group'
}

data = json.dumps([record])

fields = {
    'token': config['api_token'],
    'content': 'userDagMapping',
    'action': 'import',
    'format': 'json',
    'data': data,
}

r = requests.post(config['api_url'],data=fields)
print('HTTP Status: ' + str(r.status_code))
print(r.text)