#!/bin/env python
#-*- coding: utf8 -*-


import os
import sys
import csv
import codecs


w_filename = os.path.basename(sys.argv[1]) + ".csv"
wf = open(w_filename, "wb")
wf.write(codecs.BOM_UTF8)
csv_w = csv.writer(wf, dialect="excel")
csv_w.writerow([1,1,1])
csv_w.writerow([2,2])
wf.close()
