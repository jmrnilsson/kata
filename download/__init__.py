import requests
import os
from codecs import open
import json

from mock import Mock

with open(os.path.dirname(os.path.abspath(__file__)) + '/../sb_.json', encoding='utf-8') as fp:
    rows = json.loads(fp.read().encode('utf-8'))
    requests.get = Mock(return_value=Mock(json=Mock(return_value=rows)))
