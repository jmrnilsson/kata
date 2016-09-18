import os
import requests
from download import api
from codecs import open
from mock import Mock
from nose.tools import assert_greater, assert_equal, assert_less

__get = requests.get


def setup():
    with open(os.path.dirname(os.path.abspath(__file__)) + '/../sb.xml', encoding='utf-8') as fp:
        requests.get = Mock(return_value=Mock(text=fp.read()))


def teardown():
    requests.get = __get


def test_beers_exists():
    actual = list(api.get_beers())

    assert_greater(len(actual), 100)
    assert_equal(actual[0]['Varugrupp'], u'\xd6l')


def test_beers_in_asc_order_by_price():
    max_ = 0
    last = None
    for b in api.get_beers():
        max_ = b['PrisPerLiter'] if b['PrisPerLiter'] > max_ else max_
        last = b
    assert_equal(max_, last['PrisPerLiter'])


def test_ensure_lower_priced_come_first():
    actual = list(api.get_beers())
    yield assert_less_, actual, 'PrisPerLiter', 0, 2
    yield assert_less_, actual, 'PrisPerLiter', 11, 200
    yield assert_less_, actual, 'PrisPerLiter', 999, 1000


def assert_less_(actual, key, idx, idx_2):
    assert_less(actual[idx][key], actual[idx_2][key])
