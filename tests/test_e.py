import requests
import requests_mock
import dowins

def test_A():
    with requests_mock.Mocker() as m:
        m.get('http://test.com', text='resp')
        assert requests.get('http://test.com').text == 'resp'


def test_B(data_small_p):
    with requests_mock.Mocker() as m:
        m.get('https://www.instagram.com/polovinkinandrey/?__a=1',
            text = data_small_p)

        assert dowins.PostsExtractor.extract_user_profile('polovinkinandrey')[0] == str(1577167408)
        assert dowins.PostsExtractor.extract_user_profile('polovinkinandrey')[1] == str(6)


# def test_C():
#     with requests_mock.Mocker() as m:
#         m.get('https://www.instagram.com/', cookies={"csrf":"ESFxG4"})
#         m.get('https://www.instagram.com/, real_http=True')
#         assert dowins.PostsExtractor.get_csrf_and_cookie_string()[0] == "AEB"
#     return(requests.get('https://instgagram.com').status_code)
#         baar = dowins.PostsExtractor.get_csrf_and_cookie_string()
#     return baar
#     return(dowins.PostsExtractor.get_csrf_and_cookie_string())
#     return 5

def test_D():
#     requests_mock.adapter.register_uri('GET', 'mock://test.com/7', cookies={'foo': 'bar'})
#     resp = session.get('mock://test.com/7')
#     return resp.cookies['foo']
#     return requests_mock.adapter

if __name__ == '__main__':
    a = test_D()
    print(a)
