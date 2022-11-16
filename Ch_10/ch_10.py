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

# ex:

tips.groupby("smoker", group_keys=False).apply(top)

# Quantile and Bucket Analysis

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: simple random dataset and an equal-length bucket categorization using pandas.cut

frame = pd.DataFrame({"data1": np.random.standard_normal(1000),
                      "data2": np.random.standard_normal(1000)})

frame.head()

quartiles = pd.cut(frame["data1"], 4)   # categorical obj

quartiles.head(10)

# ex: categorical obj can be passed to groupby. We can compute a set of group statistics for the quartiles

def get_stats(group):
    return pd.DataFrame(
        {"min": group.min(), "max": group.max(),
        "count": group.count(), "mean": group.mean()}
    )

grouped = frame.groupby(quartiles)

grouped.apply(get_stats)

# Note: the same result above could have been computed simply by:

grouped.agg(["min", "max", "count", "mean"])

# ex: equal-sized buckets based on sample quantiles, use pandas.cut
# you can pass 4 as the num of buckets, & pass labels=False to obtain the quartile indices instead of intervals

quartiles_samp = pd.qcut(frame["data1"], 4, labels=False)

quartiles_samp.head()

grouped = frame.groupby(quartiles_samp)

grouped.apply(get_stats)

# Example: Filling Missing Values with Group-Specific Values

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# to remove NA's, use dropna
# to full NA's, use fillna

# ex: fill the null values with the mean:

s = pd.Series(np.random.standard_normal(6))

s[::2] = np.nan 

s

s.fillna(s.mean())  # v important

# ex: suppose you need the fill value to vary by group. 

# 1) group the data 2) use apply w/ a fn that calls fill na on each data chunk

# ex: us divided into east and west

states = ["ohio", "new york", "vermont", "florida", "oregon", "nevada",
        "california", "idaho"]

group_key = ["east", "east", "east", "east", "west", "west", "west", "west"]

data = pd.Series(np.random.standard_normal(8), index=states)

data

# lets set some values to NA

data[["vermont", "nevada", "idaho"]] = np.nan

data

data.groupby(group_key).size()

data.groupby(group_key).count()

data.groupby(group_key).mean()

# ex: fill the NA values using the group means, like so

def fill_mean(group):
    return group.fillna(group.mean())

data.groupby(group_key).apply(fill_mean)

# ex: put certain values for certain groups/keys?
# the groups have a name attribute set internally

fill_values = {"east": 0.5, "west": -1}

def fill_func(group):
    return group.fillna(fill_values[group.name])

data.groupby(group_key).apply(fill_func)

# Example: Random Sampling and Permutation

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: suppose you want to draw a random sample, w or w.o replacement- like a monte carlo simulation

# below we use the sample method for a series

# to demonstrate, here's a way to construct a deck of playing cards! 

suits = ["H", "S", "C", "D"]    # hearts, spades, clubs, diamonds
card_val = (list(range(1, 11)) + [10] *3) * 4
base_names = ["A"] + list(range(2, 11)) + ["J", "Q", "K"]
cards = []
for suit in suits:
    cards.extend(str(num) + suit for num in base_names)

deck = pd.Series(card_val, index=cards)

deck.head(13)     # a series of length 52

len(deck)

# drawing a hand of five cards from the deck could be written as:

def draw(deck, n=5):
    return deck.sample(n)   # .sample() looks interesting

draw(deck)

# suppose you wanted 2 random cards from each suit. 
# because the suit is the last char of each card name 7D, KH, etc
# we can group based on this and use apply:

def get_suit(card):
    # last letter is suit
    return card[-1]

deck.groupby(get_suit).apply(draw, n =2)

# or we could pass group_keys=False to drop the outer suit index, leaving in the selected cards:

deck.groupby(get_suit, group_keys=False).apply(draw, n=2)

# Example: Group Weighted Average and Correlation

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# split-apply-combine paradigm of groupby means
# operations bet col in a df or two series, s.a a group weighted avg, are possible

# ex: this dataset w/ group keys, values, and some weights

df = pd.DataFrame({"category": ["a", "a", "a", "a",
                                "b", "b", "b", "b"],
                    "data": np.random.standard_normal(8),
                    "weights": np.random.uniform(size=8)})

df

# the weighted avg by category would then be:

grouped = df.groupby("category")

def get_wavg(group):
    return np.average(group["data"], weights=group["weights"])

grouped.apply(get_wavg)

# ex: EOD prices for stocks and s&p index (spx):

