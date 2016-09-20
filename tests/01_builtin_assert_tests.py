from nose.tools import assert_equal

from download import beers


def test_beers_exists():
    actual = list(beers.find_all())

    assert len(actual) > 100
    print 'yes, you did it!'


def test_check():
    max_ = 0
    last = None
    for b in beers.find_all():
        max_ = b['price_per_litre'] if b['price_per_litre'] > max_ else max_
        last = b
    assert_equal(max_, last['price_per_litre'])
