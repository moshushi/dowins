import requests
import requests.utils
import http.cookiejar
import json
import requests_mock
import dowins


with open('new_cookie_string_jar.txt', 'r') as f:
    my_cookies_str = f.readline()
    my_cookies_dic = json.loads(my_cookies_str)
#     my_cookies_jar = requests.utils.cookiejar_from_dict(my_cookies_dic)

with open('new_cookie_string.txt', 'r') as s:
    str_cookie = s.readline()

def test_Q():
    with requests_mock.mock() as m:
        m.get('https://www.instagram.com', status_code=201,
            cookies={'csrftoken': my_cookies_dic},
            headers={'set-cookie': str_cookie}
            )

        assert dowins.PostsExtractor.get_csrf_and_cookie_string()[0] == my_cookies_dic
