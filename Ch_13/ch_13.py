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

# Counting Time Zones in Pure Python, Example 1

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: spose we are interestd in find the time zones that occur most often in the dataset (tz field).
# First, let's extract a list of time zones again using a list comprehension

# time_zones = [rec["tz"] for rec in records]     # spose to yield an error msg

# the reasoning is not all records have a time zone. 
# we can handle this by adding the check if "tz" in rec
# at the end of the list comprehension

time_zones = [rec["tz"] for rec in records if "tz" in rec]

time_zones[:10]

# Next, we show two ways to produce counts by time zone: 1) the hard way (using just the python lib) and 2) the easy way (using pandas)

# one way to do the counting is to use a dict to store counts while
# we iterate through the time zones

def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] +=1
        else:
            counts[x] = 1
    return counts

# using more advanced tools in the pythong standard lib, you can write the same thing more briefly

from collections import defaultdict
def get_counts2(sequence):
    counts = defaultdict(int) # values will initialize to 0
    for x in sequence:
        counts[x] += 1
    return counts

# the logic below makes the code more reusable. 
# to use it, just pass the time_zones list:

counts = get_counts(time_zones)

counts["America/New_York"]

len(time_zones)

# if we wanted the top 10 time zones and their counts, 
# we can make a list of tuples by (count, timezone) and sort it

def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

# results

top_counts(counts)

# if you search the python standard lib, you may find the collections.Counter class, 
# makes this task even simpler

from collections import Counter

counts = Counter(time_zones)

counts.most_common(10)  # notice the empty string with 521 observations

# Counting Time Zones with pandas

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# you can create a df from the original set of records by passing
# the list of records to pandas.DataFrame

frame = pd.DataFrame(records)

# we can look at basic info w/ frame.info()

frame.info()

frame["tz"].head()

# use valu_counts method for Series

tz_counts = frame["tz"].value_counts()

tz_counts.head()

# using matplotlib, we make plots nicer by filling in a sub value for unk or missing time zone values
# we replace the missing values with fillna method and use boolean array indexing for the empty strings

clean_tz = frame["tz"].fillna("Missing")    # lines 127 to 131 are very important

clean_tz[clean_tz == ""] = "Unknown"

tz_counts = clean_tz.value_counts()

tz_counts.head()    # this is dope af

# at this point, we can use the seaborn package to make a horizontal bar plot 

import seaborn as sns

subset = tz_counts.head()

sns.barplot(y=subset.index, x=subset.to_numpy())    # beautiful ass chart

# subset.index is import because it is col name
# to_numpy makes an arra (or series) of the data

# the a field contains info about the browser, device, or application used to perform the URL shortening

frame["a"][1]

frame["a"][50]

frame["a"][51][:50]     # long line

# ex: split off the first token in the string (which is roughly the broswer capability) 
# and make another summary of the user behavior

results = pd.Series([x.split()[0] for x in frame["a"].dropna()])

results.head()

results.value_counts().head(8)

# now spose, you want to decompose the top time zones into windows and non-windows users

cframe = frame[frame["a"].notna()].copy()

# we want to then compute a value for whether or not each row is windows

cframe["os"] = np.where(cframe["a"].str.contains("Windows"),
                        "Windows", "Not Windows")

cframe["os"].head(5)

# now group the data by its time zone col and this new list of operating systems

by_tz_os = cframe.groupby(["tz", "os"])

# group counts can be computed with size. This result is then reshaped into a table w/ unstack

agg_counts = by_tz_os.size().unstack().fillna(0)

agg_counts.head()

# Finally, lets select the top overall time zones. 

# I construct an indirect index array from the row_counts in agg_counts.
# After computing the row counts with agg_counts.sum("columns"), 
# I can call argsort() to obtain an index array that can be used to sort in asc

indexer = agg_counts.sum("columns").argsort()

indexer.values[:10]

# use take to select the rows in that order, then slice off the last 10 rows (largest values)

count_subset = agg_counts.take(indexer[-10:])

count_subset

# nlargest does the same thing

agg_counts.sum(axis="columns").nlargest(10)

