# -*- encoding: utf-8 -*-
"""
Script downloads and wrap foto and metainformation from INSTARGAM
Prototype
version 0.04
Based on: Instagram-Search-API-Python by TomKDickinson
https://github.com/tomkdickinson/Instagram-Search-API-Python
https://gist.github.com/tomkdickinson/a093d30523dd77ae970f3ffcf26e1344
http://tomkdickinson.co.uk/2016/12/extracting-instagram-data-part-1/
with correct post.query
https://www.instagram.com/smena8m/media/
https://stackoverflow.com/questions/17373886/how-can-i-get-a-users-media-from-instagram-without-authenticating-as-a-user
"""

import requests
import json
from pprint import pprint
# import http.client as http_client
# http_client.HTTPConnection.debuglevel = 1


INSTAGRAM_ROOT = "https://www.instagram.com/"
SUF = "?__a=1"
MEDIA = "/media/?size=L"


class PostsExtractor():
    """
    Extracts post for given username
    """

    def __init__(self, username):
        self.username = username
        self.csrf_token, self.cookie_string = PostsExtractor.get_csrf_and_cookie_string()
        self.counter = None
        self.cursor = None
        self.user_id = None

    @staticmethod
    def get_csrf_and_cookie_string():
        resp = requests.head(INSTAGRAM_ROOT)
        return resp.cookies['csrftoken'], resp.headers['set-cookie']


    def get_headers(self):
        """ Returns a bunch of headers we need to use when querying Instagram
        """
        return {
            "accept": "*/*",
            'accept-encoding': 'gzip, deflare, br',
            'accept-language': 'en-US,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': self.cookie_string,
            'origin': INSTAGRAM_ROOT,
            'referer': INSTAGRAM_ROOT + self.username +'/',
            'pragma': 'no-cache',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/56.0.3029.110 Safari/537.36',
            'x-csrftoken': self.csrf_token,
            'x-instagram-ajax': '1',
            'x-requested-with': 'XMLHttpRequest'
        }


    @staticmethod
    def extract_user_profile(username):
        """
        Maybe we don't need this method
        """
        response = requests.get(INSTAGRAM_ROOT + username + SUF)
        req = json.loads(response.text)

#         pprint(req)

        counter = str(req['user']['media']['count']) #all sum user's post
        cursor = str(req['user']['media']['page_info']['end_cursor'])
        user_id = str(req['user']['id'])

#         print (response.url)
#         print (response.status_code)

#         return req
        return user_id, counter, cursor


    def get_posts_page(self, username, end_cursor=None):
        """
        Get page General Information from username and end_cursor
        !!!! Need end_cursor add for get
        We can use it function or the same function with suffix MEDIA
        """
#         if end_cursor != None:
#             max_id
        payload = {'max_id': end_cursor}
        response = requests.get(INSTAGRAM_ROOT + username + SUF, params=payload)
        req = json.loads(response.text)
        return req


    def extract_posts(self, username):
        """
        Print '1' for every page with post
        """
        req = self.get_posts_page(username)
        print('1')
        info = []
#         info = req['user']['media']
        info.append(req['user']['media'])
        ### need coorect info and function for remake it
        while req['user']['media']['page_info']['has_next_page']:
            req = self.get_posts_page(username, req['user']['media']['page_info']['end_cursor'])
            print('2')
            print(req['user']['media']['page_info']['end_cursor'])
#             info += req['user']['media']
            info.append(req['user']['media'])
            ### need correct info how above

        return info


    def get_posts_page_media(self, username, end_cursor=None):
        """
        Get page General Information with Comments from username and end_cursor
        !!!! Need end_cursor add for get
        We can use it function or the same function without suffix MEDIA
        """
        payload = {'max_id': end_cursor}
        response = requests.get(INSTAGRAM_ROOT + username + MEDIA, params=payload)
        req = json.loads(response.text)
        return req


    def extract_posts_media(self, username):
        """
        Print '1' for every page with post
        Experemental with use MEDIA and max_id
        in construction....
        """
        req = self.get_posts_page(username)
        print('1')
        pprint(req)
        print (type(req))
        print (len(req['items']))
        bal = []
        for i in req['items']:
            print (i['id'])
            bal.append(i['id'])
        print (bal)
        print (max(bal))
        self.cursor = max(bal)


if __name__ == '__main__':
    acc = 'polovinkinandrey'
#     acc = 'sa.ny.aa'
    postextract = PostsExtractor(acc)
    print (postextract.extract_user_profile(acc))

#     print(postextract.extract_user_profile())

#     pprint(postextract.extract_some_information())
#     postextract.extract_posts(acc)
#     print (postextract.users_posts())
