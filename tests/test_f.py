import requests
# from httmock import all_requests, response, HTTMock
import httmock
import dowins

# def test_E():

@httmock.all_requests
def response_content(url, request):
	headers = {'content-type': 'application/json',
	           'Set-Cookie': 'foo=bar;'}
	content = {'message': 'API rate limit exceeded'}
	return httmock.response(403, content, headers, None, 5, request)

with httmock.HTTMock(response_content):
	r = requests.get('https://api.github.com/users/whatever')

print (r.json().get('message'))
print (r.cookies['foo'])



def test_F():
    pass

@httmock.all_requests
def response_content(url, request):
	headers = {'content-type': 'application/json',
	           'Set-Cookie': 'foo=bar;'}
	content = {'message': 'API rate limit exceeded'}
	return httmock.response(403, content, headers, None, 5, request)
