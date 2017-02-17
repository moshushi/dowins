import requests
import logging

# Examnle from
# http://stackoverflow.com/questions/10588644/how-can-i-see-the-entire-http-request-thats-being-sent-by-my-python-application
# These two lines enable debugging at httplib level (requests->urllib3->http.client)
# You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# The only thing missing will be the response.body which is not logged.
try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
http_client.HTTPConnection.debuglevel = 1

# You must initialize logging, otherwise you'll not see debug output.
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

# requests.get('https://httpbin.org/headers')
# d = requests.get(u'https://www.instagram.com/sa.ny.aa/?__a=1')
# print d.text

def main():
    with requests.Session() as s:
        reqg = requests.Request('GET', u'https://www.instagram.com/sa.ny.aa/?__a=1')
        prepared = reqg.prepare()
#         pretty_print_POST(prepared)
        resp = s.send(prepared)


if __name__ == '__main__':
    main()
