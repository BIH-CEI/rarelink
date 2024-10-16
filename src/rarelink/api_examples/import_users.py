#!/usr/bin/env python

from config import config
import requests, json

record = {
    'username':                 'test_user_47',
    'expiration':               '2016-01-01',
    'data_access_group':        1,
    'data_export':              1,
    'mobile_app':               1,
    'mobile_app_download_data': 1,
    'lock_record_multiform':    1,
    'lock_record':              1,
    'lock_record_customize':    1,
    'record_delete':            1,
    'record_rename':            1,
    'record_create':            1,
    'api_import':               1,
    'api_export':               1,
    'api_modules':              1,
    'data_quality_execute':     1,
    'data_quality_design':      1,
    'file_repository':          1,
    'data_logging':             1,
    'data_comparison_tool':     1,
    'data_import_tool':         1,
    'calendar':                 1,
    'graphical':                1,
    'reports':                  1,
    'user_rights':              1,
    'design':                   1,
}

data = json.dumps([record])

fields = {
    'token': config['api_token'],
    'content': 'user',
    'format': 'json',
    'data': data,
}

r = requests.post(config['api_url'],data=fields)
print('HTTP Status: ' + str(r.status_code))
print(r.text)