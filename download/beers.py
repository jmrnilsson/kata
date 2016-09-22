import requests


def find_all(predicate=lambda r: True):
    response = requests.get('http://www._.se/api/assortment/products/json')
    response.raise_for_status()
    json_response = response.json()
    rows = (dict(zip(json_response['columns'], row)) for row in json_response['rows'])
    return sorted(filter(predicate, rows), key=lambda r: r['price_per_litre'])


def find_by_start(start):
    return find_all(predicate=lambda r: r['start'] >= start)
