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


BASE_URL = "https://www.instagram.com/"


class PostsExtractor():
    """
    Extracts post for given username
    """

    def __init__(self, username):
        self.username = username
        self.csrf_token, self.cookie_string = PostsExtractor.get_csrf_and_cookie_string()


    @staticmethod
    def get_csrf_and_cookie_string():
        resp = requests.head(BASE_URL)
        return resp.cookies['csrftoken'], resp.headers['set-cookie']

if __name__ == '__main__':
    acc = 'polovinkinandrey'
    postextract = PostsExtractor(acc)
    print(postextract.username)
    print(postextract.csrf_token)
    print(postextract.cookie_string)


