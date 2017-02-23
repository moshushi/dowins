# -*- encoding: utf-8 -*-
"""
Script downloads and wrap foto and metainformation from INSTARGAM
Prototype
version 0.04
Based on: Instagram-Search-API-Python by TomKDickinson
https://github.com/tomkdickinson/Instagram-Search-API-Python
http://tomkdickinson.co.uk/2016/12/extracting-instagram-data-part-1/
with correct post.query
"""

import requests
import logging
import json
import arrow
import os
import time

ROOT_URL= u'https://www.instagram.com/'
# NAME = u'sa.ny.aa'
NAME = u'frenzytechnix'
# NAME = u"polovinkinandrey"
SUF = u'/?__a=1'
QUERY_URL = u'https://www.instagram.com/query/'
BASE_SUFFIX_POST = u'p/'
# NAME_URL = 'https://instagram.com/sa.ny.aa/?__a=1'


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


def get_cursor_comm(response):
    """
    get cursor from json-string response-object
    """
    return json.loads(response.text)['media']['comments']['page_info']['end_cursor']
#     return json.loads(response.text)['media']['comments']['page_info']['start_cursor']


def get_count_row(response):
    """
    get all sum of post for downloads
    """
    return str(json.loads(response.text)['user']['media']['count'])


def get_count_row_comm(response):
    """
    get all sum of post for downloads
    """
    return str(json.loads(response.text)['media']['comments']['count'])


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
        'origin': ROOT_URL,
        'referer': ROOT_URL + username +'/',
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


def get_post_resp(url):
    """
    Make post request and get
    """
    with requests.Session() as s:
        a = s.get(url)
        csrf_token, cookie = get_csrf_and_cookie_string(a)
        ### Develop
#         print cookie
        #### End Develop
        username = get_username(a)
        head = make_headers(csrf_token, cookie, username)
        s.headers.update(head)
        user_id = get_user_id(a)
        cursor = get_cursor(a)
        counter = get_count_row(a)
        #### Delete next row for production
#         counter = '20'
        post_data = make_post_data(user_id, cursor, counter)
        ### Develop
#         print post_data
        #### End Develop
        p = s.post(QUERY_URL, data=post_data)
#         print p.status_code
#         print type(p.status_code)
#         print p.text
        return p.text, p.status_code
    pass


def workin_insta(url):
    """
    Try 10 time to get info, if not - print number http error
    return unicode string
    """
    semaphor = 100
    i = 10
    while semaphor != 200 and i > 0:
        text, semaphor = get_post_resp(url)
        print semaphor
        i -=1
#     print text
    # text - variable have json unicode string with all info without comments
#     print type(text)
#     print text['media']['nodes']
    print u'OK'.encode('utf8')
    return text


def make_post_data_comm(short_code, cursor, counter):
    """
    Make correct dictonary query for post_data
    IN DEVELOPING
    """
    ### develop
#     short_code = u'BQplF2Chs57'
#     counter = u'50'

    dict_post = {'q': "ig_shortcode(" + short_code + ") { comments.before(" +
                 cursor + ", " + counter + ") {" +
    "count, "
    "nodes {" +
    "  id," +
    "  created_at," +
    "  text," +
    "  user {" +
    "    id," +
    "    profile_pic_url," +
    "    username" +
    "  }" +
    "  }," +
    "page_info" +
    "}" +
    " }"
                 }
    dict_post.update({'ref': 'media::show'})
    return dict_post


def get_post_comment(url):
    """
    Make post request and get Full comment
    need return list of ['nodes']
    IN DEVELOPING
    """
    url = u'https://www.instagram.com/p/BQplF2Chs57?__a=1'
#     url = url + SUF
    print '!!!!For get list of comment use post requests, dont forget retrun node_li'
    with requests.Session() as s:
        a = s.get(url)
        csrf_token, cookie = get_csrf_and_cookie_string(a)

        print cookie


#         username = get_username(a)
#         head = make_headers(csrf_token, cookie, username)
#         username = u'p/BQplF2Chs57' + u'/?taken-by=' + NAME
        username = u'p/BQplF2Chs57'
        head = make_headers(csrf_token, cookie, username)
        # add some value to header
        head.update({u'authority': u'www.instagram.com'})
        # problem here
        print head
#         print type(head)
#         b = json.dumps(head)
#         pretty_print_result(b)

#         for i in head.keys()
#         print head.values()
#         s.headers.update(head)

        # for develop delete after - from
        short_code = u'BQplF2Chs57'
#         cursor = u'AQDRImLPBeiRKOcnQy7DTQHrdgaK_lT66uHzeak5Y6dDf2KAQVIsRb_OmrBLGRgbLbtvtj9etarR1T2WOTEXZFx3970npubmbGUYsAO-kYF621yf5LrGYY_zm9dAUx6_9sk'
#         counter = u'20'
        # for develop delete after - to
        cursor = get_cursor_comm(a)
        counter = get_count_row_comm(a)
        print cursor
        print get_count_row_comm(a)

        post_data = make_post_data_comm(short_code, cursor, counter)
#         pretty_print_result(post_data)
#         print type(post_data)
#         print post_data.keys()
#         print post_data['q']
#         print post_data
#         print get_cursor(a)
        print '---'
        print post_data
        print a.text.encode('utf8')
        print '---'
#         print get_cursor_comm(a)
        print get_count_row_comm(a)

        p = s.post(QUERY_URL, data=post_data)
        print p.status_code
        return p.text, p.status_code


def get_raw_comments_from_page(url):
    """
    Get comments from post-foto
    """
#     print 'Processing comments from posts'
#     url = u'https://www.instagram.com/p/BQplF2Chs57'
#     url = u'https://www.instagram.com/p/BPSRWn3Abpe'

    resp = requests.get(url + SUF)
#     print resp.status_code
#     print pretty_print_result(resp.text)
#     print type(resp.text)
    comm = json.loads(resp.text)[u'media'][u'comments']
#     print json.loads(resp.text)[u'media'][u'comments'][u'count']
#     print comm[u'count']
#     row_li = json.loads(resp.text)[u'media'][u'comments'][u'nodes']
    row_li = comm[u'nodes']
