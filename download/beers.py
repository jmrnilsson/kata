import requests


def find_all():
    response = requests.get('http://www.systembolaget.se/api/assortment/products/json')
    response.raise_for_status()
    json_response = response.json()
    return (dict(zip(json_response['columns'], row)) for row in json_response['rows'])
