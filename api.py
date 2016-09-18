import requests
from xml.etree import ElementTree


def get_beers():
    keys = ['Leverantor', 'Producent', 'Varugrupp', 'Artikelid', 'Namn', 'Namn2']
    xml = ElementTree.parse(requests.get('http://www.systembolaget.se/api/assortment/products/xml'))
    for article in xml.findall('artikel'):
        if article.find('Varugrupp') is not None and u'\xd6l' in article.find('Varugrupp').text:
            return {el: el.text for el in article.iteritems() if el in keys}
