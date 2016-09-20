from nose.tools import assert_greater

from download import beers


def test_order_by_start_date():
    actual = beers.find_by_start('2016-05-01')[0]

    assert_greater(actual, '2016-04-29')
