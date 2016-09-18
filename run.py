#!/usr/bin/env python
import json
from codecs import open

from download import api

if __name__ == '__main__':
    beers = list(api.get_beers())

    # with open('sb.json', 'w', 'utf-8') as outfile:
    #    json.dump(beers, outfile, indent=2, ensure_ascii=False)

    print json.dumps(beers, indent=2, ensure_ascii=False)
