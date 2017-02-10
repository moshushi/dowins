# -*- encoding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

BASE_URL = u'https://www.instagram.com/'
NAME_ACCOUNT = u"frenzytechnix"
# MORE_CONTROLL = u'/frenzytechnix/?max_id=1368997542565559884'
QUERY = u'query'


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
    print response.status_code
    return response.text

def mod_get_data(html_doc):

    soup = BeautifulSoup(html_doc, 'html.parser')
    print soup.prettify().encode('utf-8')


def main():
    pass

if __name__ == '__main__':
    main()
