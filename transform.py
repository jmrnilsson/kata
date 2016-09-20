#!/usr/bin/env python
from codecs import open
import json
import re
import os
from xml.etree import ElementTree


def make_json():
    __map = {
        'supplier': 'Leverantor',
        'id': 'Artikelid',
        'name': 'Namn',
        'name2': 'Namn2',
        'price': 'Prisinklmoms',
        'price_per_litre': 'PrisPerLiter',
        'abv': 'Alkoholhalt'
    }
    beers = list(get_xml())

    with open('sb_.json', 'w', 'utf-8') as outfile:
        columns = __map.keys()
        rows = [
            [
                beer.get(__map[k]) for k in columns
            ] for beer in beers
        ]
        json.dump({'columns': columns, 'rows': rows}, outfile, ensure_ascii=False)


def get_xml():
    map_ = {
        'Leverantor': unicode,
        'Producent': unicode,
        'Varugrupp': unicode,
        'Artikelid': unicode,
        'Namn': unicode,
        'Namn2': unicode,
        'Prisinklmoms': float,
        'PrisPerLiter': float,
        'Alkoholhalt': lambda value: float(re.match('[0-9\.]*', value).group(0))
    }

    with open(os.path.dirname(os.path.abspath(__file__)) + '/sb.xml', encoding='utf-8') as fp:
        xml = ElementTree.fromstring(fp.read().encode('utf-8'))

        return sorted(
            [
                {
                    k: convert(article.find(k).text) for k, convert in
                    map_.iteritems()
                    if article.find(k) is not None
                }
                for article in xml.findall('artikel')
                if article.find('Varugrupp') is not None and u'\xd6l'
                in article.find('Varugrupp').text
            ], key=lambda row: row['PrisPerLiter'])


if __name__ == '__main__':
    make_json()
