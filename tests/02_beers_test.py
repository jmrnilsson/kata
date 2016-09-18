from nose.tools import assert_equal
import api


def test_beers_exists():
    actual = api.get_beers()

    assert_equal(actual, [])
