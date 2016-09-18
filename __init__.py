import requests
import os
from codecs import open

from mock import Mock

'''
http://www.systembolaget.se/api/assortment/products/xml
__get = requests.get
def get(*args, **kwargs):
    url = args[0] if args else kwargs.get('url')
    if url and re.findall('systembolaget', url):
    raise NotImplementedError()
'''

with open(os.path.dirname(os.path.abspath(__file__)) + '/sb.xml', encoding='utf-8') as fp:
    requests.get = Mock(return_value=Mock(text=fp.read().encode('utf-8')))
