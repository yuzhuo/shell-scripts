#!/bin/env python
#-*- coding: utf8 -*-

import sys
import random
import os


with open(sys.argv[1]) as f:
    data = f.readlines()
    length = len(data)

    filename = os.path.basename(sys.argv[1]) + ".rand" + sys.argv[2]
    all = []
    wf = open(filename, "w")
    for i in xrange(int(sys.argv[2])):
        rand_line =  random.randint(0, length - 1)
        #print rand_line
        while rand_line in all:
            rand_line =  random.randint(0, length - 1)
        all.append(rand_line)
        wf.write(data[rand_line])
    wf.close()

