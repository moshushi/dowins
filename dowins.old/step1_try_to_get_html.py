# -*- encoding: utf-8 -*-
"""
Try to get html page from Instagram
"""

import requests

BASE_URL = "https://www.instagram.com/"
NAME_ACCOUNT = "abc"

url = BASE_URL + NAME_ACCOUNT
r = requests.get(url)
data = r.text.encode('utf-8')
print data

with open('test.html', 'w') as output_file:
#     output_file.write(r.text.encode('utf-8'))
    output_file.write(data)
