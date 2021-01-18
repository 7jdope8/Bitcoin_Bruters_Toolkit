# FROM https://github.com/LordDarkHelmet/WordListHelperScripts/blob/master/allPermutations.py
# I don't exactly know how to fork just this bit from github, so here's his credit.

# Attributes are a word list and the permutation length.
############ use eg: 
# python .\allpermutations.py -f OutputWordList.txt wordlist1.txt 3

# eg> python allpermutations.py -f scrambledseeds.txt scrambleme.txt 3
# looking for bitcoins, lists of 12,18,24 words are common


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2020 LordDarkHelmet (https://github.com/LordDarkHelmet)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import os
import sys
import argparse
import itertools
import timeit
import math

from contextlib import ExitStack
from itertools import permutations

import operator as op
from functools import reduce

def ncr(n, R):
    r = min(R, n-R)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    ret = numer / denom
    if n < R:
        ret = 0
    return ret

PY3 = sys.version_info[0] == 3
if not PY3:
    print("This program has only been tested on Python 3.6+, you are using an unknown version of python.")
    sys.exit(0)

def sizeoffile_fmt(filesize_bytes):
    for units in ['Bytes','KB','MB','GB','TB']:
        if abs(filesize_bytes) < 1024.0:
            return "%3.1f %s" % (filesize_bytes, units)
        filesize_bytes /= 1024.0
    return "%.1f %s" % (filesize_bytes, 'PB')

parser = argparse.ArgumentParser(description='generates all permutations in a word list')
parser.add_argument("-f", dest="filename", required=True, help="Destination File (where the combined list is stored)", metavar="FILENAME")
parser.add_argument('wordlist', help='The wordlist to generate all permutations', type=argparse.FileType(mode='r', encoding='utf-8'))
parser.add_argument('words', help='The length of the permutations in words', type=int)
args = parser.parse_args()

start_time = timeit.default_timer()

print('\nStarting...\n')

mylist = args.wordlist.read().splitlines()
args.wordlist.close()

if len(mylist) < args.words:
    print("WARNING, Number of items in the list is less than the permutation length. This will produce no results.")

num_permutations = ncr(len(mylist), args.words) * math.factorial(args.words)
print('Number of Permutation: {:,}'.format(num_permutations))
print('\nLoading...')

progress_count=0
next_print_percent=0
increment = num_permutations/1000
with open(args.filename, "wb") as file1:
    for group in permutations(mylist, args.words):
        file1.write((''.join(group) + '\n').encode('UTF-8'))
        progress_count += 1
        if next_print_percent <= progress_count:
            next_print_percent = min(progress_count + increment, num_permutations)
            print('Processing... [{:.1f}%]\r'.format((progress_count/num_permutations)*100), end="")

elapsed = timeit.default_timer() - start_time
print("\nNumber of items in file = {:,}".format(progress_count))
print('Execution Time: {:.4f} seconds \n'.format(elapsed))
print('Word List File: [{}] {}'.format(sizeoffile_fmt(os.stat(args.filename).st_size), args.filename))
print('Done!\n')