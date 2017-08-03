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


# responses.activate
# def test_get_csrf_and_cookie_string(data_small_p):
#     """
#     Check correct extract csrf and cookie string
#     """
#     responses.add(responses.GET, 'https://www.instagram.com/',
#                   adding_headers = {
#                       "set-cookie:": "csrftoken=ESFxG4twi08sWbQXFQSDeVblZ8I74IfJ; " +
#                       "expires=Mon, 16-Jul-2018 11:18:19 GMT; " +
#                       "Max-Age=31449600; " +
#                       "Path=/; " +
#                       "Secure"
#                   })
#
#     assert dowins.PostsExtractor.get_csrf_and_cookie_string()[0] == "csrftoken=ESFxG4twi08sWbQXFQSDeVblZ8I74IfJ"
#     pass


# def test_user_id(data_small_p):
#     pass
