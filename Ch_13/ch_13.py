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

