#!/usr/bin/env python
import json

from download import api

if __name__ == '__main__':
    beers = list(api.get_beers())
    print json.dumps(beers, indent=2, ensure_ascii=False)
