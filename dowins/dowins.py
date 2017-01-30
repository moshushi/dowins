# -*- encoding: utf-8 -*-
"""
Script downloads and wrap foto and metainformation from INSTARGAM
Prototype
"""

import requests
import json
from bs4 import BeautifulSoup

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

def get_dict_from_html(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')

    list_of_script = soup.findAll(name="script", type='text/javascript')
    for i in list_of_script:
        if '_sharedData' in i.text:
#             print i.text
            cutter =  i.text.find('=') + 2
#             print cutter
            print i.text[cutter:]
            return i.text[cutter:]

def parse(uni_row):
#     print string
#     print dict_row["media"]
    pass

def process_page(url):
    html = get_html(url)
    dict_row = get_dict_from_html(html)
#     data = parse(dict_row)
#     print '===='
#     print dagajs.decode('utf-8').encode('cp1251')
#     print data

def main():
    process_page(BASE_URL + NAME_ACCOUNT)


if __name__ == '__main__':
    main()
