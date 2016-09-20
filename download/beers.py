import requests


def find_all():
    response = requests.get('http://www.systembolaget.se/api/assortment/products/json')
    response.raise_for_status()
    json_response = response.json()
    rows = (dict(zip(json_response['columns'], row)) for row in json_response['rows'])
    return sorted(rows, key=lambda r: r['price_per_litre'])
