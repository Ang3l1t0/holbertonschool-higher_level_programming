#!/usr/bin/python3
"""Response header value #1"""

import requests
from sys import argv

r = requests.get(argv[1])
print(r.headers.get('X-Request-Id'))
