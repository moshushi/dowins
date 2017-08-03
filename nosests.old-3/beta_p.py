import requests
import requests_mock
import dowins
from requests_mock.contrib import fixture

with open('cookie_string.txt', 'r') as f:
    str_cookie = f.readline()

@requests_mock.Mocker()
requests_mock = useFixture(fixture.Fixture())
requests_mock.register_uri('HEAD','https://instagram.com', text='resp', cookies={'set-cookie':str_cookie})
r = requests.head('https://instagram.com')

print (r.cookies)

