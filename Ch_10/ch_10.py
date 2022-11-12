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

# ex:

df.groupby("key1")["data1"]
df.groupby("key1")[["data2"]]

# are conveniences for

df["data1"].groupby(df["key1"])
df[["data2"]].groupby(df["key1"])

# ex: compute the means for just the data2 col and get the result as a df

df.groupby(["key1", "key2"])[["data2"]].mean()

# ex: indexing operation returns a grouped df if a list/arr is passed OR a grouped series if a single col is passed 

s_grouped = df.groupby(["key1", "key2"])["data2"]

s_grouped

s_grouped.mean()

# Grouping with Dictionaries and Series

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: 

people = pd.DataFrame(np.random.standard_normal((5, 5)),
                      columns=["a", "b", "c", "d", "e"],
                      index=["joe", "steve", "wanda", "jill", "trey"])

people.iloc[2:3, [1,2]] = np.nan    # add a few NA values

people

# suppose i have a group correspondence for the cols and want to sum the cols by group

mapping = {"a": "red", "b": "red", "c": "blue",
           "d": "blue", "e": "red", "f": "orange"}

# here you can pass the dict, the key f won't be included which is ok as demonstrated below

by_column = people.groupby(mapping, axis="columns")

by_column.sum()

# same can be done for a series, this can be viewed as a fixed-size mapping

map_series = pd.Series(mapping)

map_series

people.groupby(map_series, axis="columns").count()

# Grouping with Functions

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: group by name length

people.groupby(len).sum()

# mixing fn with arrays, dict, or series is not a problem. everything gets converted to arrays internally

key_list = ["one", "one", "one", "two", "two"]

people.groupby([len, key_list]).min()

# Grouping by Index Levels

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: aggregate using one of the levels of an axis index of hierarchically indexed datasets

columns = pd.MultiIndex.from_arrays([["us", "us", "us", "jp", "jp"],
                                    [1, 3, 5, 1, 3]],
                                    names=["cty", "tenor"])

hier_df = pd.DataFrame(np.random.standard_normal((4, 5)), columns=columns)

hier_df     # very cool 

# to group by level, pass the level number or name using the level keyword:

hier_df.groupby(level="cty", axis="columns").count()

# 10.2 Data Aggregation

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# table 10-1. Optimized groupby methods

# ex: 

df 

grouped = df.groupby("key1")

grouped["data1"].nsmallest(2)

# ex: to use your own aggregation functions, pass a fn that agg an arr to the agg method

def peak_to_peak(arr):
    return arr.max() - arr.min()

grouped.agg(peak_to_peak)

# ex: THE ALL IMPORTANT DESCRIBE METHOD

grouped.describe()

# Column-Wise and Multiple Function Application

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

tips = pd.read_csv("../book files/examples/tips.csv")

tips.head()

# now add a tip_pct col with the tip % of the total bill

tips["tip_pct"] = tips["tip"] / tips["total_bill"]  # this is how you add another col to the df

tips.head()

# ex: group the tips by day and smoker

grouped = tips.groupby(["day", "smoker"])

grouped_pct = grouped["tip_pct"]

grouped_pct.agg("mean")

# if you pass a list of fn's or fn names instead, you get back a df w/ col names taken from the fn

grouped_pct.agg(["mean", "std", peak_to_peak])

grouped_pct.agg([("average", "mean"), ("stdev", np.std)])

# df's have more options. To start, suppose we wanted to compute the same 3 statistics for tip_pct and total_bill

functions = ["count", "mean", "max"]

result = grouped[["tip_pct", "total_bill"]].agg(functions)  # this is very dope

result

result["tip_pct"]   # you have to get accustomed to using this syntax in python like u did R

# ex: a list of tuples with custom names can be passed:

ftuples = [("Average", "mean"), ("Variance", np.var)]

grouped[["tip_pct", "total_bill"]].agg(ftuples)

# ex: suppose you wanted to apply diff fn's to 1 or more cols. To do, pass a dict to agg that contains
# a mapping of col names to any of the fun specifications listed so far:

grouped.agg({"tip": np.max, "size": "sum"})

grouped.agg({"tip_pct": ["min", "max", "mean", "std"],
            "size": "sum"})

# Returning Aggregated Data Without Row Indexes

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

tips.groupby(["day", "smoker"], as_index=False).mean()  # use as_index=False to avoid unnecessary things

# 10.3 Apply: General split-apply-combine

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# the most general-purpose groupby method is apply. 

"""
apply splits the object being manipulated into pieces, 

invokes the passed function on each piece, 

and then attempts to concatenate the pieces.

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 
"""

# ex: suppose you wanted to select the top five tip_pct values by group

# first, write a fun that selects the rows w/ the max values in some col

def top(df, n=5, column="tip_pct"):
    return df.sort_values(column, ascending=False)[:n]

top(tips, n=6)

# Now, if we group by smoker, & call apply w/ this fn. we get the following:

tips.groupby("smoker").apply(top)

# if apply takes other args or keywords, pass them after the fn

tips.groupby(["smoker", "day"]).apply(top, n=1, colummn="total_bill")

# ex: describe method

result = tips.groupby("smoker")["tip_pct"].describe()

result  # very nice table

result.unstack("smoker")

# Suppressing the Group Keys

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

