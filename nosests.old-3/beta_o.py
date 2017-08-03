import requests
import requests_mock
import dowins

with open('cookie_string.txt', 'r') as f:
    str_cookie = f.readline()


with requests_mock.mock() as m:
    m.head('https://instagram.com/', text='resp', cookies={'set-cookie': str_cookie})
    r = requests.head('https://instagram.com')
    print(r.text)
    print(r.cookies)
    a = dowins.PostsExtractor.get_csrf_and_cookie_string()
    print(a[0])

#     resp = requests.head('https://instagram.com')
#     resp = m.head('https://instagram.com')
#     a = resp.cookies['csrftoken'], resp.headers['set-cookie']
#
# #     a = dowins.PostsExtractor.get_csrf_and_cookie_string()
#     print(a[0])


