import requests
import requests.utils
import pickle
import http.cookiejar
import json
"""
Get and write to file resp.cookies['csrftoken'] and resp.headers['set-cookie']
"""


r = requests.get('https://instagram.com')
print (r.cookies)

my_cookies = requests.utils.dict_from_cookiejar(r.cookies)
my_cookies_str = json.dumps(my_cookies)
with open('new_cookie_string_jar.txt', 'w') as f:
    f.write(my_cookies_str)

print ("------")
cookie_string = r.headers['set-cookie']
print(cookie_string)

with open('new_cookie_string.txt', 'w') as f:
    f.write(cookie_string)
# if __name__ == '__main__':


# print (type(my_cookies))
# print ( json.dumps(my_cookies))
# print (dir(requests.utils))
# new_cookeis = requests.utils.cookiejar_from_dict(my_cookies)
# print ('====')
# print ('AAAAA')
# print (type(json.dumps(my_cookies)))
# print ('====')
# print(type(new_cookeis))
# print(new_cookeis)
