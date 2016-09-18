import requests
import re
from mock import Mock
import os

__get = requests.get


'''
http://www.systembolaget.se/api/assortment/products/xml
'''


def get(*args, **kwargs):
    url = args[0] if args else kwargs.get('url')
    if url and re.findall('systembolaget', url):
        print 'intercepted request'
        with open(os.path.dirname(os.path.abspath(__file__)) + '/sb.xml', 'rb') as fp:
            return Mock(text=fp.read())
    raise NotImplementedError()
    # return __get(*args, **kwargs)

requests.get = get
