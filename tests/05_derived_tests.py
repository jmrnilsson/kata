from nose.tools import assert_greater_equal

from download import beers


def test_order_by_start_date():
    actual = beers.find_by_start('2015-05-01')[0]

    assert_greater_equal(actual['start'], '2015-04-29')
