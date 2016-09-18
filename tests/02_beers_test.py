import os
import requests
from download import api
from codecs import open
from mock import Mock
from nose.tools import assert_greater, assert_equal, with_setup

__get = requests.get


def setup_function():
    with open(os.path.dirname(os.path.abspath(__file__)) + '/../sb.xml', encoding='utf-8') as fp:
        requests.get = Mock(return_value=Mock(text=fp.read()))


def teardown_function():
    requests.get = __get


@with_setup(setup_function, teardown_function)
def test_beers_exists():
    actual = list(api.get_beers())

    assert_greater(len(actual), 100)
    assert_equal(actual[0]['Varugrupp'], u'\xd6l')


@with_setup(setup_function, teardown_function)
def test_fixture_setup_for_module():
    list(api.get_beers())
    assert_equal(requests.get.call_count, 2)
