# import pytest
import dowins
import responses

responses.activate
def test_user_id(data_small_p):
    """
    Check correct extract user_id and count posts
    """
    responses.add(responses.GET, 'https://www.instagram.com/polovinkinandrey/?__a=1',
                  body = data_small_p, status = 200)

    assert dowins.PostsExtractor.extract_user_profile('polovinkinandrey')[0] == str(1577167408)
    assert dowins.PostsExtractor.extract_user_profile('polovinkinandrey')[1] == str(6)

def test_user_id(data_small_p):
    pass
