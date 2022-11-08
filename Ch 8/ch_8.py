'''
Chapter 8. Data Wrangling: Join, Combine, and Reshape

McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 
'''

# hierarchical indexing in pandas

# 8.1 Hierarchical Indexing

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

import pandas as pd

import numpy as np

# ex: create a Series with a list of lists(or arrays) as the index:

data = pd.Series(np.random.uniform(size=9),
                index=[["a", "a", "a", "b", "b", "c", "c", "d", "d"],
                        [1, 2, 3, 1, 3, 1, 2, 2, 3]])

data

# ex: multi-index

data.index

# ex: partial indexing enables you to concisely select subsets of the data

data["b"]

data["b":"c"]   # b through c

data.loc[["b", "d"]]    # specifically, b & d

# ex: selecting all values having the value 2 from the second index level

data.loc[:,2]   # anything element with 2 as an index!

# ex: unstack method

data.unstack()  # this method brings the object into a matrix

data    # original data view

# the inverse is easy

data.unstack().stack()

# ex: In a df, either axis can have a hierarchical index

frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
                    index=[["a", "a", "b", "b"], [1, 2, 1, 2]],
                    columns=[["ohio", "ohio", "colorado"],
                            ["green", "red", "green"]])

frame

# how many levels an index has?

frame.index.nlevels

# ex: partial column indexing, you can similarly select groups of columns

frame["ohio"]

# Reordering and Sorting Levels

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: swaplevel method 

frame.index.names = ["key1", "key2"]

frame.columns.names = ["state", "color"]

frame.swaplevel("key1", "key2")

# ex: sort_index by default sorts the data lexicographically 

frame

frame.sort_index(level=1)

frame.swaplevel(0, 1).sort_index(level=0)   # this is important. it just swaps the keys

# Summary Statistics by Level

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: you can run descriptive & summary stats on a df, series at a specific level on a specific axis

frame.groupby(level="key2").sum()       # could be important

frame.groupby(level="color", axis="columns").sum()

# Indexing with a DataFrame’s columns

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: 

frame = pd.DataFrame({"a": range(7), "b": range(7, 0, -1),
                        "c": ["one", "one", "one", "two", "two",
                                "two", "two"],
                        "d": [0, 1, 2, 0, 1, 2, 3]})

frame

# ex: set_index takes a new df using one or more of its columns as the index

frame2 = frame.set_index(["c", "d"])

frame2

# the indexed cols are removed by default, they can be kept though

# ex:

frame.set_index(["c", "d"], drop=False)

# ex: reset_index() 

frame2.reset_index()

# 8.2 Combining and Merging Datasets

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# Database-Style DataFrame Joins

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex:

df1 = pd.DataFrame({"key": ["b", "b", "a", "c", "a", "a", "b"],
                        "data1": pd.Series(range(7), dtype="Int64")})

df2 = pd.DataFrame({"key": ["a", "b", "d"],
                        "data2": pd.Series(range(3), dtype="Int64")})

df1

df2

# ex: a many-to-one join

pd.merge(df1, df2)

# practice specifying column names

pd.merge(df1, df2, on="key")

# ex: you can specify column names separately, even if they are different

df3 = pd.DataFrame({"lkey": ["b", "b", "a", "c", "a", "a", "b"],
                        "data1": pd.Series(range(7), dtype="Int64")})

df4 = pd.DataFrame({"rkey": ["a", "b", "c"],
                        "data2": pd.Series(range(3), dtype="Int64")})

pd.merge(df3, df4, left_on="lkey", right_on="rkey")

# ex: outer join

pd.merge(df1, df2, how="outer")

pd.merge(df3, df4, left_on="lkey", right_on="rkey", how="outer")

# ex: many to many merges form the cartesian product of the matching keys

df1 = pd.DataFrame({"key": ["b", "b", "a", "c", "a", "b"],
                        "data1": pd.Series(range(6), dtype="Int64")})

df2 = pd.DataFrame({"key": ["a", "b", "a", "b", "d"],
                        "data2": pd.Series(range(5), dtype="Int64")})

df1

df2

pd.merge(df1, df2, on="key", how="left")

# ex: to merge multiple keys, pass a list of column names:

left = pd.DataFrame({"key1": ["foo", "foo", "bar"],
                        "key2": ["one", "two", "one"],
                        "lval": pd.Series([1, 2, 3], dtype='Int64')})

right = pd.DataFrame({"key1": ["foo", "foo", "bar", "bar"],
                        "key2": ["one", "one", "one", "two"],
                        "rval": pd.Series([4, 5, 6, 7], dtype='Int64')})

pd.merge(left, right, on=["key1", "key2"], how="outer")

