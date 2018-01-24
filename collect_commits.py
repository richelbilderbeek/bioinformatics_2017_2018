#!/usr/bin/env python

# Creates a list with
# [username], [commits]

import json
data = json.load(open('contributors'))

for i in range(0, len(data)):
  print(str(data[i]['author']['login']) + ',' + str(data[i]['total']))