#     if type(row) == type({}):
#         print type(row)
#         print row.keys()
#         pretty_print_result(json.dumps(row))
#     print type(row_li)
#     print len(row_li)
#     print '-----'
#     getco = json.loads(resp.text)[u'media'][u'comments'][u'page_info']
    getco = comm[u'page_info']
    if getco[u'has_next_page'] == False or getco[u'has_previous_page'] == False:
#         print "don't need more extended getting comment"
        print ".",
#         print row_li[0]
#         print row_li
        return row_li
#     else:
#     print 'need more extended getting comment'
    print ':'
    # Next string uncomment for continue developing
#     row_li = get_post_comment(url)
#     print row_li
    return row_li


def remake_comm(some_dict):
#     some_dict = {u'text': u'\u041a\u043b\u0430\u0441', u'created_at': 1487436467, u'id': u'17849394820182849', u'user': {u'username': u'annette_pil', u'profile_pic_url': u'https://scontent-frt3-1.cdninstagram.com/t51.2885-19/s150x150/16585102_380159532340647_7652220987924021248_a.jpg', u'id': u'2205336451'}}
#     print some_dict
    new_dict = {
        u'comment': some_dict[u'text'],
        u'date': arrow.get(some_dict[u'created_at']).isoformat(sep='T'),
        u'author': some_dict[u'user'][u'username']
    }

#     print new_dict
    return new_dict
    pass

def get_comments_from_page(url):
    comm_li = get_raw_comments_from_page(url)
    new_comm_li = [remake_comm(i) for i in comm_li]
#     print new_comm_li
    return new_comm_li
#     new_comments_li =
#     print new_comments_li


def remake_dict(some_dict):
    """
    Remake dictionary for correct save to JSON file
    """
    ## date in iso format
    some_dict[u'date'] = arrow.get(some_dict[u'date']).isoformat(sep='T')
    ## url from key to code
    some_dict[u'url'] = ROOT_URL + BASE_SUFFIX_POST + some_dict.pop(u'code')
    ## caption -> text
    if u'caption' in some_dict:
        some_dict[u'text'] = some_dict.pop(u'caption')
    else:
        some_dict[u'text'] = ""
    ## image source url
    s = some_dict.pop(u'display_src')
    sep = u'.jpg'
    rest = s.split(u'.jpg')[0] + u'.jpg'
    some_dict[u'img-source'] = rest
    ## like's
    some_dict[u'likes'] = some_dict[u'likes'][u'count']
    ## Proccessing comment
    if some_dict[u'comments'][u'count'] > 0:
        some_dict[u'comments'] = get_comments_from_page(some_dict[u'url'])
    else:
        some_dict[u'comments'] = []
    return some_dict
#     some_dict[u'date'] = '123'

def remake_main_data(some_str):
    """
    Get string, make some change, output is list
    """
    data_li = json.loads(some_str)[u'media'][u'nodes']
