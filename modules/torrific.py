import urllib2
from urllib2 import HTTPError
from urlparse import urlparse
from optparse import OptionParser
from ipaddress import ip_address, AddressValueError
import shlex
import subprocess
import getpass

PROXY_TYPE_HTTP = "http"
PROXY_TYPE_SOCKS = "socks5"

PROXY_VALID_SCHEMES = {"http", "socks5", "socks4", "socks4a"}

# holds session data
torrific_session = None

input_text = """
You are trying to fetch from a url, but you are not using a http Proxy.
This may leak your position throught DNS name resolving. Do you want to proceed?
[y/N]
"""


class TorrificData(object):

    def __init__(self):
        # module vars
        self.module_initialized = False
        self.proxy_support = None
        self.url_opener = None
        self.proxy_url = None
        self.proxy_type = None


def usage():
    print "torrific.py -p http://127.0.0.1:8118 -u www.example.com"


def initialize(proxy_url):

    global torrific_session

    # verify proxy.
    proxy_data = urlparse(proxy_url)

    if proxy_data is None:
        print "Invalid proxy!"
        print options.proxy.help
        exit(-1)

    if proxy_data.scheme is None or proxy_data.scheme not in PROXY_VALID_SCHEMES:
        print "Invalid proxy scheme!"
        exit(-1)

    if proxy_data.port is None:
        print "Please specify proxy port."
        exit(-1)

    torrific_session = TorrificData()

    torrific_session.proxy_url = proxy_data.netloc
    torrific_session.proxy_type = proxy_data.scheme
    torrific_session.proxy_support = urllib2.ProxyHandler({proxy_data.scheme: proxy_data.netloc})
    torrific_session.url_opener = urllib2.build_opener(torrific_session.proxy_support)
    torrific_session.module_initialized = True

    # all done! :)


def get_url_data(url):

    global torrific_session, input_text

    # guarantees that its using the opener...
    urllib2.install_opener(torrific_session.url_opener)

    url_data = urlparse(url)

    # check its is an ip or url to be resolved
    try:
        ip = ip_address(url_data.netloc)
    except AddressValueError as err:
        # seems we have a name
        if torrific_session.proxy_type != "http":
            answer = raw_input(input_text)

            if answer != "y":
                exit(-1)

    # fetch data
    try:
        ret = urllib2.urlopen(url).read()
        return ret
    except HTTPError as e:
        print e.code
        return -1


def create_tunnel():
    pass


if __name__ == '__main__':

    # command line parser
    cmd_parser = OptionParser()
    cmd_parser.add_option("-p", "--proxy", dest="proxy",
                          help="Proxy eg.: socks://127.0.0.1:9050,"
                                " http://127.0.0.1:8118 ...")

    cmd_parser.add_option("-u", "--url", dest="url", help="Url to fetch data")

    (options, args) = cmd_parser.parse_args()

    # initialize torrific.
    initialize(options.proxy)

    # finally
    data = get_url_data(options.url)
    if data == -1:
        exit(-1)

    print data




