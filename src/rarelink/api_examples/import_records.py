#!/usr/bin/env python

from config import config
import requests, hashlib, json

record = {
    'record_id': hashlib.sha1().hexdigest()[:16],
    'first_name': 'First',
    'last_name': 'Last',
    'address': '123 Cherry Lane\nNashville, TN 37015',
    'telephone': '(615) 255-4000',
    'email': 'first.last@gmail.com',
    'dob': '1972-08-10',
    'age': 43,
    'ethnicity': 1,
    'race': 4,
    'sex': 1,
    'height': 180,
    'weight': 105,
    'bmi': 31.4,
    'comments': 'comments go here',
    'redcap_event_name': 'events_2_arm_1',
    'basic_demography_form_complete': '2',
}

data = json.dumps([record])

fields = {
    'token': config['api_token'],
    'content': 'record',
    'format': 'json',
    'type': 'flat',
    'data': data,
}

r = requests.post(config['api_url'],data=fields)
print('HTTP Status: ' + str(r.status_code))
print(r.text)