close_px = pd.read_csv("../book files/examples/stock_px.csv", parse_dates=True, index_col=0)

close_px.info()

close_px.tail(4)

# ex: compute the yearly correlations of daily returns (computed from percent changes) w/ spx

# one way to do this, 1) create a fn that computes the pair-wise correlation of each col w/ the spx col

def spx_corr(group):
    return group.corrwith(group["SPX"])

# next, we compute precent change on close_px using pct_change:

rets = close_px.pct_change().dropna()

# group the percent changes by year

def get_year(x):
    return x.year

by_year = rets.groupby(get_year)

by_year.apply(spx_corr)

# ex: you can also do intercolumn correlations

def corr_aapl_msft(group):
    return group["AAPL"].corr(group["MSFT"])

by_year.apply(corr_aapl_msft)

# Example: Group-Wise Linear Regression

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# groupby is used to perform group-wise statistical analysis
# below uses the statsmodels econometrics library

import statsmodels.api as sm
def regress(data, yvar=None, xvars=None):
    Y = data[yvar]
    X = data[xvars]
    X["intercept"] = 1.
    result = sm.OLS(Y, X).fit()
    return result.params    

by_year.apply(regress, yvar="AAPL", xvars=["SPX"])  # linear regression

# 10.4 Group Transforms and “Unwrapped” GroupBys

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: consider a simple example of the transform method

df = pd.DataFrame({'key': ['a', 'b', 'c'] * 4,
                    'value': np.arange(12.)})

df

# here are the group means by key:

g = df.groupby('key')['value']

g.mean()

# spose we wanted a series of the same shape as df['value'] (1x12)
# but w/ values replaced by the avg grouped by 'key. 
# we can pass a fn that computes the mean of a single group to transform:

def get_mean(group):
    return group.mean()

g.transform(get_mean)

# ex: we can pass as a string alias as w/ the groupby agg method:

g.transform('mean')     # does the same thing as g.transform(get_mean) // prolly easier

# like apply, transform works w/ n that return series, but the result must be the same size as the input
 
# ex: we can multiply each group by 2 using a helper fn

def times_two(group):
    return group * 2

g.transform(times_two)

# ex: a more complicated example, we can compute the ranks in desc for each group

def get_ranks(group):
    return group.rank(ascending=False)

g.transform(get_ranks)

# ex: consider a group transform fn composed from simple aggregations:

def normalize(x):
    return (x - x.mean()) / x.std()

# we get equivalent results in this case using either transform or apply:

g.transform(normalize)

g.apply(normalize)

# ex: use built-in fn like mean or sum

g.transform('mean')

normalized = (df['value'] - g.transform('mean')) / g.transform('std')

normalized

# 10.5 Pivot Tables and Cross-Tabulation

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: spose you wanted to compute a table of group means (default pt aggregation type) arranged by day & smoker on the rows

tips.head()

tips.pivot_table(index=["day", "smoker"])

# now spose we want to take the avg of only tip_pct & size, & additionally
# group by time. we will put smoker in the table cols & time, day in table rows

tips.pivot_table(index=["time", "day"], columns="smoker",
                values=["tip_pct", "size"])

# partial totals are included by passing margins=True. allows all row, col labels

tips.pivot_table(index=["time", "day"], columns="smoker",
                values=["tip_pct", "size"], margins=True)

# count excludes null values
# len won't exclude null values

tips.pivot_table(index=["time", "smoker"], columns="day",
                values="tip_pct", aggfunc=len, margins=True)

# pass a fill_value

tips.pivot_table(index=["time", "size", "smoker"], columns="day",
                values="tip_pct", fill_value=0)

# Cross-Tabulations: Crosstab

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# crosstab is a pivot table that computes group frequencies

# ex:

from io import StringIO

data = """Sample Nationality Handedness
1 USA Right
2 JPN Left
3 USA Right
4 JPN Right
5 JPN Left
6 JPN Right
7 USA Right
8 USA Left
9 JPN Right
10 USA Right
"""

data = pd.read_table(StringIO(data), sep="\s+")

data    # this is beautiful

# we might want to summarize this data by nationality and handedness
# pivot_table could do this, but pandas.crosstab is more convenient

# ex:

pd.crosstab(data["Nationality"], data["Handedness"], margins=True)

# ex: tips data

pd.crosstab([tips["time"], tips["day"]], tips["smoker"], margins=True)

# Mastering pandas’s data grouping tools can help with data cleaning and modeling or statistical analysis work.

