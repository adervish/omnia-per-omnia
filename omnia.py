#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Alex Derbes on 2011-02-22.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import binascii
import random

words = []

letterMap = {}

def my_bin(t):
    str = bin(t)
    str = str.lstrip('0')
    str = str.lstrip('b')
    str = str.zfill(6)
    return str

for i in range(0, 26) :
    letterMap[my_bin(i)] = chr(i+65)
    letterMap[chr(i+65)] = my_bin(i)

for i in range(0, 10) :
    letterMap[my_bin(i+26)] = chr(i+48)
    letterMap[chr(i+48)] = my_bin(i+26)

letterMap[' '] = my_bin(36)
letterMap[my_bin(36)] = ' '

def load_words(file):
    for l in file:
        val = []
        l = l.strip()
        for c in l:
            if c == 'a':
                val.append('1')
            elif c == 'b':
                val.append('0')
        
        if len(val) > 0:
            words.append([''.join(val), l])

def encode(text):

    bin_text = ""
    cypher_words = []
    for t in text:
        bin_text += letterMap[t]

    while len(bin_text) > 0:
        random.shuffle(words)
        for w in words:
            if bin_text.startswith(w[0]):
                bin_text = bin_text.replace(w[0], '', 1)
                cypher_words.append(w[1])
    return ' '.join(cypher_words)

def decode(cypher_text):

    value = []
    for c in cypher_text:
        if c == 'a':
            value.append('1')
        elif c == 'b':
            value.append('0')
    
    for x in range(0, int(len(value) / 6)):
        key = value[x*6] + value[x*6+1] + value[x*6+2] + value[x*6+3] + value[x*6+4] + value[x*6+5]
        print letterMap[key]

if __name__ == '__main__':
    f = open(sys.argv[1], 'r')
    load_words(f)
    text = sys.argv[2]
    cypher_text = encode(text)    
    print cypher_text
    print decode(cypher_text)

