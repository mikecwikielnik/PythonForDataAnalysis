'''
Chapter 5. Getting Started with pandas

McKinney, Wes. Python for Data Analysis (p. 206). O'Reilly Media. Kindle Edition. 
'''

'''
5.1 Introduction to pandas Data Structures

McKinney, Wes. Python for Data Analysis (p. 207). O'Reilly Media. Kindle Edition. 
'''
import numpy as np

import pandas as pd 

from pandas import Series, DataFrame

# Series

# simplest form of a Series

obj = pd.Series([4, 7, -5, 3])

obj

# Get the array attributes and index attributes, respectively

obj.array

obj.index

# Create a Series with a matching index label

obj2 = pd.Series([4, 7, -5, 3], index=["d", "b", "a", "c"])

obj2

obj2.index

# You can use labels in the index when selecting single values or a set of values:

obj2["a"]

obj2["d"] = 6

obj2[["c", "a", "d"]]

# Using Numpy functions or Numpy-like operations, will preserve the index-value link:

obj2[obj2 > 0]

obj2 * 2

import numpy as np

np.exp(obj2)

# ex:

"b" in obj2

"e" in obj2

# ex: should you have a python dictionary, you can create a Series from it by passing the dictionary

sdata = {"Ohio": 35, "Texas": 1000, "Oregon": 160, "Utah": 75}

obj3 = pd.Series(sdata)

obj3    # this should be second nature

obj3.to_dict()  # A Series back to a dictionary

# You can override the default key insertion order by passing a desired index

states = ["California", "Ohio", "Oregon", "Texas"]

obj4 = pd.Series(sdata, index=states)

obj4

# check for NaNs

pd.isna(obj4)

pd.notna(obj4)

# Series can also check for NaNs too

obj4.isna()

# arithmetic operations

obj3 + obj4

# name attribute

obj4.name = "population"

obj4.index.name = "state"

obj4

# A Series index can be altered in place by assignment

obj

obj.index = ["bob", "steve", "jeff", "ryan"]

obj

# DataFrame

# McKinney, Wes. Python for Data Analysis (p. 215). O'Reilly Media. Kindle Edition. 

