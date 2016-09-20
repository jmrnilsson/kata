import os
from codecs import open
import json

from mock import Mock
from nose.tools import assert_equal, assert_less
import requests

from download import beers

__get = requests.get


def setup():
    with open(os.path.dirname(os.path.abspath(__file__)) + '/../sb_.json', encoding='utf-8') as fp:
        rows = json.loads(fp.read().encode('utf-8'))
        requests.get = Mock(return_value=Mock(json=Mock(return_value=rows)))


def teardown():
    requests.get = __get


def test_beers_in_asc_order_by_price():
    max_ = 0
    last = None
    for b in beers.find_all():
        max_ = b['price_per_litre'] if b['price_per_litre'] > max_ else max_
        last = b
    assert_equal(max_, last['price_per_litre'])


def test_ensure_lower_priced_come_first():
    actual = map(lambda r: r['price_per_litre'], beers.find_all())
    yield assert_less, actual[0], actual[1]
    yield assert_less, actual[200], actual[202]
    yield assert_less, actual[999], actual[1005]
