# -*- encoding: utf-8 -*-
"""
Script downloads and wrap foto and metainformation from INSTARGAM
Prototype
"""

import requests, json, arrow
#### http://crsmithdev.com/arrow/
from bs4 import BeautifulSoup
from ast import literal_eval

BASE_URL = u'https://www.instagram.com/'
BASE_SUFFIX_POST = u'p/'
NAME_ACCOUNT = "abc"
# NAME_ACCOUNT = "polovinkinandrey"
# NAME_ACCOUNT = "NBA"
NAME_ACCOUNT = "frenzytechnix"

# TEST_SOME_DICT = {u'code': u'BQA3H09gCPm', u'dimensions': {u'width': 1080, u'height': 1350}, u'caption': u'Kiev TV tower.\n#\u043a\u0438\u0457\u0432 #\u043a\u0438\u0435\u0432 #kyiv #kiev #tvtower #televisiontower', u'comments_disabled': False, u'comments': {u'count': 0}, u'date': 1486047613, u'likes': {u'count': 24}, u'owner': {u'id': u'43237241'}, u'thumbnail_src': u'https://scontent-fra3-1.cdninstagram.com/t51.2885-15/s640x640/sh0.08/e35/c0.135.1080.1080/16465279_1351964604878196_3035221119993905152_n.jpg?ig_cache_key=MTQ0MTM5NDMxMTIxOTM4OTQxNA%3D%3D.2.c', u'is_video': False, u'id': u'1441394311219389414', u'display_src': u'https://scontent-fra3-1.cdninstagram.com/t51.2885-15/e35/16465279_1351964604878196_3035221119993905152_n.jpg?ig_cache_key=MTQ0MTM5NDMxMTIxOTM4OTQxNA%3D%3D.2'}
TEST_SOME_DICT = {u'code': u'BOPfznag78S', u'dimensions': {u'width': 1080, u'height': 1080}, u'caption': u'\u0418\u0433\u0440\u0430\u0435\u043c \u0441 \u041a\u043e\u0441\u0442\u0435\u0439 \u0432 \u043d\u0430\u0441\u0442\u043e\u043b\u044c\u043d\u0443\u044e \u0440\u043e\u043b\u0435\u0432\u043a\u0443 Hero Kids. \u0413\u041c \u0438\u0437 \u043c\u0435\u043d\u044f \u0442\u0430\u043a \u0441\u0435\u0431\u0435, \u0434\u0430 \u0435\u0449\u0435 \u0438 \u0441 \u043a\u0443\u0431\u0438\u043a\u0430\u043c\u0438 \u041a\u043e\u0441\u0442\u0435 \u043d\u0435 \u0432\u0435\u0437\u043b\u043e, \u043d\u043e \u0442\u0435\u043c \u043d\u0435 \u043c\u0435\u043d\u0435\u0435 \u0434\u0435\u0442\u0438-\u043f\u0440\u0438\u043a\u043b\u044e\u0447\u0435\u043d\u0446\u044b \u0433\u0435\u0440\u043e\u0438\u0447\u0435\u0441\u043a\u0438 \u043f\u0440\u0435\u0432\u043e\u0437\u043c\u043e\u0433\u043b\u0438 \u043a\u0440\u044b\u0441\u0438\u043d\u043e\u0433\u043e \u043a\u043e\u0440\u043e\u043b\u044f ;)\n#herokids #roleplay #boardgame #pnprpg', u'comments_disabled': False, u'comments': {u'count': 1}, u'date': 1482243738, u'likes': {u'count': 22}, u'owner': {u'id': u'43237241'}, u'thumbnail_src': u'https://scontent-bru2-1.cdninstagram.com/t51.2885-15/s640x640/sh0.08/e35/15338486_1551801051502691_5653328674196291584_n.jpg?ig_cache_key=MTQwOTQ4NTA5NDg0NjE4NTIzNA%3D%3D.2', u'is_video': False, u'id': u'1409485094846185234', u'display_src': u'https://scontent-bru2-1.cdninstagram.com/t51.2885-15/e35/15338486_1551801051502691_5653328674196291584_n.jpg?ig_cache_key=MTQwOTQ4NTA5NDg0NjE4NTIzNA%3D%3D.2'}

URL_ONE_PAGE = u'https://www.instagram.com/p/BOPfznag78S/'


def get_html(url):
    """ Get html from website
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


def get_unit_rawdata_from_html(html_doc):
    """Parse data from Title page for get raw metainformation
    """
    soup = BeautifulSoup(html_doc, 'html.parser')

    list_of_script = soup.findAll(name="script", type='text/javascript')
    for i in list_of_script:
        if '_sharedData' in i.text:
            cutter =  i.text.find('=')
#             print i.text[cutter + 2: -1]
            return i.text[cutter + 2: -1]


def get_dict_from_unit(unit_string):
    """Get raw dictionary from raw data
    """
    obj = json.loads(unit_string)
    data_li = obj[u'entry_data'][u'ProfilePage'][0][u'user'][u'media'][u'nodes']
    return data_li


def change_obg_in_data(data_li):
    """Change dictionary in list on true dictionary
    """
    new_list = [ remake(i) for i in data_li ]
#     print new_list
#     print '*****'
#     for i in new_list:
#         print i
#     print '*****'
    return new_list

#             print i[u'caption'].encode('utf-8')

def remake(some_dict):
    """Modify dictionary for output in correct format for specification
    Function get dictonary from parsing page select and rename key with their values
    Return non-true dictionary
    """
    for key in some_dict:
        pass
#         print key
#     print some_dict[u'comments']

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
    if u'caption' in some_dict:
        some_dict[u'text'] = some_dict.pop(u'caption')
    else:
        some_dict[u'text'] = ""
#     print some_dict[u'text'].encode('utf-8')  # test print

    # Image source url
    s = some_dict.pop(u'display_src')
    sep = u'.jpg'
    rest = s.split(u'.jpg')[0] + u'.jpg'

    some_dict[u'img-source'] = rest

    # like's
    some_dict[u'likes'] = some_dict[u'likes'][u'count']

    # Count comments
#     some_dict[u'count-comments'] = some_dict[u'comments'][u'count']
    # If have comments run function get_comments()
    if some_dict[u'comments'][u'count'] > 0:
        pass

#     print some_dict
    return some_dict

#     print len(some_dict)

def parse(uni_row):
    pass

def process_unit_page(url):
    """Processing title list in instagram account
    """
    html = get_html(url)
    unit_row = get_unit_rawdata_from_html(html)
    data_li = get_dict_from_unit(unit_row)
    print change_obg_in_data(data_li)


def main():
    process_unit_page(BASE_URL + NAME_ACCOUNT)
#     remake(TEST_SOME_DICT)


if __name__ == '__main__':
    main()