# seaborns barplot fn
# First, call count_subset.stack() and reset the index to rearrange the data for better compatibility

count_subset = count_subset.stack()     # i think this means the bars are stacked per index

count_subset.name = "total"

count_subset = count_subset.reset_index()

count_subset.head(10)

sns.barplot(x="total", y="tz", hue="os", data=count_subset)     # very important

# ex: normalize the percentages to sum to 1! :)

def norm_total(group):
    group["normed_total"] = group["total"] / group["total"].sum()
    return group

results = count_subset.groupby("tz").apply(norm_total)

# below is the final visualization
sns.barplot(x="normed_total", y="tz", hue="os", data=results)   # very important

# ex: you could have computed the normalized sum more efficiently by using the transform method with groupby

g = count_subset.groupby("tz")

results2 = count_subset["total"] / g["total"].transform("sum")

# 13.2 MovieLens 1M Dataset

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

unames = ["user_id", "gender", "age", "occupation", "zip"]
users = pd.read_table("../book files/datasets/movielens/users.dat", sep="::",
                        header=None, names=unames, engine="python")

rnames = ["user_id", "movie_id", "rating", "timestamp"]
ratings = pd.read_table("../book files/datasets/movielens/ratings.dat", sep="::",
                        header=None, names=rnames, engine="python")

mnames = ["movies_id", "title", "genres"]
movies = pd.read_table("../book files/datasets/movielens/movies.dat", sep="::",
                        header=None, names=mnames, engine="python")

# you can verify that everything succeeded by looking at each df

users.head(5)

ratings.head(5)

movies.head(5)

ratings

# ex: table merge w/ pandas's merge fn

data = ratings.merge(users, left_on="user_id", right_on="user_id")  # this is good

data.head()

data = data.merge(movies, left_on="movie_id", right_on="movies_id")

data.head()     # this should work for the most part

data.iloc[0]

# ex: to get mean movie rating by gender, use pivot_table

mean_ratings = data.pivot_table("rating", index="title", columns="gender", aggfunc="mean")

mean_ratings.head(5)    # movie titles as row labels (the "index") and gender as column labels

# ex: filter down to movies that received at least 250 raings

ratings_by_title = data.groupby("title").size()

ratings_by_title.head()

active_titles = ratings_by_title.index[ratings_by_title >= 250]

active_titles   # this whole example is perfect

# ex: the index of titles (>250) can the be used to select rows from mean_ratings ussing .loc:

mean_ratings = mean_ratings.loc[active_titles]

mean_ratings

# ex: to see the top films among female viewers, sort by the female col in desc

top_female_ratings = mean_ratings.sort_values("F", ascending=False)

top_female_ratings

# Measuring Rating Disagreement

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: spose you wanted to find the movies that are the most divisive
# between male and viewers. One way is to add a column to mean_ratings
# containing the difference in means, then sort

mean_ratings["diff"] = mean_ratings["M"] - mean_ratings["F"]

# sort by diff yields the movies w/ the greatest rating diff 
# so we see the ones preferred by women

sorted_by_diff = mean_ratings.sort_values("diff")

sorted_by_diff.head()

# reversing the order of rows, we get the movies preferred by men
# that women didn't rate as highly

sorted_by_diff[::-1].head()

# ex: spose instead you wanted the movies that elicited the most disagreement among viewers,
# independent of gender id. disagreement can be measured by the variance or standard deviation of the ratings.
# first, we need to compute the rating standard deviation by title and then filter down to the active titles. 

rating_std_by_title = data.groupby("title")["rating"].std()

rating_std_by_title = rating_std_by_title.loc[active_titles]

rating_std_by_title.head()

# then sort in desc order

rating_std_by_title.sort_values(ascending=False)[:10]

# ex: movies can belong to multiple genres. to help us group by genre
# use the explode method on df. first, we split the genres string into a list of genres
# using str.split method on the series

movies["genres"].head()

movies["genres"].head().str.split("|")  # this is awesome

movies["genre"] = movies.pop("genres").str.split("|")

