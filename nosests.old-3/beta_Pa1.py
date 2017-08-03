import requests
import httpretty
import dowins


with open('cookie_string.txt', 'r') as f:
    str_cookie = f.readline()


@httpretty.activate
def test_api_2():
    httpretty.register_uri(httpretty.HEAD, "https://instagram.com/",
                           body="Heeee",
                           adding_headers={
                               'X-foo': 'bar',
                               'set-cookie': str_cookie
                           })
#     print (dowins.PostsExtractor.get_csrf_and_cookie_string())
    resp = requests.head("https://instagram.com/")
#     print (resp.cookies['csrftoken'])
    print (resp.text)



test_api_2()
print ("-=-=-=-=-=-")
# test_api_2()
