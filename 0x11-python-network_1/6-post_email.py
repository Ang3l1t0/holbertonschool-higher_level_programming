#!/usr/bin/python3
"""POST an email #1"""

import requests
from sys import argv

url = argv[1]
my_obj = {'email': argv[2]}

r = requests.post(url, data=my_obj)
print r.text
