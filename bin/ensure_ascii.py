#!/bin/env python
#-*- coding: utf8 -*-

import sys
import json

with open(sys.argv[1]) as f:
    for l in f:
        if l.strip():
            d = json.loads(l)
            print json.dumps(d, ensure_ascii=False).encode('utf8')
