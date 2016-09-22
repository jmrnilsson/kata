import os
import json
from codecs import open

from mock import Mock
import requests

__get = requests.get


def setup_module():
    with open(os.path.dirname(os.path.abspath(__file__)) + '/../sb_.json', encoding='utf-8') as fp:
        rows = json.loads(fp.read().encode('utf-8'))
        requests.get = Mock(return_value=Mock(json=Mock(return_value=rows)))


def teardown_module():
    requests.get = __get
