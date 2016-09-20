#!/usr/bin/env python
import json

from download import beers

if __name__ == '__main__':
    beers = list(beers.find_all())
    print json.dumps(beers, indent=2, ensure_ascii=False)
