'''
Chapter 10. Data Aggregation and Group Operations

McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 
'''

import numpy as np
import pandas as pd

# 10.1 How to Think About Group Operations

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# SPLIT-APPLY-COMBINE

# ex: 

df = pd.DataFrame({"key1": ["a", "a", None, "b", "b", "a", None],
                   "key2": pd.Series([1, 2, 1, 2, 1, None, 1], dtype="Int64"),
                   "data1": np.random.standard_normal(7),
                   "data2": np.random.standard_normal(7)})

df

# Suppose you want to compute the mean of data1 col using labels from key1
# there are a number of ways to do it. One is to access data1 and call groupby w/ the col (a series) at key1:

grouped = df["data1"].groupby(df["key1"])

grouped

# ex: compute group means. we use groupby's mean method

grouped.mean()  # look at line 23. here we have the mean of each group in "key1"

# if instead we had passed multiple arrays as a list, we'd get something different

means = df["data1"].groupby([df["key1"], df["key2"]]).mean()

means

# above, we grouped the data using two keys, & now the resulting series now has a hierarchical index consisting of unique pairs

means.unstack()

# ex: the group keys are all series, tho they could be any arrays of the right length

states = np.array(["OH", "CA", "CA", "OH", "OH", "CA", "OH"])

years = [2005, 2005, 2006, 2005, 2006, 2005, 2006]

df["data1"].groupby([states, years]).mean()

# pass column names as the group keys

df.groupby("key1").mean()

df.groupby("key2").mean()

df.groupby(["key1", "key2"]).mean()

# ex: a useful groupby method is size, returns a series

df.groupby(["key1", "key2"]).size()

# ex: missing values are dropped by default. This can be disabled by passing dropna=False to groupby

df.groupby("key1", dropna=False).size()

df.groupby(["key1", "key2"], dropna=False).size()

# ex: count computes the # of nonnull values in each group

df.groupby("key2").count()

df  # do the groupby().count() or groupby().size() with ur finger, it helps with the abstractness

# Iterating over Groups

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: 

for name, group in df.groupby("key1"):
    print(name)
    print(group)

# in case of multiple keys, the first element in the tuple will be a tuple of keys

for (k1, k2), group in df.groupby(["key1", "key2"]):
    print((k1, k2))
    print(group)

# a useful thing to do is computing a dict of the data pieces as a one-liner

pieces = {name: group for name, group in df.groupby("key1")}

pieces["b"]

# ex: groupby some axis

grouped = df.groupby({"key1": "key", "key2": "key",
                      "data1": "data", "data2": "data"}, axis="columns")

# we cn print out the groups like so:

for group_key, group_values in grouped:
    print(group_key)
    print(group_values)

# Selecting a Column or Subset of Columns

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

