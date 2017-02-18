# -*- encoding: utf-8 -*-
"""
with correct post.query
"""

import requests
import logging
import json
import time

NAME_URL = 'https://instagram.com/sa.ny.aa/?__a=1'


def start_logging():
    """
    Function for starting http logging
    """
    try:
        import http.client as http_client
    except ImportError:
        # Python 2
        import httplib as http_client
    http_client.HTTPConnection.debuglevel = 1


def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in
    this function because it is programmed to be pretty
    printed and may differ from the actual request.
    """
    print('{}\n{}\n{}\n\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))


def show_request_headers(response):
    """
    Show request headers, what we send to server
    """
    return response.request.headers


def pretty_print_result(string):
    """
    Pretty view result
    """
    obj = json.loads(string)
    print json.dumps(obj, indent=4, sort_keys=True)


def get_csrf_and_cookie_string(response):
    """
    get CSRF-Token and cookie_string from response
    """
    return response.cookies['csrftoken'], response.headers['set-cookie']


def get_user_id(response):
    """
    get user_id from json-string response-object
    """
    return json.loads(response.text)['user']['id']


def get_cursor(response):
    """
    get cursor from json-string response-object
    """
    return json.loads(response.text)['user']['media']['page_info']['end_cursor']


def get_count_row(response):
    """
    get all sum of post for downloads
    """
    return str(json.loads(response.text)['user']['media']['count'])


def get_username(response):
    """
    get username from response
    """
    return json.loads(response.text)['user']['username']


def has_next_page(response):
    """
    has next page from json-string response-object
    """
    return json.loads(response.text)['user']['media']['page_info']['has_next_page']


def make_headers(token, cookie, username):
    """
    make correct headers
    """
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflare, br',
        'accept-language': 'en-US,en;q=0.8',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': cookie,
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/' + username +'/',
        'pragma': 'no-cache',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/56.0.2924.87 Safari/537.36',
        'x-csrftoken': token,
        'x-instagram-ajax': '1',
        'x-requested-with': 'XMLHttpRequest'
    }
    return headers


def make_post_data(user_id, cursor, counter):
    """
    Make correct dictonary query for post_data
    """
    dict_post = {'q': "ig_user(" + user_id + ") { media.after(" +
                 cursor + ", " + counter + ") {" +
    "nodes {" +
    "  caption," +
    "  code," +
    "  comments {" +
    "    count" +
    "  }," +
    "  date," +
    "  display_src," +
    "  is_video," +
    "  likes {" +
    "    count" +
    "  }," +
    "  video_views" +
    "}," +
    "page_info" +
    "}" +
    " }"
                 }
    dict_post.update({'ref': 'users::show'})
    return dict_post


def get_post_resp():
    """
    Make post request and get
    """
    with requests.Session() as s:
        a = s.get(NAME_URL)
        csrf_token, cookie = get_csrf_and_cookie_string(a)
        username = get_username(a)
        head = make_headers(csrf_token, cookie, username)
        s.headers.update(head)
        user_id = get_user_id(a)
        cursor = get_cursor(a)
        counter = get_count_row(a)
        counter = '2'
        post_data = make_post_data(user_id, cursor, counter)
        p = s.post('https://www.instagram.com/query/', data=post_data)
        print p.status_code
#         print p.text
        return p.text
    pass


def main():
    print get_post_resp()
    pass

def main_old():
#     start_logging()
            status_semaphor = 100
            i = 0
            while status_semaphor != 200 and i<= 10:
                i += 1
                print i
                post_data = make_post_data(user_id, cursor, counter)
                p = s.post('https://www.instagram.com/query/', data=post_data)
                print p.status_code
                status_semaphor = int(p.status_code)
                time.sleep(5)


if __name__ == '__main__':
    main()
