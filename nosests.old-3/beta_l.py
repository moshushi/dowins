import requests
import httpretty
import dowins


with open('cookie_string.txt', 'r') as f:
    str_cookie = f.readline()

# r = requests.get('http://twitter.com/')
r = requests.get('http://instagram.com/')
print (r.status_code)
print ('***')
print (r.cookies)
# r = requests.head('http://twitter.com/')
# print (r.head)
# print (r.cookies['csrftoken'])
print ('---')
print (r.headers['set-cookie'])
print (r.cookies['csrftoken'])
print ('===')

@httpretty.activate
def test_api():
    httpretty.register_uri(httpretty.GET, "http://instagram.com/",
                           body="Heeee",
                           adding_headers={
                               'X-foo': 'bar',
                               'set-cookie': str_cookie
                           })

    response = requests.get("http://instagram.com/")
    print (response.text)
    print (response.cookies)
    print (response.headers)
    print ("---------")
    print (response.headers['set-cookie'])
#     print (response.cookies['csrftoken'])

# test_api()


@httpretty.activate
def test_api_2():
    httpretty.register_uri(httpretty.GET, "https://instagram.com/",
                           body="Heeee",
                           adding_headers={
                               'X-foo': 'bar',
                               'set-cookie': str_cookie
                           })
#     print (dowins.PostsExtractor.get_csrf_and_cookie_string())
    resp = requests.get("https://instagram.com/")
    print (resp.cookies['csrftoken'])


test_api()
print ("-=-=-=-=-=-")
# test_api_2()
