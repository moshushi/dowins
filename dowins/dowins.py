# -*- encoding: utf-8 -*-
"""
Script downloads and wrap foto and metainformation from INSTARGAM
Prototype
"""

import requests, json, arrow
# import io
#### http://crsmithdev.com/arrow/
from bs4 import BeautifulSoup
from ast import literal_eval

BASE_URL = u'https://www.instagram.com/'
BASE_SUFFIX_POST = u'p/'
# NAME_ACCOUNT = u"abc"
# NAME_ACCOUNT = u"polovinkinandrey"
# NAME_ACCOUNT = u"NBA"
NAME_ACCOUNT = u"frenzytechnix"

# TEST_SOME_DICT = {u'code': u'BQA3H09gCPm', u'dimensions': {u'width': 1080, u'height': 1350}, u'caption': u'Kiev TV tower.\n#\u043a\u0438\u0457\u0432 #\u043a\u0438\u0435\u0432 #kyiv #kiev #tvtower #televisiontower', u'comments_disabled': False, u'comments': {u'count': 0}, u'date': 1486047613, u'likes': {u'count': 24}, u'owner': {u'id': u'43237241'}, u'thumbnail_src': u'https://scontent-fra3-1.cdninstagram.com/t51.2885-15/s640x640/sh0.08/e35/c0.135.1080.1080/16465279_1351964604878196_3035221119993905152_n.jpg?ig_cache_key=MTQ0MTM5NDMxMTIxOTM4OTQxNA%3D%3D.2.c', u'is_video': False, u'id': u'1441394311219389414', u'display_src': u'https://scontent-fra3-1.cdninstagram.com/t51.2885-15/e35/16465279_1351964604878196_3035221119993905152_n.jpg?ig_cache_key=MTQ0MTM5NDMxMTIxOTM4OTQxNA%3D%3D.2'}
TEST_SOME_DICT = {u'code': u'BOPfznag78S', u'dimensions': {u'width': 1080, u'height': 1080}, u'caption': u'\u0418\u0433\u0440\u0430\u0435\u043c \u0441 \u041a\u043e\u0441\u0442\u0435\u0439 \u0432 \u043d\u0430\u0441\u0442\u043e\u043b\u044c\u043d\u0443\u044e \u0440\u043e\u043b\u0435\u0432\u043a\u0443 Hero Kids. \u0413\u041c \u0438\u0437 \u043c\u0435\u043d\u044f \u0442\u0430\u043a \u0441\u0435\u0431\u0435, \u0434\u0430 \u0435\u0449\u0435 \u0438 \u0441 \u043a\u0443\u0431\u0438\u043a\u0430\u043c\u0438 \u041a\u043e\u0441\u0442\u0435 \u043d\u0435 \u0432\u0435\u0437\u043b\u043e, \u043d\u043e \u0442\u0435\u043c \u043d\u0435 \u043c\u0435\u043d\u0435\u0435 \u0434\u0435\u0442\u0438-\u043f\u0440\u0438\u043a\u043b\u044e\u0447\u0435\u043d\u0446\u044b \u0433\u0435\u0440\u043e\u0438\u0447\u0435\u0441\u043a\u0438 \u043f\u0440\u0435\u0432\u043e\u0437\u043c\u043e\u0433\u043b\u0438 \u043a\u0440\u044b\u0441\u0438\u043d\u043e\u0433\u043e \u043a\u043e\u0440\u043e\u043b\u044f ;)\n#herokids #roleplay #boardgame #pnprpg', u'comments_disabled': False, u'comments': {u'count': 1}, u'date': 1482243738, u'likes': {u'count': 22}, u'owner': {u'id': u'43237241'}, u'thumbnail_src': u'https://scontent-bru2-1.cdninstagram.com/t51.2885-15/s640x640/sh0.08/e35/15338486_1551801051502691_5653328674196291584_n.jpg?ig_cache_key=MTQwOTQ4NTA5NDg0NjE4NTIzNA%3D%3D.2', u'is_video': False, u'id': u'1409485094846185234', u'display_src': u'https://scontent-bru2-1.cdninstagram.com/t51.2885-15/e35/15338486_1551801051502691_5653328674196291584_n.jpg?ig_cache_key=MTQwOTQ4NTA5NDg0NjE4NTIzNA%3D%3D.2'}

TEST_COMM_DICT = {u'text': u'Account/name for sale ?', u'created_at': 1478387038, u'id': u'17864164036049124', u'user': {u'username': u'karlstuke', u'profile_pic_url': u'https://scontent-vie1-1.cdninstagram.com/t51.2885-19/s150x150/16111039_114702712372274_4748516602666811392_a.jpg', u'id': u'227378072'}}

