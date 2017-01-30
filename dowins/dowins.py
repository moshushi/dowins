# -*- encoding: utf-8 -*-
"""
Script downloads and wrap foto and metainformation from INSTARGAM
Prototype
"""

import requests
import json
from bs4 import BeautifulSoup
from ast import literal_eval

BASE_URL = "https://www.instagram.com/"
# NAME_ACCOUNT = "abc"
NAME_ACCOUNT = "polovinkinandrey"
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
    profile_page = obj[u'entry_data']
    page_content = profile_page[u'ProfilePage'][0]
    print page_content


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