# Merging on Index

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: left_index=True or right_index=True (or both) indicate that the index should be used as the merge key

left1 = pd.DataFrame({"key": ["a", "b", "a", "a", "b", "c"],
                        "value": pd.Series(range(6), dtype="Int64")})

right1 = pd.DataFrame({"group_val": [3.5, 7]}, index=["a","b"])

left1 

right1

pd.merge(left1, right1, left_on="key", right_index=True)

# default merge keys is to intersect the join keys, you can instead form a union of them w/ outer join

# ex: union of sets is an outer join

pd.merge(left1, right1, left_on="key", right_index=True, how="outer")

# ex: with hierarchically indexed data, joining on index === to a multiple-key merge:

lefth = pd.DataFrame({"key1": ["ohio", "ohio", "ohio",
                                "nevada", "nevada"],
                        "key2": [2000, 2001, 2002, 2001, 2002],
                        "data": pd.Series(range(5), dtype="Int64")})

righth_index = pd.MultiIndex.from_arrays(
        [
                ["nevada", "nevada", "ohio", "ohio", "ohio", "ohio"],
                [2001, 2000, 2000, 2000, 2001, 2002]
        ]
)

righth = pd.DataFrame({"event1": pd.Series([0, 2, 4, 6, 8, 10], dtype="Int64",
                                index=righth_index),
                        "event2": pd.Series([1, 3, 5, 7, 9, 11], dtype="Int64", 
                                index=righth_index)})

lefth

righth

# ex: you have to indicate mult cols to merge on a list

pd.merge(lefth, righth, left_on=["key1", "key2"], right_index=True)

pd.merge(lefth, righth, left_on=["key1", "key2"], right_index=True, how="outer")

# ex: using indexes of both sides of the merge is possible

left2 = pd.DataFrame([[1., 2.], [3., 4.], [5., 6.]], 
                                        index=["a", "c", "e"], 
                                        columns=["ohio", "nevada"]).astype("Int64")

right2 = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],
                                        index=["b", "c", "d", "e"],
                                        columns=["missouri", "alabama"]).astype("Int64")

left2

right2

pd.merge(left2, right2, how="outer", left_index=True, right_index=True)

# ex: df has a join instance method. of course it does.

# in the prior example, you could have written:

left2.join(right2, how="outer")

# join performs a left join on the join keys by default

left1.join(right1, on="key")

# ex: for simple index-on-index merges, you can pass a list of dfs to join,
# instead of using the more general pandas.concat function

another = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [16., 17.]],
                        index=["a", "c", "e", "f"],
                        columns=["new york", "oregon"])

another

left2.join([right2, another])

left2.join([right2, another], how="outer")

# Concatenating Along an Axis

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

arr = np.arange(12).reshape((3, 4))

arr

np.concatenate([arr, arr], axis=1)      # axis=1 puts the arrays next to each other, not ontop

# ex: we have 3 series with no index overlap

s1 = pd.Series([0, 1], index=["a", "b"], dtype="Int64")

s2 = pd.Series([2, 3, 4], index=["c", "d", "e"], dtype="Int64")

s3 = pd.Series([5, 6], index=["f", "g"], dtype="Int64")

# calling pandas.concat with these obj in a list glues together the values/indexes

s1
s2
s3

pd.concat([s1, s2, s3])

# By default, pandas.concat works along axis="index", producing another Series. 

# If you pass axis="columns", the result will instead be a DataFrame:

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

pd.concat([s1, s2, s3], axis="columns")

# union === outer join // intersection === inner join

s4 = pd.concat([s1, s3])

s4

pd.concat([s1, s4], axis="columns", join="inner")

# ex: you want to create a hierarchical index on the concat axis. To do this, use the key argument

result = pd.concat([s1, s1, s3], keys=["one", "two", "three"])

result

result.unstack()

# ex: combine series along axis="columns", the keys become the df column headers

pd.concat([s1, s2, s3], axis="columns", keys=["one", "two", "three"])

# ex: same logic applies to df

df1 = pd.DataFrame(np.arange(6).reshape(3,2), index=["a", "b", "c"],
                                columns=["one", "two"])

df2 = pd.DataFrame(np.arange(4).reshape(2,2), index=["a", "c"],
                                columns=["three", "four"])

df1

df2

pd.concat([df1, df2], axis="columns", keys=["level1", "level2"])

# ex: pass a dictionary of obj instead of a list. the dict keys will be used

pd.concat({"level1": df1, "level2": df2}, axis="columns")

# ex: you can create hierarchical index by creating axis levels with the names argument

pd.concat([df1, df2], axis="columns", keys=["level1", "level2"], names=["upper", "lower"])

# Combining Data with Overlap

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: Numpy's where fun, does the array-oriented equivalent of an if-else expression

