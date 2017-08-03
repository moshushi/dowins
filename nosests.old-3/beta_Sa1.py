import requests
import requests.utils
import pickle
import http.cookiejar
import json

# r = requests.get('https://twitter.com')

# print (r.cookies)
# print (type(r.cookies))

# r.cookies = http.cookiejar.LWPCookieJar(filename="test.cookies")
# r = requests.get('https://twitter.com')
# jar = r.cookies
# print(dir(jar))
# print('---')
# print (r.cookies.extract_cookies)
# with open('somefile', 'w') as f:
#     pickle(requests.utils.dict_from_cookiejar(r.cookies), f)
# print (dir(requests.utils))

r = requests.get('https://twitter.com')
print (r.cookies)
my_cookies = requests.utils.dict_from_cookiejar(r.cookies)
print (type(my_cookies))
# print ( json.dumps(my_cookies))
# print (dir(requests.utils))
new_cookeis = requests.utils.cookiejar_from_dict(my_cookies)
print ('====')
print(type(new_cookeis))
print(new_cookeis)
