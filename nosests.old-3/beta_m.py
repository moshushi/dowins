import requests
import requests_mock

with open('cookie_string.txt', 'r') as f:
    str_cookie = f.readline()

@requests_mock.Mocker()
def test_function(m):
    m.get('https://test.com', text='resp', cookies={'set-cookie': str_cookie})
    return requests.get('https://test.com')

print(test_function().text)
print(test_function().cookies)
