#!/usr/bin/env python

from config import config
import requests

fields = {
    'token': config['api_token'],
    'content': 'log',
    'format': 'json',
    'logtype': '',
    'user': '',
    'record': '',
    'beginTime': '10/06/2020 17:37',
    'endTime': '',
}

r = requests.post(config['api_url'],data=fields)
print('HTTP Status: ' + str(r.status_code))
print(r.text)