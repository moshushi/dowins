import requests
import httpretty
import dowins


with open('cookie_string.txt', 'r') as f:
    str_cookie = f.readline()


# @httpretty.activate

def get_csrf(url):
    r = requests.get(url)
    return r.cookies

print(get_csrf('https://twitter.com/'))
print('---')

@httpretty.activate
def role():
    httpretty.register_uri(httpretty.GET, 'https://twitter.com',
                           body='[{"title": "Test"}]',
                           content_type="application/json",
                           adding_headers={
                               'set-cookie': str_cookie
                           })
    r = requests.get('https://twitter.com/')
    print(r.cookies)

role()
