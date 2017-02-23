# -*- encoding: utf-8 -*-
"""
Script downloads and wrap foto and metainformation from INSTARGAM
Prototype
version 0.02
Based on: Instagram-Search-API-Python by TomKDickinson
https://github.com/tomkdickinson/Instagram-Search-API-Python
http://tomkdickinson.co.uk/2016/12/extracting-instagram-data-part-1/
"""

import requests, json, arrow

ROOT_URL = u'https://www.instagram.com/'
QUERY_URL = u'https://www.instagram.com/query/'
SUF = u'?__a=1'
NAME_ACCOUNT = u'sa.ny.aa'



def get_csrf_and_cookie_string():
    """
    For first connect and return CSRF Token and cookies for next request
    """
    r = requests.head(ROOT_URL)
    print r.status_code
#     print r.cookies['csrftoken']
#     print r.headers['set-cookie']
    return r.cookies['csrftoken'], r.headers['set-cookie']


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


def get_user_info(name, headers):
    r = requests.get(ROOT_URL+name+SUF, headers)
#     print r.text
# something wrong!
#     print r.cookies['csrftoken']
#     print r.text['user']

    ad = json.loads(r.text)
#     print json.dumps(ad, indent=4, sort_keys=True)
#     print ad['user']
    user_id = ad['user']['id']
    has_next_page = ad['user']['media']['page_info']['has_next_page']
    end_cursor = ad['user']['media']['page_info']['end_cursor']
#     print ad['page_info']
    return user_id, end_cursor

def some_post(user_id, end_cursor, headers):
    """
    try to post
    """
    post_data = {'q': "ig_user(%s) " % (user_id) +
                 "{media.after(" + end_cursor + ", 12){" +
                "  count," +
                "  nodes {" +
                "    id," +
                "    is_verified," +
                "    followed_by_viewer," +
                "    requested_by_viewer," +
                "    full_name," +
                "    profile_pic_url," +
                "    username" +
                "  }," +
                "  page_info {" +
                "    end_cursor," +
                "    has_next_page" +
                "  }" +
                "}" +
                " }",
                 'ref': "users::show"
                }

#     r = requests.post(QUERY_URL, data=post_data, headers=headers)
#     r = requests.post(QUERY_URL, data=json.dumps(post_data), headers=headers)
    r = requests.post(QUERY_URL, json=post_data, headers=headers)
    print '#####'
    print post_data
#     print end_cursor
    print r.status_code
    print r.history
#     print r.text
#     print r.headers['Set-Cookie']
    pass

def process_page(string):
    """
    Pretty view result
    """
    obj = json.loads(string)
    print json.dumps(obj, indent=4, sort_keys=True)

def main():
# We need a CSRF token, so we query Instagram first
    token, cookie = get_csrf_and_cookie_string()
#     print "---"
#     print token
#     print cookie
#     print "-----"
    h = get_headers(token, cookie)
#     print h
#     user_id, cursor = get_user_info(NAME_ACCOUNT, h)
    user_id, cursor = get_user_info(NAME_ACCOUNT, h)
    print user_id
    print cursor
    some_post(user_id, cursor, h)
#     some_post(user_id, cursor, h)


if __name__ == '__main__':
    main()
