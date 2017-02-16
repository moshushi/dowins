# -*- encoding: utf-8 -*-
"""
Script downloads and wrap foto and metainformation from INSTARGAM
Prototype
version 0.02
Based on: Instagram-Search-API-Python by TomKDickinson
https://github.com/tomkdickinson/Instagram-Search-API-Python
"""

import requests, json, arrow

ROOT_URL = u'https://www.instagram.com/'
SUF = u'?__a=1'
NAME_ACCOUNT = u'sa.ny.aa'
# NAME_ACCOUNT = u'abc'


def get_csrf_and_cookie_string(session):
    """get csrf-token and cookie string when first connect to Instagram
    """
    try:
        response = session.get(ROOT_URL)
    except requests.exceptions.ConnectionError as e:
        print "Site %s isn't accessibility" % BASE_URL
    except requests.exceptions.ReadTimeout as e:
        print "Error: Read Timeout"
    except requests.exceptions.HTTPError as e:
        print "Get an HTTPError:", e.message
#     print response.headers
#     print "-----"
#     print requests.head
#     print "-----"
    return response.cookies['csrftoken'], response.headers['set-cookie']


def get_headers(token=None, cookie=None):
    """Make useable headers for extractor
    """
    return {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-GB,en;q=0.8,en-US;q=0.6",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "cookie": cookie,
        "origin": "https://www.instagram.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/56.0.2924.87 Safari/537.36",
        "x-csrftoken": token,
        "x-instagram-ajax": "1",
        "X-Requested-With": "XMLHttpRequest"
    }


def simple_json_get_page(url, session):
    """get information from userpage without pagenation
    """
    response = session.get(url+SUF)
#     print response.cookies['csrftoken']
#     print response.text
    print json.dumps(response.text, indent=4).encode('utf8')
#     print response.headers
    return response.text


def simple_post(url, session):
    """get custom information
    """
    data = {
        'q':
            " page_info {" +
            " end_cursor," +
            " has_next_page" +
            " }",
        'ref': 'user::show',
    }
    resp = session.get(url+SUF)
#     print resp.cookies['csrftoken']
    print json.dumps(resp.text, indent=4)
    return resp.text

    pass



def main():
    s = requests.session()
    start_head = get_headers()
    csrftoken, cookie = get_csrf_and_cookie_string(s)
#     print csrftoken
#     head = get_headers(csrftoken, cookie)
#     print head
    simple_json_get_page(ROOT_URL + NAME_ACCOUNT, s)
#     simple_json_get_page(ROOT_URL + NAME_ACCOUNT, s)
    simple_post(ROOT_URL + NAME_ACCOUNT, s)
    simple_post(ROOT_URL + NAME_ACCOUNT, s)
    simple_post(ROOT_URL + NAME_ACCOUNT, s)
    simple_post(ROOT_URL + NAME_ACCOUNT, s)
    pass


if __name__ == '__main__':
    main()

