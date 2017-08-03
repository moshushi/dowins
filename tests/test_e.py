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