#     data_li = [{u'code': u'BQqQGRfBwFk', u'comments': {u'count': 9}, u'caption': u'\u041f\u0430\u043c\u044f\u0442\u044c-\u0441\u0438\u043b\u044c\u043d\u0435\u0435 \u043e\u0431\u0438\u0434. \u044f \u043f\u043e\u043c\u043d\u044e', u'likes': {u'count': 4092}, u'date': 1487436439, u'is_video': True, u'display_src': u'https://scontent-frt3-1.cdninstagram.com/t51.2885-15/e35/16789474_257263561396009_1937190525790584832_n.jpg?ig_cache_key=MTQ1MzA0NDYyOTYxNTYwODE2NA%3D%3D.2'}, {u'code': u'BQplF2Chs57', u'comments': {u'count': 41}, u'caption': u'\u043c\u043e\u0433\u0443 \u0438\u0441\u043f\u043e\u043b\u043d\u044f\u0442\u044c \u0436\u0435\u043b\u0430\u043d\u0438\u044f \U0001f31f\nLocation: \u043a\u0440\u0443\u0442\u043e\u0439 \u0430\u043d\u0442\u0438 \u043a\u0438\u043d\u043e\u0442\u0435\u0430\u0442\u0440 @rockfellow210! \u043e\u0447\u0435\u043d\u044c \u0430\u0442\u043c\u043e\u0441\u0444\u0435\u0440\u043d\u043e\u0435 \u043c\u0435\u0441\u0442\u043e)\nPhoto : @danilyukart \u2764\ufe0f', u'likes': {u'count': 18865}, u'date': 1487413891, u'is_video': False, u'display_src': u'https://scontent-frt3-1.cdninstagram.com/t51.2885-15/e35/16583709_198534297296189_4234798802797592576_n.jpg?ig_cache_key=MTQ1Mjg1NTQ4NDE0NjQzNzc1NQ%3D%3D.2'}, {u'code': u'BQpPEJSBtD9', u'comments': {u'count': 19}, u'caption': u'\u0421 \u0434\u043e\u0431\u0440\u0435\u043d\u044c\u043a\u0438\u043c \U0001f44b\U0001f3fb\n\u041a\u0442\u043e \u043a\u0443\u0434\u0430 \u0434\u0435\u0440\u0436\u0438\u0442 \u043f\u0443\u0442\u044c \u043d\u0430 \u044d\u0442\u0438\u0445 \u0432\u044b\u0445\u043e\u0434\u043d\u044b\u0445 ??)\n\u0421\u043f\u0430\u0441\u0438\u0431\u043e, \u041c\u0430\u0448\u0430 @m.s.nailstudio \u0437\u0430 \u0438\u0437\u0443\u043c\u0440\u0443\u0434\u043d\u043e\u0435 \u0447\u0443\u0434\u043e \u0438 \u043a\u043b\u0430\u0441\u0441\u043d\u044b\u0435 \u0440\u0430\u0441\u0441\u043a\u0430\u0437\u044b ,\u044f \u0435\u0449\u0451 \u043f\u0440\u0438\u0439\u0434\u0443 !', u'likes': {u'count': 17297}, u'date': 1487402343, u'is_video': False, u'display_src': u'https://scontent-frt3-1.cdninstagram.com/t51.2885-15/e35/16789942_1673735729585483_1643648073957638144_n.jpg'}, {u'code': u'BQn2dV1hMa7', u'comments': {u'count': 24}, u'caption': u'\u0412\u0435\u0441\u043d\u0443 \u0437\u0430\u043a\u0430\u0437\u044b\u0432\u0430\u043b\u0438 ?) \u043d\u0443 \u043c\u044b \u0441 @danilyukart \u0440\u0435\u0448\u0438\u043b\u0438  \u0447\u0442\u043e \u043f\u043e\u0440\u0430\U0001f644\nLocation : @rockfellow210 ! \u043c\u044b \u043e\u0446\u0435\u043d\u0438\u043b\u0438 \u044d\u0442\u043e \u043c\u0435\u0441\u0442\u043e\u043e\u043e\u043e)', u'likes': {u'count': 18596}, u'date': 1487355888, u'is_video': False, u'display_src': u'https://scontent-frt3-1.cdninstagram.com/t51.2885-15/e35/16789485_298121417270360_3938643078113394688_n.jpg?ig_cache_key=MTQ1MjM2ODkxNTY3MzE3MTY0Mw%3D%3D.2'}, {u'code': u'BQnuqjfBgWt', u'comments': {u'count': 55}, u'caption': u'\u0421\u043f\u0430\u0441\u0438\u0431\u043e \u0442\u0435\u0431\u0435 \u0437\u0430 \u0434\u0435\u043d\u044c \u0438 \u0437\u0430 \u0441\u044a\u0451\u043c\u043a\u0443 ! \u042f \u0432\u043b\u044e\u0431\u0438\u043b\u0430\u0441\u044c \u0432 \u044d\u0442\u043e \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435,\u043f\u043e\u044f\u0432\u0438\u043b\u043e\u0441\u044c \u0432\u0434\u043e\u0445\u043d\u043e\u0432\u0435\u043d\u0438\u0435 ! \u0412\u0435\u0441\u043d\u0430 \u043d\u0430\u0447\u0438\u043d\u0430\u0435\u0442\u0441\u044f \u043f\u0440\u0435\u0436\u0434\u0435 \u0432\u0441\u0435\u0433\u043e \u0432 \u0433\u043e\u043b\u043e\u0432\u0435 \u0438 \u0432 \u043e\u043a\u0440\u0443\u0436\u0435\u043d\u0438\u0438 )\nPh: @danilyukart \u2764\ufe0f\u2764\ufe0f\u2764\ufe0f\u2764\ufe0f\u2764\ufe0f\u2764\ufe0f\u2764\ufe0f\u2764\ufe0f', u'likes': {u'count': 22552}, u'date': 1487351802, u'is_video': False, u'display_src': u'https://scontent-frt3-1.cdninstagram.com/t51.2885-15/e35/16789479_1790953457893337_3908477598648238080_n.jpg'}, {u'code': u'BQk6EL2BGHy', u'comments': {u'count': 26}, u'caption': u'\u0421\u043f\u0430\u0441\u0438\u0431\u043e \u041a\u0438\u0435\u0432\u0443 \u0437\u0430 \u0445\u043e\u043b\u043e\u0434\u0430,\u0430 @vuna.me \u0437\u0430 \u0447\u0442\u043e \u0441\u043f\u0430\u0441\u0430\u0435\u0442\u0435 \u043c\u0435\u043d\u044f \u043e\u0442 \u044d\u0442\u043e\u0433\u043e \u0443\u0436\u0430\u0441\u0430 \U0001f63f\n\u0438 \u0437\u0434\u0435\u0441\u044c \u044f \u043f\u043e\u043b\u044e\u0431\u0438\u043b\u0430 \u0448\u0430\u043f\u043a\u0438 \u0435\u0449\u0451 \u0431\u043e\u043b\u044c\u0448\u0435 !', u'likes': {u'count': 22962}, u'date': 1487257116, u'is_video': False, u'display_src': u'https://scontent-frt3-1.cdninstagram.com/t51.2885-15/e35/16585608_1260757557313212_1595671231971983360_n.jpg'}, {u'code': u'BQii6hhhG2r', u'comments': {u'count': 40}, u'caption': u'\U0001f63f\U0001f63f\U0001f63f\U0001f63f\U0001f63f\U0001f63f', u'likes': {u'count': 22852}, u'date': 1487177869, u'is_video': False, u'display_src': u'https://scontent-frt3-1.cdninstagram.com/t51.2885-15/e35/16465838_391025604598149_7571675207069335552_n.jpg?ig_cache_key=MTQ1MDg3NTU4NTI3MzU1NjM5NQ%3D%3D.2'}, {u'code': u'BQh5DCnBQJB', u'video_views': 24561, u'comments': {u'count': 22}, u'caption': u'\u0427\u0442\u043e\u0431\u044b \u044f \u043f\u043e\u043c\u043d\u0438\u043b\u0430,\u0430 \u0432\u044b \u0437\u043d\u0430\u043b\u0438 \u043a\u0430\u043a\u043e\u0439 \u0431\u044b\u043b \u0447\u0443\u0434\u0435\u0441\u043d\u044b\u0439 \u0434\u0435\u043d\u044c', u'likes': {u'count': 7613}, u'date': 1487155919, u'is_video': True, u'display_src': u'https://scontent-frt3-1.cdninstagram.com/t51.2885-15/s1080x1080/e15/fr/16583356_1644075285894812_6931956316709584896_n.jpg'}, {u'code': u'BQhxC3JBwHh', u'comments': {u'count': 3}, u'caption': u'\u0412\u0447\u0435\u0440\u0430 \u0432\u043e\u0442 \u0431\u044b\u043b \u0414\u0435\u043d\u044c \u0421\u0432\u044f\u0442\u043e\u0433\u043e \u0412\u0430\u043b\u0435\u043d\u0442\u0438\u043d\u0430 \U0001f3e9 \u0438 \u043f\u043e\u043a\u0430 \u0432\u0441\u0435 \u043f\u0430\u0440\u043e\u0447\u043a\u0438 \u0440\u0430\u0434\u043e\u0432\u0430\u043b\u0438 \u0434\u0440\u0443\u0433 \u0434\u0440\u0443\u0433\u0430, \u043c\u043e\u044f \u0440\u0430\u0434\u043e\u0441\u0442\u044c - \u043c\u0430\u0441\u043b\u043e @apothecary_skin_desserts ,\u0438 \u043d\u0435 \u043e\u0434\u0438\u043d \u0440\u0430\u0437 \u0432 \u0433\u043e\u0434\u0443 ,\u0430 \u0435\u0436\u0435\u043c\u0435\u0441\u044f\u0447\u043d\u043e ,\u0435\u0436\u0435\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u043e ,\u0435\u0436\u0435\u0434\u043d\u0435\u0432\u043d\u043e \U0001f31f\U0001f54a', u'likes': {u'count': 11038}, u'date': 1487151723, u'is_video': False, u'display_src': u'https://scontent-frt3-1.cdninstagram.com/t51.2885-15/e35/16788947_1257474197633232_2480019665531699200_n.jpg?ig_cache_key=MTQ1MDY1NjI1NTkxNTI2MjQzMw%3D%3D.2'}, {u'code': u'BQgbOKqBA1w', u'comments': {u'count': 17}, u'caption': u'\u0441\u0430\u043b\u044e\u0442\u0438\u043a\u0438', u'likes': {u'count': 19805}, u'date': 1487106727, u'is_video': False, u'display_src': u'https://scontent-frt3-1.cdninstagram.com/t51.2885-15/e35/16585665_1430609003617307_8964350955894079488_n.jpg?ig_cache_key=MTQ1MDI3ODgwMDc4NDEwMDcyMA%3D%3D.2'}, {u'code': u'BQgaBzjhNYZ', u'comments': {u'count': 15}, u'caption': u'\u041e\u0447\u0435\u043d\u044c \u0434\u0430\u0432\u043d\u043e \u0431\u044b\u043b\u0430 \u044d\u0442\u0430 \u0441\u044a\u0435\u043c\u043a\u0430 ,\u0438 \u044f \u0443\u0436\u0435 \u0445\u043e\u0447\u0443 \u0445\u043e\u0447\u0443 \u0445\u043e\u0447\u0443 \u043d\u043e\u0432\u044b\u0445 \u0441\u043d\u0438\u043c\u043a\u043e\u0432,\u043a\u0440\u0443\u0442\u043e\u0439 \u0430\u0442\u043c\u043e\u0441\u0444\u0435\u0440\u044b \u0438 \u0441\u0443\u0435\u0442\u044b \u043f\u0435\u0440\u0435\u0434 \u0442\u0435\u043c,\u043a\u0430\u043a \u0441\u0442\u0430\u0442\u044c \u0432 \u043a\u0430\u0434\u0440\U0001f63b \u0438 \u0442\u0430\u043a \u0436\u0435 \u0434\u0430\u0432\u043d\u043e \u0443 \u043c\u0435\u043d\u044f \u044d\u0442\u0430 \u043f\u0438\u0436\u0430\u043c\u0430 \u043e\u0442 @kotovich_lingerie - \u0438 \u0432\u0441\u0435\u0433\u0434\u0430 \u0445\u043e\u0442\u0435\u043b\u0430 \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u044d\u0442\u0443 \u043a\u0440\u0430\u0441\u043e\u0442\u0443 ,\u043d\u043e \u0432\u043e\u0442 \u043a\u0430\u043a \u0440\u0430\u0437 \u043f\u043e\u0434\u0432\u0435\u0440\u0433\u043d\u0443\u043b\u0441\u044f \u0441\u043b\u0443\u0447\u0430\u0439 \U0001f54a\u0442\u0430\u043a \u043a\u0430\u043a \u043c\u043d\u043e\u0433\u0438\u0435 \u0443\u0442\u0432\u0435\u0440\u0436\u0434\u0430\u044e\u0442 ,\u0447\u0442\u043e \u0441\u0435\u0433\u043e\u0434\u043d\u044f \u043a\u043b\u0430\u0441\u0441\u043d\u044b\u0439 \u043f\u0440\u0430\u0437\u0434\u043d\u0438\u043a \u0442\u043e \u0438 \u043f\u043e\u0434\u0430\u0440\u043a\u0438 \u0434\u043e\u043b\u0436\u043d\u044b \u0431\u044b\u0442\u044c \u043d\u0435 \u0445\u0443\u0436\u0435 ,\u0430 \u043f\u0438\u0436\u0430\u043c\u0430 - \u043b\u0443\u0447\u0448\u0435\u0435 ,\u0447\u0442\u043e \u043c\u043e\u0436\u043d\u043e \u043f\u0440\u0438\u0434\u0443\u043c\u0430\u0442\u044c ) \n\u0441\u043f\u0430\u0441\u0438\u0431\u043e @kotovich_lingerie\U0001f31f', u'likes': {u'count': 16192}, u'date': 1487106101, u'is_video': False, u'display_src': u'https://scontent-frt3-1.cdninstagram.com/t51.2885-15/sh0.08/e35/p750x750/16788443_693496874154468_6364037820566208512_n.jpg?ig_cache_key=MTQ1MDI3MzU1MzI5ODgwNjI5Nw%3D%3D.2'}, {u'code': u'BQddTLyh6Y_', u'comments': {u'count': 25}, u'caption': u'\u041c\u044b \u043f\u043e\u043c\u0447\u0438\u043c\u0441\u044f ,\u043c\u044b \u043f\u043e\u043b\u0435\u0442\u0438\u043c,\u0438 \u043f\u0443\u0441\u0442\u044c \u0433\u043e\u0440\u0438\u0442 \u043e\u0433\u043d\u0451\u043c \u044d\u0442\u043e \u0442\u0440\u0435\u0442\u0438\u0439 \u0420\u0438\u043c"\U0001f3bc', u'likes': {u'count': 15986}, u'date': 1487007153, u'is_video': False, u'display_src': u'https://scontent-frt3-1.cdninstagram.com/t51.2885-15/e35/16464817_1824694054439613_6586615300861460480_n.jpg'}, {u'code': u'BQbJVGKh6ML', u'comments': {u'count': 10}, u'caption': u'\u043b\u044e\u0431\u0438 \u043c\u0435\u043d\u044f \u0442\u0430\u043a \u0436\u0435 ,\u043a\u0430\u043a \u044f \u043b\u044e\u0431\u043b\u044e \u043d\u043e\u0447\u043d\u044b\u0435 \u0433\u043e\u0440\u043e\u0434\u0430', u'likes': {u'count': 14154}, u'date': 1486929574, u'is_video': False, u'display_src': u'https://scontent-frt3-1.cdninstagram.com/t51.2885-15/e35/16583282_391155111250055_631774884489330688_n.jpg'}, {u'code': u'BQZ-SZ2BJPJ', u'comments': {u'count': 37}, u'caption': u'\u0441 \u043d\u0435\u043a\u043e\u0442\u043e\u0440\u044b\u043c\u0438 \u043b\u044e\u0434\u044c\u043c\u0438 \u043d\u0435 \u0432\u0438\u0434\u0435\u043b\u0430\u0441\u044c \u0441 \u043f\u0440\u043e\u0448\u043b\u043e\u0433\u043e \u0433\u043e\u0434\u0430\U0001f62d\U0001f62d\U0001f62d\n\u0412 \u043a\u0430\u043a\u043e\u0439 \u0431\u044b \u0441\u0442\u0440\u0430\u043d\u0435 \u043d\u0435 \u0436\u0438\u0442\u044c,\u043d\u043e \u043c\u0435\u0441\u044f\u0446 \u0431\u0435\u0437 \u0436\u0438\u0432\u043e\u0433\u043e \u043e\u0431\u0449\u0435\u043d\u0438\u044f -\u043e\u0447\u0435\u043d\u044c \u043e\u0447\u0435\u043d\u044c \u0433\u0440\u0443\u0441\u0442\u043d\u043e (', u'likes': {u'count': 21284}, u'date': 1486890230, u'is_video': False, u'display_src': u'https://scontent-frt3-1.cdninstagram.com/t51.2885-15/e35/16583183_1308688162527181_8145340081691951104_n.jpg'}, {u'code': u'BQYuyxnh08N', u'comments': {u'count': 69}, u'caption': u'\u0432\u043e\u0442 \u043e\u043d\u2764\ufe0f \u0441\u0435\u0433\u043e\u0434\u043d\u044f,\u0432\u043e\u0442 \u0447\u0442\u043e\u0431\u044b \u043d\u0435 \u0441\u043e\u0432\u0440\u0430\u0442\u044c -\u043e\u0434\u043d\u043e\u0439 \u0438\u0441\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439 \u043c\u0435\u0447\u0442\u043e\u0439 \u0441\u0442\u0430\u043b\u043e \u0431\u043e\u043b\u044c\u0448\u0435) \u0435\u0449\u0451 \u043a\u043e\u0433\u0434\u0430 \u0448\u043b\u0430 \u043f\u043e \u043f\u0430\u0440\u0430\u043b\u043b\u0435\u043b\u044c\u043d\u043e\u0439 \u0443\u043b\u0438\u0446\u0435 \u0438 \u0441\u043b\u0443\u0448\u0430\u043b\u0430 \u0448\u0443\u043c \u0432\u043e\u0434\u044b \u0444\u043e\u043d\u0442\u0430\u043d\u0430 -\u0441\u0442\u0440\u0430\u0448\u043d\u043e \u0438 \u0440\u0430\u0434\u043e\u0441\u0442\u043d\u043e . \u041d\u0443 \u0432\u0441\u0435,\u044f \u043d\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0430 \u043b\u044e\u0431\u043e\u0432\u044c\u044e \u0438 \u0433\u043e\u0442\u043e\u0432\u0430 \u0435\u0451 \u0434\u0430\u0440\u0438\u0442\u044c \U0001f54a', u'likes': {u'count': 24337}, u'date': 1486848553, u'is_video': False, u'display_src': u'https://scontent-frt3-1.cdninstagram.com/t51.2885-15/e35/16464851_1893727254178835_3021238664983216128_n.jpg'}, {u'code': u'BQYsl-VB1El', u'comments': {u'count': 20}, u'caption': u'\u0413\u0443\u043b\u044f\u043b\u0438 \u043f\u043e \u0442\u0451\u043f\u043b\u043e\u043c\u0443 \u0441\u043e\u043b\u043d\u0435\u0447\u043d\u043e\u043c\u0443 \u0420\u0438\u043c\u0443,\u043a\u0443\u0448\u0430\u043b\u0438 \u0432\u043a\u0443\u0441\u043d\u0435\u0439\u0448\u0435\u0435 \u043c\u043e\u0440\u043e\u0436\u0435\u043d\u043e\u0435 \u043f\u043e\u0434 \u0448\u0443\u043c \u0444\u043e\u043d\u0442\u0430\u043d\u0430 \u043d\u0430 \u0422\u0440\u0435\u0432\u0438. \u0421\u0447\u0430\u0441\u0442\u044c\u0435 ? \u0414\u0430 ,\u0431\u0435\u0437\u0443\u0441\u043b\u043e\u0432\u043d\u043e', u'likes': {u'count': 16703}, u'date': 1486847399, u'is_video': False, u'display_src': u'https://scontent-frt3-1.cdninstagram.com/t51.2885-15/e35/16463940_380764898970612_1014765025308442624_n.jpg?ig_cache_key=MTQ0ODEwMzQwMzc5MTUzNjQyMQ%3D%3D.2'}, {u'code': u'BQV89T8BqXZ', u'comments': {u'count': 34}, u'caption': u'\u043e\u0434\u043d\u043e\u0437\u043d\u0430\u0447\u043d\u043e ,\u043c\u043e\u0440\u0435 !', u'likes': {u'count': 21992}, u'date': 1486755316, u'is_video': False, u'display_src': u'https://scontent-frt3-1.cdninstagram.com/t51.2885-15/e35/16464773_380263892350303_8574841295237808128_n.jpg'}, {u'code': u'BQVwZNghUQ9', u'comments': {u'count': 21}, u'caption': u'\u0411\u043e\u043b\u044c\u0448\u0430\u044f \u0447\u0430\u0441\u0442\u044c \u043b\u044e\u0434\u0435\u0439,\u043a\u043e\u0442\u043e\u0440\u0430\u044f \u0433\u043e\u0432\u043e\u0440\u0438\u0442,\u0447\u0442\u043e \u0446\u0435\u043d\u0438\u0442 "\u043d\u0430\u0442\u0443\u0440\u0430\u043b\u044c\u043d\u0443\u044e \u043a\u0440\u0430\u0441\u043e\u0442\u0443" \u0434\u0430\u0436\u0435 \u043d\u0435 \u0438\u043c\u0435\u044e\u0442 \u043f\u043e\u043d\u044f\u0442\u0438\u044f \u0447\u0442\u043e \u044d\u0442\u043e.', u'likes': {u'count': 20457}, u'date': 1486748728, u'is_video': False, u'display_src': u'https://scontent-frt3-1.cdninstagram.com/t51.2885-15/e35/16464782_580071805533269_5104649956501749760_n.jpg?ig_cache_key=MTQ0NzI3NTY5Mzk5MzE4MjI2OQ%3D%3D.2'}, {u'code': u'BQTB7C1Birw', u'comments': {u'count': 19}, u'caption': u'\u043e\u0447\u0435\u043d\u044c \u0441\u0438\u043c\u0432\u043e\u043b\u0438\u0447\u043d\u043e \u0438 \u043e\u0447\u0435\u043d\u044c \u0433\u0440\u0443\u0441\u0442\u043d\u043e \U0001f1ee\U0001f1f9', u'likes': {u'count': 20904}, u'date': 1486657255, u'is_video': False, u'display_src': u'https://scontent-frt3-1.cdninstagram.com/t51.2885-15/e35/16585105_1459792967378486_6333404550443040768_n.jpg'}, {u'code': u'BQP_sJaBmqU', u'comments': {u'count': 48}, u'caption': u'\u0435\u0441\u0442\u044c \u043e\u0434\u043d\u0430 \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u0430 \u0432 \u044d\u0442\u043e\u0439 \u043f\u0440\u0435\u043a\u0440\u0430\u0441\u043d\u043e\u0439 \u043f\u043e\u0435\u0437\u0434\u043a\u0435 \u0432 \u0418\u0442\u0430\u043b\u0438\u044e - \u044f \u043a\u0430\u043a \u0442\u043e \u0437\u0434\u0435\u0441\u044c \u043d\u0435 \u0432\u043e\u0441\u043f\u0440\u0438\u043d\u0438\u043c\u0430\u044e \u0440\u0435\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c . \u041c\u043d\u0435 \u043a\u0430\u0436\u0435\u0442\u0441\u044f ,\u0447\u0442\u043e \u043c\u043e\u0436\u043d\u043e \u043f\u0440\u043e\u0441\u0442\u043e \u0445\u043e\u0434\u0438\u0442\u044c \u043f\u043e \u0443\u043b\u0438\u0446\u0430\u043c,\u0436\u0438\u0442\u044c \u0432 \u0434\u0440\u0443\u0433\u043e\u0439 \u0441\u0442\u0440\u0430\u043d\u0435 \u0438 \u0442\u0430\u043a \u0442\u044b \u0432\u044b\u0443\u0447\u0438\u0448\u044c \u044f\u0437\u044b\u043a,\u043c\u043e\u0436\u043d\u043e \u043a\u0443\u0448\u0430\u0442\u044c \u0432\u0441\u0435 \u043f\u043e\u0434\u0440\u044f\u0434 \u0438 \u0442\u044b \u043d\u0435 \u043f\u043e\u043f\u0440\u0430\u0432\u0438\u0448\u044c\u0441\u044f ,\u0432 \u043e\u0431\u0449\u0435\u043c \u043c\u043e\u0436\u043d\u043e \u0432\u0441\u0435 \u0442\u043e,\u043a \u0447\u0435\u043c\u0443 \u0434\u043e\u043c\u0430 \u044f \u043e\u0442\u043d\u043e\u0448\u0443\u0441\u044c \u0441\u043e\u0432\u0441\u0435\u043c \u0438\u043d\u0430\u0447\u0435 . \u041f\u043b\u044e\u0441 \u043a\u043e \u0432\u0441\u0435\u043c\u0443 ,\u044f \u0441\u0442\u0430\u043b\u0430 \u0437\u0430\u043c\u0435\u0447\u0430\u0442\u044c \u043a\u0430\u043a \u043f\u043e\u0441\u043b\u0435 \u043b\u0435\u043a\u0446\u0438\u0439 \u0445\u043e\u0447\u0443 \u0434\u043e\u043c\u043e\u0439,\u043f\u043e\u0442\u043e\u043c\u0443 \u0447\u0442\u043e \u0442\u0430\u043c \u0433\u043e\u0432\u043e\u0440\u044f\u0442 \u043d\u0430 \u043f\u043e\u043d\u044f\u0442\u043d\u043e\u043c \u043c\u043d\u0435 \u044f\u0437\u044b\u043a\u0435,\u0438 \u0434\u0430\u0436\u0435 \u0435\u0441\u043b\u0438 \u043d\u0430 \u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u043e\u043c \u043c\u044b \u0433\u043e\u0432\u043e\u0440\u0438\u043c \u0432\u043f\u043e\u043b\u043d\u0435 \u043d\u043e\u0440\u043c\u0430\u043b\u044c\u043d\u043e,\u0442\u043e \u0432\u0441\u0435 \u0440\u0430\u0432\u043d\u043e \u043d\u0438\u043a\u0442\u043e \u043d\u0435 \u043f\u043e\u043d\u0438\u043c\u0430\u0435\u0442 \u0442\u0432\u043e\u0435\u0433\u043e \u0434\u0443\u0440\u043d\u043e\u0433\u043e \u0433\u043e\u0432\u043e\u0440\u0430,\u0442\u044b \u0443\u0436\u0435 \u043d\u0435 \u043c\u043e\u0436\u0435\u0448\u044c \u0441\u043a\u0430\u0437\u0430\u0442\u044c "\u043c\u0430\u0433\u0430\u0437,\u0444\u043e\u0442\u043a\u0430\u0442\u044c,\u0438\u043d\u0441\u0442\u0430,\u043a\u0440\u043e\u0441\u0441\u044b". \u041c\u0435\u043d\u044f \u043e\u0447\u0435\u043d\u044c \u0441\u0442\u0430\u043b\u0438 \u0431\u0435\u0441\u0438\u0442\u044c \u043b\u044e\u0434\u0438 ,\u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0432 \u0442\u0443\u043f\u0443\u044e \u043d\u0430\u0432\u0438\u0441\u0430\u044e\u0442 \u0441 \u0432\u043e\u043f\u0440\u043e\u0441\u0430\u043c\u0438 \u043d\u0430 \u0434\u0440\u0443\u0433\u0438\u0445 \u044f\u0437\u044b\u043a\u0430\u0445,\u0430 \u044f \u043f\u0440\u043e\u0441\u0442\u043e \u043d\u0435 \u043f\u043e\u043d\u0438\u043c\u0430\u044e \u044d\u0442\u043e\u0433\u043e. \u0418 \u043f\u043e\u043b\u043e\u0432\u0438\u043d\u0443 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u043e\u0442\u0432\u0435\u0447\u0430\u044e \u043d\u0430 \u0438\u0442\u0430\u043b\u044c\u044f\u043d\u0441\u043a\u043e\u043c ,\u0430 \u0432\u0442\u043e\u0440\u0443\u044e -\u043d\u0430 \u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u043e\u043c . \u0425\u043e\u0442\u044f \u0435\u0441\u043b\u0438 \u0431\u044b \u044f \u0432\u044b\u0431\u0438\u0440\u0430\u043b\u0430 \u043e\u0441\u0442\u0430\u0442\u044c\u0441\u044f \u0437\u0434\u0435\u0441\u044c \u0438\u043b\u0438 \u0432\u0435\u0440\u043d\u0443\u0442\u0441\u044f \u0432 \u0423\u043a\u0440\u0430\u0438\u043d\u0443 \u0434\u0443\u043c\u0430\u044e \u043e\u0442\u0432\u0435\u0442 \u043e\u0447\u0435\u0432\u0438\u0434\u0435\u043d ,\u0447\u0442\u043e \u044f \u0431\u044b \u043e\u0441\u0442\u0430\u043b\u0430\u0441\u044c. \u043d\u043e \u0441\u0435\u0439\u0447\u0430\u0441 \u0445\u043e\u0447\u0435\u0442\u0441\u044f \u0441\u0434\u0435\u043b\u0430\u0442\u044c \u043f\u0435\u0440\u0435\u0440\u044b\u0432 \u0438 \u043f\u043e\u0433\u043e\u0432\u043e\u0440\u0438\u0442\u044c \u0441\u043e \u0441\u0432\u043e\u0438\u043c\u0438 \u0440\u043e\u0434\u043d\u044b\u043c\u0438 \u043b\u044e\u0434\u044c\u043c\u0438. \u0418 \u0435\u0441\u043b\u0438 \u043a\u0442\u043e \u0442\u043e \u0431\u044b\u043b \u0432 \u043b\u0430\u0433\u0435\u0440\u044f\u0445,\u0438\u043b\u0438 \u0432\u043e\u0442 \u0432 \u0442\u0430\u043a\u0438\u0445 \u043f\u043e\u0435\u0437\u0434\u043a\u0430\u0445 \u0434\u0443\u043c\u0430\u044e \u0432\u044b \u0437\u043d\u0430\u0435\u0442\u0435 \u0447\u0442\u043e \u0441\u0430\u043c\u043e\u0435 \u043e\u0431\u0438\u0434\u043d\u043e -\u044d\u0442\u043e \u043a\u043e\u0433\u0434\u0430 \u0442\u044b \u0437\u043d\u0430\u043a\u043e\u043c\u0438\u0448\u044c\u0441\u044f \u0441 \u043e\u0433\u0440\u043e\u043c\u043d\u044b\u043c \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e\u043c \u043b\u044e\u0434\u0435\u0439,\u0437\u0430\u0432\u043e\u0434\u0438\u0448\u044c \u0445\u043e\u0440\u043e\u0448\u0438\u0435 \u0437\u043d\u0430\u043a\u043e\u043c\u0441\u0442\u0432\u0430,\u0442\u044b \u0436\u0438\u0432\u0451\u0448\u044c ,\u043f\u044c\u0451\u0448\u044c \u043f\u0430\u0444\u043e\u0441\u043d\u043e \u0432\u0438\u043d\u043e \u0441 \u0442\u0430\u043a\u0438\u043c\u0438 \u0436\u0435 \u0434\u0443\u0440\u043d\u044b\u043c\u0438 \u043a\u0430\u043a \u0438 \u0442\u044b ,\u0435\u0441\u0442\u044c \u043f\u043e\u0434\u0440\u0443\u0436\u043a\u0438 ,\u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0442\u0435\u0431\u0435 \u0434\u0435\u043b\u0430\u044e\u0442 \u0442\u043e\u043c\u0430\u0442\u043d\u044b\u0439 \u0441\u0443\u043f \u0438 \u0432\u044b \u043d\u0430 \u0440\u0443\u0441\u0441\u043a\u043e\u043c \u043e\u0431\u0441\u0443\u0436\u0434\u0430\u0435\u0442\u0435 \u0440\u044f\u0434\u043e\u043c \u0441\u0438\u0434\u044f\u0449\u0435\u0433\u043e \u0438\u0441\u043f\u0430\u043d\u0446\u0430,\u0430 \u0447\u0435\u0440\u0435\u0437 \u043f\u0430\u0440\u0443 \u0434\u043d\u0435\u0439 \u0442\u044b \u0443\u0435\u0437\u0436\u0430\u0435\u0448\u044c . \u042d\u0442\u043e \u043a\u043e\u0433\u0434\u0430 \u0442\u0435\u0431\u0435 10 \u043b\u0435\u0442,\u0442\u044b \u0432 \u043c\u043b\u0430\u0434\u0448\u0435\u043c \u043e\u0442\u0440\u044f\u0434\u0435 \u0438 \u043f\u043e\u0437\u043d\u0430\u043a\u043e\u043c\u0438\u043b\u0430\u0441\u044c \u0441\u043e "\u0441\u0442\u0430\u0440\u0448\u0430\u043a\u0430\u043c\u0438". \u0418 \u0442\u0430\u043a \u0436\u0435 \u0432\u0441\u0435\u0433\u0434\u0430 ,\u043f\u043e \u0436\u0438\u0437\u043d\u0438. \u0422\u044b \u0437\u043d\u0430\u043a\u043e\u043c\u0438\u0448\u044c\u0441\u044f ,\u043e\u0431\u0449\u0430\u0435\u0442\u0435\u0441\u044c ,\u0434\u0440\u0443\u0436\u0438\u0442\u0435 ,\u0432\u0441\u0442\u0440\u0435\u0447\u0430\u0435\u0442\u0435\u0441\u044c ,\u0430 \u043f\u043e\u0442\u043e\u043c \u0432\u0441\u0435 \u0441\u0430\u043c\u043e \u0441\u043e\u0431\u043e\u0439 \u043a\u0443\u0434\u0430 \u0442\u043e \u0434\u0435\u0432\u0430\u0435\u0442\u0441\u044f . \u0422\u0432\u043e\u044f \u043b\u0443\u0447\u0448\u0430\u044f \u043f\u043e\u0434\u0440\u0443\u0433\u0430 \u0443\u0436\u0435 \u043d\u0435 \u0442\u0432\u043e\u044f \u043f\u043e\u0434\u0440\u0443\u0433\u0430,\u0430 \u0442\u0432\u043e\u0439 \u043f\u0430\u0440\u0435\u043d\u044c \u0443\u0436\u0435 \u043d\u0435 \u0442\u0432\u043e\u0439 ,\u0442\u0432\u043e\u0438 \u0434\u0440\u0443\u0437\u044c\u044f -\u0441\u043e\u0432\u0441\u0435\u043c \u043d\u0435 \u0442\u0435 \u043b\u044e\u0434\u0438,\u0441 \u043a\u043e\u0442\u043e\u0440\u044b\u043c\u0438 \u0432\u044b \u043e\u0431\u043c\u0435\u043d\u0438\u0432\u0430\u043b\u0438\u0441\u044c \u043e\u0431\u0435\u0449\u0430\u043d\u0438\u044f\u043c\u0438 \u0434\u0440\u0443\u0436\u0438\u0442\u044c \u0432\u0435\u0447\u043d\u043e \u043d\u0438 \u0432\u0437\u0438\u0440\u0430\u044f \u043d\u0438 \u043d\u0430 \u0447\u0442\u043e. \u041e\u0431\u044a\u044f\u0441\u043d\u0438\u0442\u044c \u0441\u0430\u043c\u043e\u0439 \u0441\u0435\u0431\u0435 \u044f \u043c\u043e\u0433\u0443 \u044d\u0442\u043e \u0442\u043e\u043b\u044c\u043a\u043e \u0442\u0435\u043c,\u0447\u0442\u043e \u0440\u0430\u043d\u043e \u0438\u043b\u0438 \u043f\u043e\u0437\u0434\u043d\u043e \u043f\u0440\u0438\u0439\u0434\u0435\u0442 \u0432 \u0433\u043e\u043b\u043e\u0432\u0443 \u043a\u0430\u0436\u0434\u043e\u0433\u043e,\u0447\u0442\u043e \u043d\u0435 \u0441\u0442\u043e\u0438\u0442 \u043b\u044e\u0434\u044f\u043c \u0434\u0430\u0432\u0430\u0442\u044c \u0431\u043e\u043b\u044c\u0448\u0435,\u043d\u0435\u0436\u0435\u043b\u0438 \u043e\u043d\u0438 \u0442\u043e\u0433\u043e \u0437\u0430\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u044e\u0442 . \u0438 \u0434\u0443\u043c\u0430\u0442\u044c ,\u0447\u0442\u043e \u0432 \u0434\u0440\u0443\u0433\u043e\u043c \u043c\u0435\u0441\u0442\u0435 \u0432\u0441\u0435 \u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c\u0441\u044f \u043a \u043b\u0443\u0447\u0448\u0435\u043c\u0443 ,\u043d\u0430\u0447\u043d\u0451\u0442\u0441\u044f \u043d\u043e\u0432\u0430\u044f \u0436\u0438\u0437\u043d\u044c -\u043d\u0435 \u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c\u0441\u044f \u0438 \u043d\u0435 \u043d\u0430\u0447\u043d\u0451\u0442\u0441\u044f', u'likes': {u'count': 19416}, u'date': 1486555421, u'is_video': False, u'display_src': u'https://scontent-frt3-1.cdninstagram.com/t51.2885-15/e35/16585538_1858955610993358_247305681487527936_n.jpg?ig_cache_key=MTQ0NTY1NDExNjA5NjY5OTAyOA%3D%3D.2'}]
#     for i in data_li:
#         if i[u'is_video'] == True:
#             print i
#     print len(data_li)
#     new_data_li = [i for i in data_li if i[u'is_video'] == False]
    print 'Processing comments'
    new_data_li = [remake_dict(i) for i in data_li if i[u'is_video'] == False]
