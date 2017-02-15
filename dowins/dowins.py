# -*- encoding: utf-8 -*-
"""
Script downloads and wrap foto and metainformation from INSTARGAM
Prototype
version 0.02
"""

import requests, json, arrow

ROOT_URL = u'https://www.instagram.com/'
SUF = u'?__a=1'
NAME_ACCOUNT = u'sa.ny.aa'


def get_csrf_and_cookie_string():
    """get csrf-token and cookie string when first connect to Instagram
    """
    try:
        response = requests.get(ROOT_URL)
    except requests.exceptions.ConnectionError as e:
        print "Site %s isn't accessibility" % BASE_URL
    except requests.exceptions.ReadTimeout as e:
        print "Error: Read Timeout"
    except requests.exceptions.HTTPError as e:
        print "Get an HTTPError:", e.message
    return response.cookies['csrftoken'], response.headers['set-cookie']


def simple_json_get_page(url):
    """get information from userpage without pagenation
    """
    response = requests.get(url+SUF)
    print response.cookies['csrftoken']
    print response.text
    return response.text


def main():
    csrftoken, cookie = get_csrf_and_cookie_string()
    print csrftoken
    simple_json_get_page(ROOT_URL + NAME_ACCOUNT)
    pass


if __name__ == '__main__':
    main()

