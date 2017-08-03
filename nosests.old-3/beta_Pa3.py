import requests
import httpretty
import dowins
from cookielib import CookieJar, Cookie


with open('cookie_string.txt', 'r') as f:
    str_cookie = f.readline()

def get_csrf(url):
    r = requests.get(url)
    return r.cookies

def get_status(url):
    r = requests.get(url)
    return r.status_code

print(get_csrf('https://twitter.com/'))
print (get_status('https://twitter.com/'))
print('---')


httpretty.enable()
httpretty.register_uri(httpretty.GET, "https://twitter.com/",
                       body="TEST", status=201,
                       adding_headers={
                           'set-cookie': str_cookie
                       })
print (get_status('https://twitter.com/'))
print(get_csrf('https://twitter.com/'))
print (get_status('https://twitter.com/'))
