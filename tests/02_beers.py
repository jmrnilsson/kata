import api


def test_beers_exists():
    actual = api.get_beers()

    assert len(actual) > 100
    assert actual[0].get('Varugrupp') == u'\xd6l'
