#!/usr/local/bin/python3
# Elena Tolpygo Cranley

"""
weather, due 9/18: Write a program that gets the current temperature at your location from the wunderground.com API.
"""

import urllib.request, json

secret_key = '6053d5fd9da3923d'
url = 'http://api.wunderground.com/api/' + secret_key + '/conditions/q/CA/San_Francisco.json'

response = urllib.request.urlopen(url)
str_response = response.readall().decode('utf-8')
obj = json.loads(str_response)

temp_F = obj['current_observation']['temp_f']
temp_C = obj['current_observation']['temp_c']
temp_string = obj['current_observation']['temperature_string']
city = obj['current_observation']['display_location']['city']
state = obj['current_observation']['display_location']['state']

print("Current temperature in " + city + ", " + state + " is: " + temp_string)