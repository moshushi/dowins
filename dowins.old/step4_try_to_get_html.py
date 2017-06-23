# -*- encoding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

BASE_URL = u'https://www.instagram.com/'
NAME_ACCOUNT = u"frenzytechnix"
# MORE_CONTROLL = u'/frenzytechnix/?max_id=1368997542565559884'
QUERY = u'query'


# def get_html(url, cookies=None):
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
    return (response.text, response.cookies)

def mod_get_data(html_doc):

    soup = BeautifulSoup(html_doc, 'html.parser')
    print soup.prettify().encode('utf-8')

def get_html_more(url, cookies):
#     response = requests.post(BASE_URL + NAME_ACCOUNT)
    response = requests.post(url, cookies=cookies)
    print response.status_code
#     print response.text.encode('utf-8')
    return response.text


def main():
    (html, cook) = get_html(BASE_URL + NAME_ACCOUNT)
    mod_get_data(html)
    print '=============================='
    print 'helllo'
    html2 = get_html_more(u'https://www.instagram.com/query/', cookies = cook)
    mod_get_data(html2)
    pass

if __name__ == '__main__':
    main()
