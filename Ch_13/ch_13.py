"""
Chapter 13. Data Analysis Examples

McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 
"""

import numpy as np
import pandas as pd


# 13.1 Bitly Data from 1.USA.gov

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: 

path = "../book files/datasets/bitly_usagov/example.txt"

with open(path) as f:
    print(f.readline())

# ex: converting a JSON string into a python dict

import json

with open(path) as f:
    records = [json.loads(line) for line in f]

# now the resulting obj records is now a list of python dict

records[0]

# Counting Time Zones in Pure Python

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: spose we are interestd in find the time zones that occur most often in the dataset (tz field).
# First, let's extract a list of time zones again using a list comprehension

# time_zones = [rec["tz"] for rec in records]     # spose to yield an error msg

# the reasoning is not all records have a time zone. 
# we can handle this by adding the check if "tz" in rec
# at the end of the list comprehension

time_zones = [rec["tz"] for rec in records if "tz" in rec]

time_zones[:10]

# Next, we show two ways to produce counts by time zone: the hard way (using just the python lib) and the easy way (using pandas)

# one way to do the counting is to use a dict to store counts while
# we iterate through the time zones

def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] +=1
        else:
            counts[x] = 1
    return counts

# using more advanced tools in the pythong standard lib, you can write the same thing more briefly

from collections import defaultdict
def get_counts2(sequence):
    counts = defaultdict(int) # values will initialize to 0
    for x in sequence:
        counts[x] += 1
    return counts

# the logic below makes the code more reusable. 
# to use it, just pass the time_zones list:

counts = get_counts(time_zones)

counts["America/New_York"]

len(time_zones)

# if we wanted the top 10 time zones and their counts, 
# we can make a list of tuples by (count, timezone) and sort it

def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

# results

top_counts(counts)

# if you search the python standard lib, you may find the collections.Counter class, 
# makes this task even simpler

from collections import Counter

counts = Counter(time_zones)

counts.most_common(10)  # notice the empty string with 521 observations

# Counting Time Zones with pandas

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

