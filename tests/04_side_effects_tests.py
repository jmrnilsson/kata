from nose.tools import assert_equal, assert_is_not_none
from mock import Mock

from download import beers


def test_side_effect_with_list():
    beers.find_all = Mock(side_effect=[0, 1, {'something': True}])
    beers.find_all()
    assert_equal(beers.find_all.call_count, 1)

    beers.find_all()
    assert_is_not_none(beers.find_all())
    assert_equal(beers.find_all.call_count, 3)
