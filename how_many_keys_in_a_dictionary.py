#! /usr/bin/python3
# -*- coding: utf-8 -*-
#
# How many entries can be stuffed into a dictionary?

import random

ctr = 0
d = dict()
try:
    while True:
        d[0] = random.randint(0, 0x7FFFFFFF)
        ctr += 1
except Exception as e:
    print("Counter is ", ctr)
    print("exception is ", str(e))
    raise
