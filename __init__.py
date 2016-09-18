import requests
import re
from codecs import open
from mock import Mock

__get = requests.get

'''
http://www.systembolaget.se/api/assortment/products/xml
'''


def get(*args, **kwargs):
    url = next(iter(args[:1]), **kwargs.get('url'))
    if url and re.match('systembolaget', url):
        return Mock(content=open(os.path.dirname(os.path.abspath(__file__)) + '/sb.xml'))
    return requests.get(*args, **kwargs)
