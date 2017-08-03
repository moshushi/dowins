import requests
import requests.utils
import http.cookiejar
import json
import httpretty
"""
Better now
Read from file cookie and check how to work
"""


with open('new_cookie_string_jar.txt', 'r') as f:
    my_cookies_str = f.readline()
    my_cookies_dic = json.loads(my_cookies_str)
    my_cookies_jar = requests.utils.cookiejar_from_dict(my_cookies_dic)


with open('new_cookie_string.txt', 'r') as f:
    cookie_string = f.readline()


def get_csrf(url):
    r = requests.get(url)
    return r.cookies

def get_cookie_string(url):
    r = requests.get(url)
    return r.headers['set-cookie']

r = requests.get('https://twitter.com')
print (r.status_code)
print (r.cookies)
print ('----')

httpretty.enable()
httpretty.register_uri(httpretty.GET, "https://twitter.com/",
                       body="TEST", status=201,
                       adding_headers={
                           'set-cookie': cookie_string
                       },
                       cookies=my_cookies_jar)

r = requests.get('https://twitter.com')
print (r.status_code)
print (r.cookies)

httpretty.disable()

# print("====")
# print (my_cookies_jar)
