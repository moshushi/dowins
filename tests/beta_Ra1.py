import requests
import responses


with open('cookie_string.txt', 'r') as f:
    str_cookie = f.readline()


def get_csrf(url):
    r = requests.get(url)
    return r.cookies

def get_status(url):
    r = requests.get(url)
    return r.status_code

# print(get_csrf('https://twitter.com/'))
print (get_status('https://twitter.com/'))
print('---')

with responses.RequestsMock() as rsps:
# responses.add(responses.GET, 'https://twitter.com/', status=201)
    rsps.add(responses.GET, 'https://twitter.com/', status=403, adding_headers = {
        'set-cookie':str_cookie})

#     print (get_status('https://twitter.com/'))
    print(get_csrf('https://twitter.com/'))