#     print len(new_data_li)
#     print new_data_li
    return new_data_li
#     print new_data_li[0].keys()
    pass


def save_data(name, output):
    """Write metadata to file
    """
    namefile = name + u'.json'
    with open(namefile, 'w') as json_file:
        data = json.dumps(output, indent=4, sort_keys=True, encoding='utf8')
        json_file.write(data)


def processing_meta(name):
    """
    Processing get metadata use Name and !save it to json-file
    """

    string_pf = workin_insta(ROOT_URL + name + SUF)
#     print '---'
#     print string_pf
    raw_data_li = remake_main_data(string_pf)
    return raw_data_li
#     save_data(name, raw_data_li)


def saving_meta(name, meta_li):
    save_data(name, meta_li)



def get_name_image(url):
    """
    Get name image from their url
    """
    name_image = url.split(u'/')[-1]
    return name_image


def create_folder(directory):
    """
    Create folder for save file
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

def dumpimage(url, name):
    """
    Downloads image to folder-name-account
    """
    file_name = get_name_image(url)
    complete_name = os.path.join(os.getcwd(), name, file_name)
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(complete_name, 'wb') as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)


def processing_images(name, meta_li):
    """
    Downloads all image from link in metadata to sub-Name folder
    """
    create_folder(name)
    print u'\nDownloading images'.encode('utf8')
    for i in meta_li:
#         print i[img-source]
        dumpimage(i['img-source'], name)
        print u'.',


def main():
    metadat_list = processing_meta(NAME)
    saving_meta(NAME, metadat_list)
    processing_images(NAME, metadat_list)

#     get_comments_from_page('aa')
#     remake_comm('a')
#     get_raw_comments_from_page('a')
#     get_post_comment('a')
#     print '==='
#     get_post_resp(ROOT_URL + NAME + SUF)
##### early - developing post comments


if __name__ == '__main__':
    main()
