from nose.tools import assert_equal, assert_is_not_none
from mock import patch

from download import beers


def test_side_effect_with_list():
    with patch.object(beers, 'find_all', side_effect=[0, 1, {'something': True}]):
        beers.find_all()
        assert_equal(beers.find_all.call_count, 1)

        b = beers.find_all()
        assert_equal(b, 1)
        assert_is_not_none(beers.find_all())
        assert_equal(beers.find_all.call_count, 3)
