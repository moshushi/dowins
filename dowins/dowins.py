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
# NAME_ACCOUNT = "abc"
NAME_ACCOUNT = "polovinkinandrey"
# NAME_ACCOUNT = "NBA"
# NAME_ACCOUNT = "frenzytechnix"

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
    print data_li
    print type(data_li)
    print len(data_li)
    for i in data_li:
        print i
        print i[u'code']
        print type(i[u'date'])
        j = {u'date':arrow.get(i[u'date']).format('YYYY-MM-DD'), u'url':BASE_URL + BASE_SUFFIX_POST + i[u'code']}
        print j
##### u'code' - is number of page on pose



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
    process_page(BASE_URL + NAME_ACCOUNT)


if __name__ == '__main__':
    main()
