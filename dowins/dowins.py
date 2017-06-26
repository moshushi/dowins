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
"""

import requests
import json
# import http.client as http_client
# http_client.HTTPConnection.debuglevel = 1


INSTAGRAM_ROOT = "https://www.instagram.com/"


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
            'Chrome/56.0.2924.87 Safari/537.36',
            'x-csrftoken': self.csrf_token,
            'x-instagram-ajax': '1',
            'x-requested-with': 'XMLHttpRequest'
        }


    def extract_user_profile(self, user_id=None):
        if user_id is None:
            user_id = json.loads(requests.get(INSTAGRAM_ROOT + self.username + "?__a=1").text)['user']['id']
        return user_id


#     @staticmethod
    def get_userdata_params(self):
        """
        Need correct query for get json 1 file all data
        """
        if self.counter == None:
            get_userdata_params(self, self.user_id)


        dict_post = {'q': "ig_user(" + self.user_id + ") { media.after(" +
                        self.cursor + ", " + str(self.counter) + ") {" +
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
        pass


    def extract_some_information(self, user_id=None):
        if user_id is None:
            user_id = self.extract_user_profile()
        req = json.loads(requests.get(INSTAGRAM_ROOT + self.username + "?__a=1").text)
        self.counter = req['user']['media']['count'] #all sum user's post
        self.cursor = req['user']['media']['page_info']['end_cursor']
        self.user_id = str(user_id)
#         req = requests.get(INSTAGRAM_ROOT + self.username + "?__a=1").text
        return req


    def users_posts(self):
        headers = self.get_headers()
        post_data = self.get_userdata_params()
        req = requests.post(INSTAGRAM_ROOT + "query/", data = post_data, headers = headers)
#         return json.loads(req.text)
        return len(req.text)
        pass
        pass
        pass



if __name__ == '__main__':
    acc = 'polovinkinandrey'
    acc = 'abc'
    postextract = PostsExtractor(acc)
    print(postextract.extract_user_profile())
    print(postextract.extract_some_information())
    print(postextract.counter)
    print(postextract.cursor)
    print('----')
    print(postextract.get_userdata_params())
    print('====')
    print(postextract.users_posts())

#     print postextract.get_headers()
#     print(postextract.username)
#     print(postextract.csrf_token)
#     print(postextract.cookie_string)
#     print(postextract.text)