a = pd.Series([np.nan, 2.5, 0.0, 3.5, 4.5, np.nan],
                index=["f", "e", "d", "c", "b", "a"])

b = pd.Series([0., np.nan, 2., np.nan, np.nan, 5.],
                index=["a", "b", "c", "d", "e", "f"])

a 

b

np.where(pd.isna(a), b, a)

# ex: to line up values by index, use the series combine_first method:

a.combine_first(b)      # b into a, not a into b

# ex: with dataframes, combine_first does the same thing col by col

df1 = pd.DataFrame({"a": [1., np.nan, 5., np.nan],
                    "b": [np.nan, 2., np.nan, 6.,],
                    "c": range(2, 18, 4)})

df2 = pd.DataFrame({"a": [5., 4., np.nan, 3., 7.],
                    "b": [np.nan, 3., 4., 6., 8.]})


df1 

df2 

df1.combine_first(df2)  # again, df2 into df1, not df1 into df2

# 8.3 Reshaping and Pivoting

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# stack: this "rotates" or pivots from the columns to rows

# unstack: this pivots from row into the columns

# ex: row/column indexes are strings

data = pd.DataFrame(np.arange(6).reshape((2,3)),
                    index=pd.Index(["ohio", "colorado"], name="state"),
                    columns=pd.Index(["one", "two", "three"],
                    name="number"))

data

# using stack changes the df into a series:

result = data.stack()

result

# the reverse of above

result.unstack()

# ex: you can unstack at different levels by passing a level number or name:

result.unstack(level=0)         # the axes (indexes!) just switch. simple case.

result.unstack(level="state")   # the same result

# ex: unstacking could introduce missing data because values aren't found in each subgroup

s1 = pd.Series([0, 1, 2, 3], index=["a", "b", "c", "d"], dtype="Int64")
s2 = pd.Series([4,5,6], index=["c", "d", "e"], dtype="Int64")

data2 = pd.concat([s1, s2], keys=["one", "two"])        # the cols on top of each other, index still on the left

data2

data2.unstack()

data2.unstack().stack()

data2.unstack().stack(dropna=False)

# ex: unstack a df

df = pd.DataFrame({"left": result, "right": result + 5},
                columns=pd.Index(["left", "right"], name="side"))

df

df.unstack(level="state")

# calling stack we can indicate the name of the axis to stack:

df.unstack(level="state").stack(level="side")

# Pivoting “Long” to “Wide” Format

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: time series wrangling and other data cleaning

data = pd.read_csv("../book files/examples/macrodata.csv")

data.head()

data = data.loc[:, ["year", "quarter", "realgdp", "infl", "unemp"]]

data.head()     # should be second nature

# combine the year and quarter columns

periods = pd.PeriodIndex(year=data.pop("year"),         # pop deletes the col while putting it in periods
                        quarter=data.pop("quarter"),    # pop does the same thing here
                        name="date")

periods

data.index = periods.to_timestamp("D")

data.head()

# select a subset of cols and give the cols index the name "item":

data = data.reindex(columns=["realgdp", "infl", "unemp"])

data.columns.name = "item"

data.head()

# reshape the stack, turn the new index levels into cols with reset_index & adding col name "values"

long_data = (data.stack()
                .reset_index()
                .rename(columns={0: "value"}))

long_data       # long format for mult time series

# ex: df pivot method

pivoted = long_data.pivot(index="date", columns="item", values="value")

pivoted.head()

# ex: two value cols that you want to reshape simultaneously

long_data["value2"] = np.random.standard_normal(len(long_data))

long_data[:10]

# by omitting the last arg, you obtain a df with hierarchical cols

pivoted = long_data.pivot(index="date", columns="item")

pivoted.head()

pivoted["value"].head()

# ex: pivot is the same thing as set_index here followed by a unstack call

unstacked = long_data.set_index(["date", "item"]).unstack(level="item")

unstacked.head()

# Pivoting “Wide” to “Long” Format

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: inverse operation to pivot for df is pandas.melt. 
# instead of transforming one col into many in a new df, it merges mult col into one

df = pd.DataFrame({"key": ["foo", "bar", "baz"],
                "A": [1, 2, 3],
                "B": [4, 5, 6],
                "C": [7, 8, 9]})

df      # this should be second nature

# using pandas.melt, we need to tell which col (if any) are group indicators. Let's use "key" here

melted = pd.melt(df, id_vars="key")

melted

# using pivot. we can reshape back to the original layout

reshaped = melted.pivot(index="key", columns="variable", values="value")

reshaped        # second nature type of data manipulation

# reshaped creates an index from the row labels, but we need reset_index to get the data back

reshaped.reset_index()
