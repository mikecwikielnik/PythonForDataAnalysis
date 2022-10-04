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

data = {"state": ["ohio", "ohio", "ohio", "nevada", "nevada", "nevada"],
        "year": [2000, 2001, 2002, 2001, 2002, 2003],
        "pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}

frame = pd.DataFrame(data)

frame   # lines 116 - 122 should be second nature

frame.head()    # Same as R

frame.tail()    # Same as R

# specify a sequence of columns

pd.DataFrame(data, columns=["year", "state", "pop"])

# if you pass a column that doesn't exist, you get NaNs

frame2 = pd.DataFrame(data, columns=["year", "state", "pop", "debt"])

frame2

frame2.columns

# retrieve via dict notation or dot attribute

frame2["state"]  # dictionary notation

frame2.year

# frame2[column] works for any column name

# iloc and loc attributes! 

frame2.loc[1]

frame2.iloc[2]

# columns can be modified in-place, debt is assigned a scalar value or an array of values:

frame2["debt"] = 16.5

frame2

frame2["debt"] = np.arange(6.)

frame2

# ex: things must match

val = pd.Series([-1.2, -1.5, -1.7], index=["two", "four", "five"])

frame2["debt"] = val

frame2

# del method

frame2["eastern"] = frame2["state"] == "ohio"   # this is one way to create new columns

frame2

del frame2["eastern"]

frame2.columns

# ex: nested dictionary of dictionaries

populations = {"ohio": {2000: 1.5, 2001: 1.7, 2002: 3.6},
               "nevada": {2001: 2.4, 2002: 2.9}}

frame3 = pd.DataFrame(populations)

frame3

frame3.T    # transpose an array

# a -> a.T -> a may lose information about column data types

# ex: the book shifts the years over one by the explicit index [2001, 2002, 2003]

pd.DataFrame(populations, index=[2001, 2002, 2003])

# Dictionaries of Series are treated in the same way:

pdata = {"ohio": frame3["ohio"][:-1],
         "nevada": frame3["nevada"][:2]}

pd.DataFrame(pdata)

# Table 5-1. Possible data inputs to the DataFrame constructor

# McKinney, Wes. Python for Data Analysis (p. 224). O'Reilly Media. Kindle Edition. 

# ex: naming the axis of df

frame3.index.name = "year"  # y axis

frame3.columns.name = "state"   # x axis

frame3

# Index Objects

# McKinney, Wes. Python for Data Analysis (p. 226). O'Reilly Media. Kindle Edition. 

# ex:

obj = pd.Series(np.arange(3), index=["a", "b", "c"])

index = obj.index

index

index[1:]

# Index objects are immutable

index[1] = "d"  # TypeError

# Immutability makes it safer to share Index objects among data structures:

labels = pd.Index(np.arange(3))

labels

obj2 = pd.Series([1.5, -2.5, 0], index=labels)

obj2

# boolean check

obj2.index is labels

# Index is array-like, and behaves like a fixed-size set

frame3

frame3.columns

"ohio" in frame3.columns

2022 in frame3.index

# Table 5-2. Some Index methods and properties

# McKinney, Wes. Python for Data Analysis (p. 228). O'Reilly Media. Kindle Edition. 

# the table above computes set intersection, set union, append, difference, and insert

'''
5.2 Essential Functionality

McKinney, Wes. Python for Data Analysis (p. 229). O'Reilly Media. Kindle Edition. 
'''

# Reindexing

# McKinney, Wes. Python for Data Analysis (p. 229). O'Reilly Media. Kindle Edition. 

# important method on pandas objects is reindexing

# ex:

obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=["d", "b", "a", "c"])      # pd.Series!

obj

# calling a reindex on this Series

obj2 = obj.reindex(["a", "b", "c", "d", "e"])

obj2

# method: ffill

obj3 = pd.Series(["blue", "purple", "yellow"], index=[0, 2, 4])

obj3    # second nature

obj3.reindex(np.arange(6), method="ffill")

# In df, reindex can alter rows/columns/both, rows are first though

frame = pd.DataFrame(np.arange(9).reshape((3, 3)),
                     index=["a", "c", "d"],
                     columns=["ohio", "texas", "california"])

frame

frame2 = frame.reindex(index=["a", "b", "c", "d"])

frame2

# columns can be reindexed with the columns keyword:

states = ["texas", "utah", "california"]

frame.reindex(columns=states)

# ex:

frame.reindex(states, axis="columns")

# Table 5-3. reindex function arguments

# McKinney, Wes. Python for Data Analysis (p. 232). O'Reilly Media. Kindle Edition. 

# many users prefer to reindex using the loc operator

frame.loc[["a", "d", "c"], ["california", "texas"]]

# Dropping Entries from an Axis

# McKinney, Wes. Python for Data Analysis (p. 234). O'Reilly Media. Kindle Edition. 

obj = pd.Series(np.arange(5.), index=["a", "b", "c", "d", "e"])         # np.arange(5.) stretches the values from 0 to 5 & it must match the index 

obj     # this should be second nature

new_obj = obj.drop("c")         # convenient

new_obj

obj.drop(["d", "c"])

# With pd.DataFrame, index values can be deleted from either axis. 

# ex: an example DataFrame

data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=["ohio", "colorado", "utah", "new york"],
                    columns=["one", "two", "three", "four"])

data    # hi beautiful dataframe

# calling drop with a seq of labels will drop values from the row labels (axis 0):

data.drop(index=["colorado", "ohio"])

# to drop labels from columns, instead use the columns keyword:

data.drop(columns=["two"])      # we are not affecting the main array. these are "views" into the data

new_array = data.drop(columns=["two"])

new_array       # this is a new variable with col "two" dropped. you have done this alot in R

# Indexing, Selection, and Filtering

# McKinney, Wes. Python for Data Analysis (p. 236). O'Reilly Media. Kindle Edition. 

# ex:

obj = pd.Series(np.arange(4.), index=["a", "b", "c", "d"])

obj

obj["b"]        # selects the "value" in the key, value ordered pair. ofc, this isn't a dictionary

obj[1]  # yields the same as ["b"], because ["a"] is 0

# up to here should be second nature. this is really just a review on R

obj[2:4]        # a typical slice

obj[["b", "a", "d"]]

obj[[1, 3]]

obj[obj < 2]

# again, nothing here is all that different from R

# Note: the preferred way is the loc operator. This will be shown in the following example:

obj1 = pd.Series([1, 2, 3], index=[2, 0, 1])

obj2 = pd.Series([1, 2, 3], index=["a", "b", "c"])

obj1

obj2    

obj1[[0, 1, 2]]

obj2[[0, 1, 2]]

# Series is a n row x 1 column data frame
# DataFrame is the union of all the Series to make a n row x n column dataframe

# making elements of the series 5

obj2.loc["b":"c"] = 5   # called "indexing into"

obj2    # this is also something that should be second nature. It is quite powerful in something like sql

# indexing into a df retrieves 1 or more columns either with a single value or seq:

data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=["ohio", "colorado", "utah", "new york"],     # index is y axis
                    columns=["one", "two", "three", "four"])

data

data["two"]

data[["three", "one"]]  # here is good because you can switch the columns

# attow, you don't know the sql version of this. perhaps you manually pick it there too

# indexing like this has a few special cases

data[:2]        # modifies rows

data[data["three"] > 5]         # pick the rows where the "three" columns is greater than 5

# more sql like queries into the data

# ex: Boolean frame

data < 5

# Given an inequality, index into the 0 for all values less than 5:

data[data < 5] = 0

data

# Selection on DataFrame with loc and iloc

# McKinney, Wes. Python for Data Analysis (p. 243). O'Reilly Media. Kindle Edition. 

# ex: select a single row by label:

data

data.loc["colorado"]

data.loc[["colorado", "new york"]]

# below is another way to parse

data.loc["colorado", ["two", "three"]]

# ex:

data.iloc[2]

data.iloc[[2, 1]]

data.iloc[2, [3, 0, 1]]

data.iloc[[1, 2], [3, 0, 1]]    # RC Cola...count starts at 0, 2x3 array

# a multiple "query" view into the data

data.loc[:"utah", "two"]

data.iloc[:, :3][data.three > 5]

# Table 5-4. Indexing options with DataFrame

# McKinney, Wes. Python for Data Analysis (p. 246). O'Reilly Media. Kindle Edition. 

# Integer indexing pitfalls

# McKinney, Wes. Python for Data Analysis (p. 247). O'Reilly Media. Kindle Edition. 

# ex: use an index to use list like call features

ser = pd.Series(np.arange(3.))

ser

ser[-1] # will yield an error msg

ser

ser2 = pd.Series(np.arange(3.), index=["a", "b", "c"])

ser2[-1]

# ex: use loc for labels or iloc for integers: you will get exactly what you want

ser.iloc[-1]

# ex:

ser[:2]         # integer oriented slicing

# always prefer indexing with loc and iloc to avoid ambiguity

# Pitfalls with chained indexing

# McKinney, Wes. Python for Data Analysis (p. 249). O'Reilly Media. Kindle Edition. 

# be tender when modifying dataframes in place

data.loc[:, "one"] = 1

data

data.iloc[2] = 5

data

data.loc[data["four"] > 5] = 3

data

# Arithmetic and Data Alignment

# McKinney, Wes. Python for Data Analysis (p. 252). O'Reilly Media. Kindle Edition. 

# ex:

s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=["a", "c", "d", "e"])

s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1],
               index=["a", "c", "e", "f", "g"])

s1

s2

# adding s1 + s2 yields:

s1 + s2         # this is a nice move

# ex: with df, alignment is happens across both rows and columns

df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list("bcd"),
                index=["ohio", "texas", "colorado"])
# pay attention to what happens between arange and reshape
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list("bde"),
                   index=["utah", "ohio", "texas", "oregon"])

df1

df2

df1 + df2       # look at the mathematics of ohio: "b", the arithmetic is carried out

# elements that are not found in both, get NaN

# a df with no column or row labels in common, the result will contain all nulls:

# Arithmetic methods with fill values

# McKinney, Wes. Python for Data Analysis (p. 255). O'Reilly Media. Kindle Edition. 

# ex: when an axis label is found in one object but not the other:

df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)),
                   columns=list("abcd"))

df2 = pd.DataFrame(np.arange(20.).reshape(4, 5),
                   columns=list("abcde"))

df2.loc[1, "b"] = np.nan        # manually inputtin a nan value

df1

df2

df1 + df2

# ex: using the add method to fill in values. Takind df1 values and inputting them into the df2 df

df1.add(df2, fill_value=0)

# Table 5-5. Flexible arithmetic methods

# McKinney, Wes. Python for Data Analysis (p. 257). O'Reilly Media. Kindle Edition. 

# Operations between DataFrame and Series

# McKinney, Wes. Python for Data Analysis (p. 258). O'Reilly Media. Kindle Edition. 

