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

