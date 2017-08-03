import requests
import requests.utils
import http.cookiejar
import json
import requests_mock

r = requests.get('https://twitter.com')
print (r.status_code)
print (r.cookies)
# print (r.header) ### !not correct
print ('----')


with open('new_cookie_string_jar.txt', 'r') as f:
    my_cookies_str = f.readline()
    my_cookies_dic = json.loads(my_cookies_str)
    my_cookies_jar = requests.utils.cookiejar_from_dict(my_cookies_dic)

with open('new_cookie_string.txt', 'r') as s:
    str_cookie = s.readline()

with requests_mock.mock() as m:
    m.get('https://twitter.com', status_code=201, cookies={'csrftoken': my_cookies_dic})
    r = requests.get('https://twitter.com')
    print (r.status_code)
    print (r.cookies)
    print ('~~~~')
    print (r.cookies['csrftoken'])


# httpretty.enable()
# httpretty.register_uri(httpretty.GET, "https://twitter.com/",
#                        body="TEST", status=201, cookies=my_cookies_jar,
#                        adding_headers={
#                            'set-cookie': str_cookie,
#                            'Host': 'twitter.com'
#                        })
#
# r = requests.get('https://twitter.com')
# print (r.status_code)
# print (r.cookies)
# print (r.headers)
# # print (type(r.cookies))
# # httpretty.disable()
#
# # print("~~~~~")
# # print(my_cookies_jar)
# # print(type(my_cookies_jar))
# # print("~~~~~")
# # print(r.headers)
#
# #                        cookies = my_cookies_jar,
