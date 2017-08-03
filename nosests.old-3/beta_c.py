import dowins
import responses
import requests

@responses.activate
def test_R():
    responses.add(responses.GET, 'http://invalid/cookies',
                    adding_headers = {
                        "set-cookie": "foo=bar; " +
                        "domain=.invalid; " +
                        "path=/; " +
                        ""
                    })

session = requests.Session()
session.get('http://invalid/cookies')

assert dict(response.cookies) == {'foo': 'bar', 'path': '/', 'domain': '.invalid'}
