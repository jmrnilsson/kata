import requests
import re
from xml.etree import ElementTree


def get_beers():
    map_ = {
        'Leverantor': unicode,
        'Producent': unicode,
        'Varugrupp': unicode,
        'Artikelid': unicode,
        'Namn': unicode,
        'Namn2': unicode,
        'Prisinklmoms': float,
        'PrisPerLiter': float,
        'Alkoholhalt': lambda value: float(re.findall('[0-9\.]*', value)[0]),

    }
    response = requests.get('http://www.systembolaget.se/api/assortment/products/xml')
    xml = ElementTree.fromstring(response.text.encode('utf-8'))

    return iter(sorted([
        {
            k: convert(article.find(k).text) for k, convert in map_.iteritems()
            if article.find(k) is not None
        }
        for article in xml.findall('artikel')
        if article.find('Varugrupp') is not None and u'\xd6l' in article.find('Varugrupp').text
    ], key=lambda row: row['PrisPerLiter']))
