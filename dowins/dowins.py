# -*- encoding: utf-8 -*-
"""
Script downloads and wrap foto and metainformation from INSTARGAM
Prototype
"""

import requests
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
    return soup

def process_page(url):
    html = get_html(url)
    data = parse(html)
    print data

def main():
    process_page(BASE_URL + NAME_ACCOUNT)


if __name__ == '__main__':
    main()
