#!/usr/bin/env python
from codecs import open
import json
import re
import os
from xml.etree import ElementTree


def make_json():
    map_ = {
        'Producent': ['manufacturer', unicode],
        'Artikelid': ['id', unicode],
        'Namn': ['name', unicode],
        'Namn2': ['name_2', unicode],
        'Prisinklmoms': ['price', float],
        'PrisPerLiter': ['price_per_litre', float],
        'Alkoholhalt': ['abv', lambda value: float(re.match('[0-9\.]*', value).group(0))],
        'Saljstart': ['start', unicode]
    }

    keys = map_.keys()

    with open(os.path.dirname(os.path.abspath(__file__)) + '/sb.xml', encoding='utf-8') as fp:
        xml = ElementTree.fromstring(fp.read().encode('utf-8'))

        rows = sorted(
            [
                {
                    map_[k][0]: map_[k][1](article.find(k).text) for k in keys
                    if article.find(k) is not None
                }
                for article in xml.findall('artikel')
                if article.find('Varugrupp') is not None and
                u'\xd6l' in article.find('Varugrupp').text
            ], key=lambda r: r['price_per_litre']
        )

        columns = [map_[k][0] for k in keys]
        rows = [[row.get(k) for k in columns] for row in rows]

    with open('sb_.json', 'w', 'utf-8') as outfile:
        return json.dump(dict(columns=columns, rows=rows), outfile, ensure_ascii=False)


if __name__ == '__main__':
    make_json()
