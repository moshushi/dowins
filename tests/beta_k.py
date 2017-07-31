import responses
import requests


def test_my_api():
    with responses.RequestsMock() as rsps:
        rsps.add(responses.GET, 'https://twitter.com/api/1/foobar',
                 body='{}', status=200,
                 content_type='application/json')
        resp = requests.get('https://twitter.com/api/1/foobar')
        print (resp.status_code)
        print (resp.cookies)

test_my_api()
