from nose.tools import assert_equal

from download import beers


def test_beers_exists():
    actual = list(beers.find_all())

    assert len(actual) > 100
    print 'yes, you did it!'
