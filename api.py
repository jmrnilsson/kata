import requests
from xml.etree import ElementTree


def get_beers():
    keys = ['Leverantor', 'Producent', 'Varugrupp', 'Artikelid', 'Namn', 'Namn2']
    response = requests.get('http://www.systembolaget.se/api/assortment/products/xml')
    xml = ElementTree.fromstring(response.text)
    for article in xml.findall('artikel'):
        if article.find('Varugrupp') is not None and u'\xd6l' in article.find('Varugrupp').text:
            yield {
                k: article.find(k).text for k in keys
                if article.find(k) is not None
            }