# URL_ONE_PAGE = u'https://www.instagram.com/p/BOPfznag78S/'
# URL_ONE_PAGE = u'https://www.instagram.com/p/BPo_wvZgCrL/'
URL_ONE_PAGE = u'https://www.instagram.com/p/BMU8EkDAgZH/'

def time_to_iso(timestamp):
#     print arrow.get(timestamp).isoformat(sep='T')
    return arrow.get(timestamp).isoformat(sep='T')

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
    """Parse data from Title page or Foto page for get raw metainformation
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
#     for key in some_dict:
#         pass
#         print key
#     print some_dict[u'code']
#     print some_dict[u'comments']

    # remove some pair from dictionary
    list_item_for_remove = [u'owner',u'id', u'dimensions', u'comments_disabled',
                            u'thumbnail_src', u'is_video']
    for item in list_item_for_remove:
        some_dict.pop(item, None)

    # date in pretty format
#     some_dict[u'date'] = arrow.get(some_dict[u'date']).format('YYYY-MM-DD')
    some_dict[u'date'] = time_to_iso(some_dict[u'date'])

    #  url from key to code
    some_dict[u'url'] = BASE_URL + BASE_SUFFIX_POST + some_dict.pop(u'code')

    # caption:text
    if u'caption' in some_dict:
        some_dict[u'text'] = some_dict.pop(u'caption')
        pass
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

#     print "===="
#     print some_dict
#     print some_dict[u'url']
#     print "===="

    # Count comments
#     some_dict[u'count-comments'] = some_dict[u'comments'][u'count']
    # If have comments run function get_comments()
    if some_dict[u'comments'][u'count'] > 0:
        """vvogu zdes
        """
#         print '**'
#         print get_comments(some_dict[u'url'])
#         print '**'
#         print get_comments(some_dict[u'url'])
        some_dict[u'comments'] = get_comments(some_dict[u'url'])
    else:
        some_dict[u'comments'] = []
        pass
#
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
# #     print change_obg_in_data(data_li)
#     print change_obg_in_data(data_li)
    return change_obg_in_data(data_li)


# # def get_one_rawdata_from_html(html_doc):
# #     """Parse data from Foto page for get raw metainformation
# #     """
# #     soup = BeautifulSoup(html_doc, 'html.parser')
# #     print soup.pretty()

def get_dict_from_one(one_string):
    """Get raw dictionary from raw data
    """
    obj = json.loads(one_string)

    data_li = obj[u'entry_data'][u'PostPage'][0][u'media'][u'comments'][u'nodes']
    return data_li


def remake_comment(dict_comm):

    # remove some pair from dictionary
    dict_comm.pop(u'id')

    # date in pretty format
#     dict_comm[u'date'] = arrow.get(dict_comm[u'created_at']).format('YYYY-MM-DD')
#     dict_comm[u'date'] = arrow.get(dict_comm.pop(u'created_at')).format('YYYY-MM-DD')
    dict_comm[u'date'] = time_to_iso(dict_comm.pop(u'created_at'))

    # text in comment don't change

    # author reduce to pretty format
    dict_comm[u'author'] = dict_comm.pop(u'user')[u'username']

#     print dict_comm
#     print '****'
#     for i in dict_comm:
#         print i
    return dict_comm


def change_obj_in_one_page(data_li):
    """Change dictionary in list on true dictionary
    """
    new_list = [ remake_comment(i) for i in data_li ]
    return new_list


def get_comments(url):
    """Processing one page for getting comments
    """
    html = get_html(url)
#     print html.encode('utf-8')
    one_row = get_unit_rawdata_from_html(html)
#     print one_row
    data_li = get_dict_from_one(one_row)
# #     print change_obj_in_one_page(data_li)
    return change_obj_in_one_page(data_li)

#     print data_li
    pass


def save_data(name, output):
    """Write metadata to file
    """
    namefile = name + u'.json'
#     with open(namefile, 'w') as jsfile:
    with open(namefile, 'w') as json_file:
        data = json.dumps(output, indent=4, sort_keys=True, encoding='utf8')
        json_file.write(data)
#         jsfile.write(json.dumps(output, indent=4, sort_keys=True).decode('utf8'))
    pass

def main():
#     process_unit_page(BASE_URL + NAME_ACCOUNT)
#     print get_comments(URL_ONE_PAGE)
#     remake(TEST_SOME_DICT)
#     remake_comment(TEST_COMM_DICT)
#
#     print process_unit_page(BASE_URL + NAME_ACCOUNT)
#     time_to_iso(1368303838)


    save_data(NAME_ACCOUNT, process_unit_page(BASE_URL + NAME_ACCOUNT))
    pass

if __name__ == '__main__':
    main()
