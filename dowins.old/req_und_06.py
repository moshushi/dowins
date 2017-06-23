# -*- encoding: utf-8 -*-

import requests

BASE_URL = u'https://www.instagram.com/sa.ny.aa/'
QUERY_URL = u'https://www.instagram.com/query/'
BZ_URL = u'https://www.instagram.com/ajax/bz/'
INS_URL = u'https://www.instagram.com/'

s = requests.session()
r = s.get(BASE_URL)
print r.status_code
# print r.headers
csrftoken = r.cookies['csrftoken']
print csrftoken
mid = r.cookies['mid']
print mid

# c = requests.utils.dict_from_cookiejar(s.cookies)
# print c
# print c['csrftoken']

# print s.cookies

cookies = {
    'mid': mid,
    'ig_vw': '1920',
    'ig_pr': '1',
    's_network': '""',
    'csrftoken': csrftoken
}

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'

headers = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4',
    'Connection': 'keep-alive',
    'Content-Length': '253',
    'Host': 'www.instagram.com',
    'Origin': 'https://www.instagram.com',
    'Referer': 'https://www.instagram.com/sa.ny.aa/',
    'User-Agent': user_agent,
    'X-csrftoken': csrftoken,
    'X-Instagram-AJAX': '1',
    'X-Requested-With': 'XMLHttpRequest'
}

p = requests.post(QUERY_URL, cookies=cookies, headers=headers)
print p.status_code

