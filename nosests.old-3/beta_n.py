import requests
import requests_mock
import dowins

adapter = requests_mock.Adapter()
session = requests.Session()
session.mount('mock', adapter)

with open('cookie_string.txt', 'r') as f:
    str_cookie = f.readline()

# @requests_mock.Mocker()
# adapter.register_uri('GET', 'mock://instagram.com', text='resp', cookies={'set-cookie': str_cookie})
# requests_mock.mock.get('mock://instagram.com', text='resp', cookies={'set-cookie': str_cookie})
# requests_mock.adapter('GET', 'mock://instagram.com', text='resp', cookies={'set-cookie': str_cookie})
@requests_mock.Mocker()
def test_1(m):
    m.get('https://instagram.com', text='resp', cookies={'set-cookie': str_cookie})
    a = dowins.PostsExtractor.get_csrf_and_cookie_string()
    return a

# print(test_function().text)
# print(test_function().cookies)
# print (a[0])
# print (a[1])

print (test_1()[0])
print (test_1()[1])
