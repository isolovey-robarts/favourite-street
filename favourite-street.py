#!/usr/bin/env python3

import csv
import sys

with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if linecount > 0:
        print("{}'s favourite street is {}.".format(row[1],row[2]))

print('Done.')
