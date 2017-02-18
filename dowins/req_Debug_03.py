# -*- encoding: utf-8 -*-

import requests
import logging
import json

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



def has_next_page(response):
    """
    has next page from json-string response-object
    """
    return json.loads(response.text)['user']['media']['page_info']['has_next_page']


def make_headers(token):
    """
    make correct headers
    """
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflare, br',
        'accept-language': 'en-US,en;q=0.8',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/sa.ny.aa/',
        'pragma': 'no-cache',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/56.0.2924.87 Safari/537.36',
        'x-csrftoken': token,
        'x-instagram-ajax': '1',
        'x-requested-with': 'XMLHttpRequest'
    }
    return headers

def main():
#     start_logging()
        with requests.Session() as s:
            a = s.get(NAME_URL)
            print a.cookies
            csrf_token = get_csrf_and_cookie_string(a)[0]
#             print csrf_token
            head = make_headers(csrf_token)
            print head
            s.headers.update(head)
            a = s.get(NAME_URL)

            print a.status_code
#             print json.loads(show_request_headers(a))
            print show_request_headers(a)
#             print type(show_request_headers(a))
#             print type(show_request_headers(a)['Accept'])
#             print show_request_headers(a)['Accept']

#             print '----'
#             print a.text

#     a = requests.get(NAME_URL)
#     print get_csrf_and_cookie_string(a)
#     print a.status_code
#     print get_cursor(a)
#     print has_next_page(a)
#     pretty_print_result(a.text)
#     print show_request_headers(a)
    #### loading_page_id $$$$



if __name__ == '__main__':
    main()
