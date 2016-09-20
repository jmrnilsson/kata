#!/usr/bin/env python
import os
from codecs import open
import json


def make_json():
    with open(os.path.dirname(os.path.abspath(__file__)) + '/sb_.json', encoding='utf-8') as fp:
        data = json.loads(fp.read().encode('utf-8'))
        return json.dumps(data, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    print make_json()
