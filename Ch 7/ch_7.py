"""
Chapter 7. Data Cleaning and Preparation

McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 
"""

from tokenize import group
import numpy as np

import pandas as pd

# 7.1 Handling Missing Data

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

float_data = pd.Series([1.2, -3.5, np.nan, 0])

float_data

# ex: isna() yields a Boolean Series with True where values are null

float_data.isna()

# ex: analysis done on the missing data itself

string_data = pd.Series(["aardvark", np.nan, None, "avocado"])

string_data     # second nature

string_data.isna()

float_data = pd.Series([1, 2, None], dtype='float64')

float_data

float_data.isna()

# See Table 7-1 for a list of some functions related to missing data handling.

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# Filtering Out Missing Data

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: dropna() is useful

data = pd.Series([1, np.nan, 3.5, np.nan, 7])

data.dropna()

# below is the same

data[data.notna()]

# dropna() by default drops any row containing a missing value

data = pd.DataFrame([[1., 6.5, 3.], [1., np.nan, np.nan],
                    [np.nan, np.nan, np.nan], [np.nan, 6.5, 3.]])

data

# ex: hot="all" will drop only rows that are all NaN

data.dropna(how="all")

# to pass columns in the same way, pass axis="columns":

data[4] = np.nan

data

data.dropna(axis="columns", how="all")

# ex: Suppose you want to keep only rows containing at most a certain number of missing obs. thresh arg

df = pd.DataFrame(np.random.standard_normal((7, 3)))

df.iloc[:4, 1] = np.nan

df.iloc[:2, 2] = np.nan

df

df.dropna()

df.dropna(thresh=2)

# Filling In Missing Data

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# fillna() with a constant replaces missing values. workhorse function.

df.fillna(100)

# fillna() with a dictionary, you can use different value for each column

df.fillna({1: 0.5, 2: 0.10})

# ex: simple data imputation using the median or mean statistics with fillna()

data = pd.Series([1., np.nan, 3.5, np.nan, 7])

data.fillna(data.mean())

# See Table 7-2 for a reference on fillna function arguments.

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

"""
7.2 Data Transformation

McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 
"""

# Removing Duplicates

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: 

data = pd.DataFrame({"k1": ["one", "two"] * 3 + ["two"],
                    "k2": [1, 1, 2, 3, 3, 4, 4]})

data    # so easy

# ex: duplicated method returns a boolean series indicating whether each row is a duplicate

data.duplicated()

# ex: drop_duplicates. duplicates are dropped (look at last row)

data.drop_duplicates()

# ex: Suppose we had an additional column of values and wanted to filter duplicates based on only the "k1" column

data["v1"] = range(7)   # really nice trick

data

data.drop_duplicates(subset=["k1"])     # another really nice trick

# ex: duplicated and drop_duplicates by default keep the last observed value combination. pass keep="last" will return the last one

data.drop_duplicates(["k1", "k2"], keep="last")

# Transforming Data Using a Function or Mapping

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: 

data = pd.DataFrame({"food": ["bacon", "pulled pork", "bacon",
                              "pastrami", "corned beef", "bacon",
                              "pastrami", "honey ham", "nova lox"],
                            "ounces": [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})

data    # you should know how to do this

# ex: adding a column indicating the type of animal that each food came from

meat_to_animal = {
    "bacon": "pig",
    "pulled pork": "pig",
    "pastrami": "cow",
    "corned beef": "cow",
    "honey ham": "pig",
    "nova lox": "salmon"
}

# ex: map method on a Series 

data["animal"] = data["food"].map(meat_to_animal)   # data["food"].map(meat_to_animal) matches meat_to_animal to "food" 

data

# ex: we can also pass a function that does all the work

def get_animal(x):
    return meat_to_animal[x]

data["food"].map(get_animal)

# map is convenient to perform element-wise transformation

# Replacing Values

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# map can be used to modify a subet of values, but 'replace' is simpler

# ex: consider this Series

data = pd.Series([1., -999., 2., -999., -1000., 3.])

data

data.replace(-999, np.nan)
 
# if you want to replace multiple values at once, you pass a list

data.replace([-999, -1000], np.nan)

# to use a different replacement value, pass a list of substitutes

data.replace([-999, -1000], [np.nan, 0])

# you can do it via directory as well

data.replace({-999: np.nan, -1000: 0})

# Renaming Axis Indexes

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: modifying axes in place 

data = pd.DataFrame(np.arange(12).reshape((3, 4)),
                    index=["ohio", "colorado", "new york"],
                    columns=["one", "two", "three", "four"])

# like a Series, the axis indexes have a map method

def transform(x):
    return x[:4].upper()

data.index.map(transform)   # this is cool and a little obscure 

# assigning the index attribute, this modifies the df in place

data.index = data.index.map(transform)

data

# rename creates a modified view of the original df

data.rename(index=str.title, columns=str.upper)

# rename can be used with a dictionary which can provide new values

data.rename(index={"ohio": "indiana"},
            columns={"three": "peekaboo"})

# Discretization and Binning

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]

# divide into bins of 18-25, 26-35, 36-60, 61+. You have to use pandas.cut

bins = [18, 25, 35, 60, 100]

age_categories = pd.cut(ages, bins)

age_categories

# special categorical object

age_categories.codes    

age_categories.categories

age_categories.categories[0]

pd.value_counts(age_categories)     # bin coutns for the result of pandas.cut! this- you should know. 

# pass a list or array to the labels option to use labels

group_names = ["youth", "youngAdult", "middleAged", "senior"]

pd.cut(ages, bins, labels=group_names)  # second nature

# passing an integer creates uniform equal-length bins based on min/max

# ex:

data = np.random.uniform(size=20)

pd.cut(data, 4, precision=6)    # 2 decimal places

# panda.qcut

data = np.random.standard_normal(1000)

quartiles = pd.qcut(data, 4, precision=2)

quartiles

pd.value_counts(quartiles)  # neat

# pass your own quartiles (numbers between 0 and 1)

pd.qcut(data, [0, 0.1, 0.5, 0.9, 1.]).value_counts()

# Detecting and Filtering Outliers

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: df with some normally distributed data

data = pd.DataFrame(np.random.standard_normal((1000, 4)))

data.describe()

# suppose you want to find values in one of the columns exceeding 3 in absolute value

col = data[2]

col[col.abs() > 3]

# to select all rows having a value exceeding 3 or -3, you use the any method on a boolean df

data[(data.abs() > 3).any(axis="columns")]

# Permutation and Random Sampling

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

