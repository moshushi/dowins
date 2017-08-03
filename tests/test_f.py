import requests
import requests_mock
import dowins



def test_Q(my_cookies_dic, str_cookie):
    with requests_mock.mock() as m:
        m.get('https://www.instagram.com', status_code=201,
            cookies={'csrftoken': my_cookies_dic},
            headers={'set-cookie': str_cookie}
            )

        assert dowins.PostsExtractor.get_csrf_and_cookie_string()[0] == my_cookies_dic
