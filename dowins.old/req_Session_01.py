# -*- encoding: utf-8 -*-
"""
Example print http raw
http://stackoverflow.com/questions/20658572/python-requests-print-entire-http-request-raw
"""

import json
from requests import Request, Session

ROOT_URL = u'https://www.instagram.com/'
QUERY_URL = u'https://www.instagram.com/query/'
SUF = u'?__a=1'
NAME_ACCOUNT = u'sa.ny.aa'




def process_page(string):
    """
    Pretty view result
    """
    obj = json.loads(string)
    print json.dumps(obj, indent=4, sort_keys=True)

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


def main():
    with Session() as s:
        reqg = Request('GET', u'https://www.instagram.com/sa.ny.aa/?__a=1')
        prepared = reqg.prepare()
        pretty_print_POST(prepared)
        resp = s.send(prepared)
        print '----'
        print resp.request.headers
#         process_page(reqg.text)



if __name__ == '__main__':
    main()
