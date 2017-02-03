# -*- encoding: utf-8 -*-
"""
Script downloads and wrap foto and metainformation from INSTARGAM
Prototype
"""

import requests
import json
import arrow
#### http://crsmithdev.com/arrow/
from bs4 import BeautifulSoup
from ast import literal_eval

BASE_URL = u'https://www.instagram.com/'
BASE_SUFFIX_POST = u'p/'
NAME_ACCOUNT = "abc"
# NAME_ACCOUNT = "polovinkinandrey"
# NAME_ACCOUNT = "NBA"
NAME_ACCOUNT = "frenzytechnix"

TEST_SOME_DICT = {u'code': u'BQA3H09gCPm', u'dimensions': {u'width': 1080, u'height': 1350}, u'caption': u'Kiev TV tower.\n#\u043a\u0438\u0457\u0432 #\u043a\u0438\u0435\u0432 #kyiv #kiev #tvtower #televisiontower', u'comments_disabled': False, u'comments': {u'count': 0}, u'date': 1486047613, u'likes': {u'count': 24}, u'owner': {u'id': u'43237241'}, u'thumbnail_src': u'https://scontent-fra3-1.cdninstagram.com/t51.2885-15/s640x640/sh0.08/e35/c0.135.1080.1080/16465279_1351964604878196_3035221119993905152_n.jpg?ig_cache_key=MTQ0MTM5NDMxMTIxOTM4OTQxNA%3D%3D.2.c', u'is_video': False, u'id': u'1441394311219389414', u'display_src': u'https://scontent-fra3-1.cdninstagram.com/t51.2885-15/e35/16465279_1351964604878196_3035221119993905152_n.jpg?ig_cache_key=MTQ0MTM5NDMxMTIxOTM4OTQxNA%3D%3D.2'}

def get_html(url):
    """
    Get html from website
    """
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError as e:
        print "Site %s isn't accessibility" % BASE_URL
    except requests.exceptions.ReadTimeout as e:
        print "Error: Read Timeout"
    except requests.exceptions.HTTPError as e:
        print "Get an HTTPError:", e.message
#     return response.text
#     return response.text
    return response.text

def get_unit_from_html(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')

    list_of_script = soup.findAll(name="script", type='text/javascript')
    for i in list_of_script:
        if '_sharedData' in i.text:
            cutter =  i.text.find('=')
#             print i.text[cutter + 2: -1]
            return i.text[cutter + 2: -1]

def get_dict_from_unit(unit_string):
    obj = json.loads(unit_string)
    data_li = obj[u'entry_data'][u'ProfilePage'][0][u'user'][u'media'][u'nodes']
#     print data_li
    print type(data_li)
    print len(data_li)
    print data_li[1]
    for i in data_li:
        print i
        print i[u'code']
        print '----'
#         print i.keys()
        for key in i.keys():
            print key

        print '======'
        print i
#         if u'caption' in i.keys():
#             print i[u'caption'].encode('utf-8')
            ## for testing
        print '----'
#         print type(i[u'date'])
        j = {u'date':arrow.get(i[u'date']).format('YYYY-MM-DD'), u'url':BASE_URL + BASE_SUFFIX_POST + i[u'code']}
        print j
        if u'caption' in i.keys():
#             print i[u'caption'].encode('utf-8')
            ## for testing
            j[u'text'] = i[u'caption']
        print '*****'
        print j
##### u'code' - is number of page on pose

def remake(some_dict):
    """Recreate dictionary for output
    Function get dictonary from parsing page select and rename key with their values
    """
    for key in some_dict:
        pass
#         print key
#     print some_dict[u'display_src']
    print some_dict[u'comments']

    print some_dict
    print len(some_dict)
    # remove some pair from dictionary
    list_item_for_remove = [u'owner',u'id', u'dimensions', u'comments_disabled',
                            u'thumbnail_src', u'is_video']
    for item in list_item_for_remove:
        some_dict.pop(item, None)

    # date in pretty format
    some_dict[u'date'] = arrow.get(some_dict[u'date']).format('YYYY-MM-DD')

    # add url from key:code
    some_dict[u'url'] = BASE_URL + BASE_SUFFIX_POST + some_dict.pop(u'code')

    # caption:text
    some_dict[u'text'] = some_dict.pop(u'caption')
#     print some_dict[u'text'].encode('utf-8')  # test print

    # Image source url
    s = some_dict.pop(u'display_src')
    sep = u'.jpg'
    rest = s.split(u'.jpg')[0] + u'.jpg'

    some_dict[u'img-source'] = rest

    # like's
    some_dict[u'likes'] = some_dict[u'likes'][u'count']

    print some_dict

    print len(some_dict)

def parse(uni_row):
#     print string
#     print dict_row["media"]
    pass

def process_page(url):
    html = get_html(url)
    unit_row = get_unit_from_html(html)
    get_dict_from_unit(unit_row)
#     data = parse(dict_row)
#     print '===='
#     print dagajs.decode('utf-8').encode('cp1251')
#     print data

def main():
#     process_page(BASE_URL + NAME_ACCOUNT)
    remake(TEST_SOME_DICT)


if __name__ == '__main__':
    main()
