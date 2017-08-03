import requests
# from httmock import all_requests, response, HTTMock
import httmock
import dowins

"""
https://github.com/patrys/httmock
"""

with open('cookie_string.txt', 'r') as f:
    str_cookie = f.readline()

# def test_E():

@httmock.all_requests
def response_content(url, request):
	headers = {'content-type': 'application/json',
	           'Set-Cookie': 'foo=bar;'}
	content = {'message': 'API rate limit exceeded'}
	return httmock.response(403, content, headers, None, 5, request)

with httmock.HTTMock(response_content):
	r = requests.get('https://api.github.com/users/whatever')

# print (r.json().get('message'))
# print (r.cookies['foo'])



def test_F():
    pass

@httmock.all_requests
def response_content(url, request):
	headers = {'content-type': 'application/json',
	           'Set-Cookie': str_cookie}
	content = {'message': 'API rate limit exceeded'}
	return httmock.response(200, content, headers, None, 5, request)

# print (str_cookie)

with httmock.HTTMock(response_content):
	r = requests.get('https://www.instagram.com/')

# print (r)
# print (r.text)
# print (r.cookies)
# print (r.headers)
# # print (r.cookies['csrftoken'])
# print (r.headers)
# print (r.status_code)
# print (r.headers)
with httmock.HTTMock(response_content):
    pass
#     print (dowins.PostsExtractor.get_csrf_and_cookie_string())
#     print (dowins.PostsExtractor.get_csrf_and_cookie_string()[1])