movies.head()

# now calling movies.explode("genre") yields an unique row per unique genre per movie

movies_exploded = movies.explode("genre")

movies_exploded[:10]

# now merge all 3 tables together and group by name

movies_exploded.head()

ratings_with_genre = pd.merge(movies_exploded, ratings, left_on="movies_id", right_on="movie_id")

ratings_with_genre = pd.merge(ratings_with_genre, users, left_on="user_id", right_on="user_id")

ratings_with_genre.columns

ratings_with_genre.iloc[0]

genre_ratings = (ratings_with_genre.groupby(["genre", "age"])["rating"].mean().unstack("age"))

genre_ratings[:10]

# 13.3 US Baby Names 1880–2010

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# we have to do some data wrangling to load this dataset

names1880 = pd.read_csv("../book files/datasets/babynames/yob1880.txt", names=["name", "sex", "births"])

names1880

# take the sum of the births column by sex as the total number of births in that year

names1880.groupby("sex")["births"].sum()    # groupby by (sex) to get the ["births"] figure, what figure? sum(). 

# ex: you have separate files, we need to put them in a single df and add a year field. 
# use pandas.concat

pieces = []
for year in range(1880, 2022):  # off-one error even w/ file names
    path = f"../book files/datasets/babynames/yob{year}.txt"
    frame = pd.read_csv(path, names=["name", "sex", "births"])

    # Add a column for the year
    frame["year"] = year
    pieces.append(frame)

# Concatentate everything into a single df
names = pd.concat(pieces, ignore_index=True) # True because we're not interesteed in preserving the original row numbers

names

# Now, we can start aggregating the data at the year & sex level
# using groupby or pivot_table

total_births = names.pivot_table("births", index="year", columns="sex", aggfunc=sum)
# what data fields do you want to look at? births. what index (y-axis)? year. what col names do you want? sex. 
# aggfunc=sum means sum all the births.

total_births.tail()

total_births.plot(title="Total births by sex and year")

# Now, lets insert a column prop w/ the fraction of babies given each name relative to the total number of births
# a prop value of 0.02 means 2/100 babies. Then we groupby by year and sex, then add a new col to each group

def add_prop(group):
    group["prop"] = group["births"] / group["births"].sum()
    return group
names = names.groupby(["year", "sex"]).apply(add_prop)

# the resulting complete dataset now looks like this

names


# w/ a grouping operation, check your work aka "sanity check". verify all the col sums = 1

names.groupby(["year", "sex"])["prop"].sum()

# now, extract a subset. the top 1,000 names for each sex/year combo. Another group operation.

def get_top1000(group):
    return group.sort_values("births", ascending=False)[:1000]

grouped = names.groupby(["year", "sex"])

top1000 = grouped.apply(get_top1000)

top1000.head()

# drop the group index since we don't need it 

top1000 = top1000.reset_index(drop=True)

top1000.head()

# Analyzing Naming Trends

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# w/ the full dataset and the top 1000 in hand. let's analyze some trends.
# first we ca split the top 1000 names into the boy and girl portions

boys = top1000[top1000["sex"] == "M"]   # v interesting way to get a subset

# take the top1000 and then look at the sex col then take M for boys, F for girls

girls = top1000[top1000["sex"] == "F"]

# form a pivot table of the total number of births by year and name

total_births = top1000.pivot_table("births", index="year", columns="name", aggfunc=sum)

total_births

# dataframe's plot method will be useful here

total_births.info()     # v cool to look at! df.info()

subset = total_births[["John", "Harry", "Mary", "Marilyn"]]

subset.plot(subplots=True, figsize=(12, 10), title="Number of births per year")

# what is important with the above code is this: we really have three sets here. 
# boys, girls, and the top 1000. total_births is a pivot table that takes all the names
# in alphabetical order as columns, the index is the year! the number in the field is the
# number of births. total_births[["John", "Harry", "Mary", "Marilyn"]] means calling these
# fields in total_births pivot table. This means subset has these four names and the years
# 1880 - 2021 as the index. 

# Measuring the increase in naming diversity

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

