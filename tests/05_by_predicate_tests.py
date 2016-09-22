import re

from nose.tools import assert_greater_equal, assert_is_not_none

from download import beers


def test_by_start_date():
    actual = beers.find_by_start('2015-05-01')[0]

    assert_greater_equal(actual['start'], '2015-04-29')


def test_by_custom_predicate_name():
    actual = beers.find_all(predicate=lambda r: re.findall('^Swe', r['name']))

    print actual
    assert_is_not_none(actual)
