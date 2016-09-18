import requests
import os
from codecs import open

from mock import Mock


with open(os.path.dirname(os.path.abspath(__file__)) + '/../sb.xml', encoding='utf-8') as fp:
    requests.get = Mock(return_value=Mock(text=fp.read()))
