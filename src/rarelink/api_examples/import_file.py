#!/usr/bin/env python

from config import config
import requests

file = '/tmp/test_file.txt'


fields = {
    'token': config['api_token'],
    'content': 'file',
    'action': 'import',
    'record': 'f21a3ffd37fc0b3c',
    'field': 'file_upload',
    'event': 'event_1_arm_1',
    'returnFormat': 'json'
    # 'file': (pycurl.FORM_FILE, file)
}

# fields['returnFormat'] = 'json';

file_obj = open(file_path, 'rb')
r = requests.post(config['api_url'],data=fields,files={'file':file_obj})
file_obj.close()

print('HTTP Status: ' + str(r.status_code))
print(r.text)