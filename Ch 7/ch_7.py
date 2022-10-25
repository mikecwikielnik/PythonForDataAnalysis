"""
Chapter 7. Data Cleaning and Preparation

McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 
"""

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

# permuting (randomly reordering) a Series or the rows in the df is possible under numpy.random.permutation function

# permutations produces an array of integers indicating the new ordering

df = pd.DataFrame(np.arange(5 * 7).reshape((5, 7)))

df

sampler = np.random.permutation(5)

sampler

# ex: take function or the iloc-based indexing

df.take(sampler)

df.iloc[sampler]

# ex: axis="columns" selects a premutation of the columns

column_sampler = np.random.permutation(7)

column_sampler

df.take(column_sampler, axis="columns")

# ex: a random subset w.o replacement (same row can't appear twice), you use the sample method on a series & a df

df.sample(n=3)

# ex: to generate a sample with replacement, you use replace=True to sample

choices = pd.Series([5, 7, -1, 6, 4])

choices.sample(n=10, replace=True)

# Computing Indicator/Dummy Variables

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: pandas.get_dummies function 

df = pd.DataFrame({"key": ["b", "b", "a", "c", "a", "b"],
                    "data1": range(6)})

df

pd.get_dummies(df["key"])

# ex: adding a prefix to the columns

dummies = pd.get_dummies(df["key"], prefix="key")

df_with_dummy = df[["data1"]].join(dummies)

df_with_dummy

# ex: movielens 1m dataset 

mnames = ["movie_id", "title", "genres"]

movies = pd.read_table("../book files/datasets/movielens/movies.dat", sep="::",
                        header=None, names=mnames, engine="python")

movies[:10]

# ex: Series method str.get_dummies

dummies = movies["genres"].str.get_dummies("|")

dummies.iloc[:10, :6]

# adding "Genre_" to the column names in the dummies df with the add_prefix method

movies_windic = movies.join(dummies.add_prefix("Genre_"))

movies_windic.iloc[0]

# ex: a useful recipe for stats applications is to combine pandas.get_dummies with a discretization function like pandas.cut

np.random.seed(12345)   # to make the example repeatable

values = np.random.uniform(size=10)

values

bins = [0, 0.2, 0.4, 0.6, 0.8, 1]

pd.get_dummies(pd.cut(values, bins))

# 7.3 Extension Data Types

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: create a Series of integers with a missing value

s = pd.Series([1, 2, 3, None])

s

s.dtype

# ex: create a Series instead using pandas.Int64Dtype

s = pd.Series([1, 2, 3, None], dtype=pd.Int64Dtype())

s

s.isna()

s.dtype

# output <NA> means the value is missing 

s[3]

s[3] is pd.NA

# ex: Categorical extension type

# extension types allows you to convert easily as part of your data cleaning process

df = pd.DataFrame({"A": [1, 2, None, 4],
                   "B": ["one", "two", "three", None],
                   "C": [False, None, False, True]})

df

df["A"] = df["A"].astype("Int64")
df["B"] = df["B"].astype("string")
df["c"] = df["C"].astype("boolean")

df

# 7.4 String Manipulation

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# Python Built-In String Object Methods

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: a comma-separated string can be broken into pieces with split

val = "a,b, guido"

val.split(",")

# split is often combined with strip to trim whitespace

pieces = [x.strip() for x in val.split(",")]

pieces

# substrings can be concatenated together w/ 2 colon delimeter using addition:

first, second, third = pieces

first + "::" + second + "::" + third

# but this isn't practical. A better way is pass a list or tuple to the join method on teh string "::"

"::".join(pieces)

# ex: the in keyword is the best way to detect a substring, though index and find can also be used

"guido" in val

val.index(",")

val.find(":")

# ex: count returns number of occurences

val.count(",")

# ex: replace will sub occurences. it is also used to delete patterns by passing an empty string

val.replace(",", "::")

val.replace(",", "")

# See Table 7-4 for a listing of some of Python’s string methods.

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# Regular Expressions

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: split a string with a variable number of whitespace characters(tabs, spaces, and newlines)

# regex describing one or more whitespace characters is \s+

import re

text = "foo     bar\t baz    \tqux"

re.split(r"\s+", text)

# ex: compile using re.compile, forms a reusable regex object

regex = re.compile(r"\s+")

regex.split(text)

# ex: listing all the patterns matching regex, you can use the findall method

regex.findall(text)

# re.compile is important when applying to many different strings

# match and search are closely related to findall.
# search returns first match.
# match only matches the beginning of the string

# ex: a block of text and a regular expression

text = """Dave dave@google.com
Steve steve@gmail.com
Rob rob@gmail.com
Ryan ryan@yahoo.com"""
pattern = r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}"

# re.IGNORECASE makes the regex case insensitive
regex = re.compile(pattern, flags=re.IGNORECASE)

# using findall produces a list of the email addresses

regex.findall(text)

# search returns a special match for the first email in the text 
# the preceding regex, the match object can only tell us the start and end position

m = regex.search(text)

m

text[m.start():m.end()]

# regex.match returns None, as it will match only if the pattern occurs at the start of the string

print(regex.match(text))

# sub will return a new string with occurences of the pattern replaced by a new string

print(regex.sub("REDACTED", text))

# ex: you have emails and you want to split into username, domain name, and domain suffix.
# you put paranthesis around the parts of the pattern to segment

pattern = r"(A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})"

regex = re.compile(pattern, flags=re.IGNORECASE)

# a match object returns a tuple of the pattern componenets with its groups method

m = regex.match("wesm@bright.net")

m.groups()  # didn't work

regex.findall(text)     # didn't work

# String Functions in pandas

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

data = {"Dave": "dave@google.com", "Steve": "steve@gmail.com",
        "Rob": "rob@gmail.com", "Wes": np.nan}

data = pd.Series(data)

data

data.isna()

# string and regex methods can be used on each value using data.map, but this will fail on NA values

# ex: we could check whether each email address has "gmail" in with stir.contains:

data.str.contains("gmail")

# ex:

data_as_string_ext = data.astype('string')  # this looks like it changes the data type to string

data_as_string_ext

data_as_string_ext.str.contains("gmail")

# ex: vectorized element retrieval. Either use str.get or index into the str attribute:

import re

pattern = r"([A-Z0-9._%+-]+)@(A-Z0-9.-]+)\.([A-Z]{2,4})"

data.str.findall(pattern, flags=re.IGNORECASE)

matches = data.str.findall(pattern, flags=re.IGNORECASE).str[0]

matches

matches.str.get(1)

# 7.5 Categorical Data

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# Background and Motivation

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: unique and value_counts

values = pd.Series(['apple', 'orange', 'apple', 'apple']*2)

values

pd.unique(values)

pd.value_counts(values)

# ex: dimension tables

values = pd.Series([0, 1, 0, 0] * 2)

dim = pd.Series(['apple', 'orange'])

values

dim

# ex: take method restors the original Series of strings

dim.take(values)

# Categorical Extension Type in pandas

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

