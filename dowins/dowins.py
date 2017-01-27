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

def parse(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
#     print soup

    list_of_script = soup.findAll(name="script", type='text/javascript')
#     print list_of_script[0]
#     dt = list_of_script[4]
#     data = json.loads(dt.text)
    print list_of_script[4].prettify()
#     some_script = soup.find(name="script", type='text/javascript', text='_sharedData')
    some_script = soup.find(name="script", type='text/javascript')
#     print some_script.text
    print '----'
    for i in list_of_script:
        if '_sharedData' in i.text:
            print i.text
#     return soup

#     data = soup.find('script', type='text/javascript')
#     print data

def process_page(url):
    html = get_html(url)
    data = parse(html)
#     print data

def main():
    process_page(BASE_URL + NAME_ACCOUNT)


if __name__ == '__main__':
    main()
