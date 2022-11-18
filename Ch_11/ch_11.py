"""
Chapter 11. Time Series

McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 
"""

import numpy as np
import pandas as pd

# 11.1 Date and Time Data Types and Tools

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# start here: datetime, time, and calendar
# datetime.datetime, or simply datetime, is widely used

from datetime import datetime

now = datetime.now()

now

now.year, now.month, now.day

# datetime stores both date, time down to the microsecond

# ex: datetime.timedelta, or simply timedelta, is the difference bet two datetime obj

delta = datetime(2011, 1, 7) - datetime(2008, 6, 24, 8, 15)

delta

delta.days

delta.seconds

# you can add or subtract a timedelta or multiple to a datetime obj to yield a new obj

from datetime import timedelta

start = datetime(2011, 1, 7)

start + timedelta(12)

start -2 * timedelta(12)

# Converting Between String and Datetime

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: format datetime obj as strings using str or the strftime method

stamp = datetime(2011, 1, 3)

str(stamp)  

stamp.strftime("%Y-%m-%d")

# you can use many of the same format codes to convert strings to date using datetime.strptime (sometimes %F can't be used)

value = "2011-01-03"

datetime.strptime(value, "%Y-%m-%d")

datestrs = ["7/6/2011", "8/6/2011"]

[datetime.strptime(x, "%m/%d/%Y") for x in datestrs]

# datetime.strptime is one way to parse a date with a known format

# ex: pd.to_datetime method parses many different kinds of date representations

datestrs = ["2011-07-06 12:00:00", "2011-08-06 00:00:00"]

pd.to_datetime(datestrs)

# also, it handles values that should be considered missing(None, empty string, etc):

idx = pd.to_datetime(datestrs + [None])

idx

idx[2]

pd.isna(idx)

# 11.2 Time Series Basics

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

dates = [datetime(2011, 1, 2), datetime(2011, 1, 5),
        datetime(2011, 1, 7), datetime(2011, 1, 8),
        datetime(2011, 1, 10), datetime(2011, 1, 12)]

ts = pd.Series(np.random.standard_normal(6), index=dates)

ts

# under the hood, these datetime objs have been put in a DatetimeIndex:

ts.index

# like other series, arithmetic automatically aligns the dates

ts + ts[::2]    # ts[::2] selects every second element in ts

# A pandas.Timestamp can be substituted most places where you would use a datetime object.

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# Indexing, Selection, Subsetting

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# time series behaves like any other series when you are indexing and selecting data based on the label

stamp = ts.index[2]

ts[stamp]   

# as a convenience, you can pass a string that is interpretable as a date:

ts["2011-01-10"]

# ex: 

longer_ts = pd.Series(np.random.standard_normal(1000),
                    index=pd.date_range("2000-01-01", periods=1000))

longer_ts

longer_ts["2001"]

# here, the str "2001" is interpreted as a year and selects that time period
# this also works if you specify the month

longer_ts["2001-05"]    # a nice way to parse by year, month

# slicing w/ datetime obj works as well:

ts[datetime(2011, 1, 7):]

ts[datetime(2011, 1, 7):datetime(2011, 1, 10)]

# ex: performing a range query

ts

ts["2011-01-06":"2011-01-11"]

# ex: you can also truncate. it slices a series between two dates:

ts.truncate(after="2011-01-09")

# it holds up for df too, indexing on its rows:

dates = pd.date_range("2001-01-01", periods=100, freq="W-WED")

long_df = pd.DataFrame(np.random.standard_normal((100, 4)),
                        index=dates,
                        columns=["colorado", "texas",
                                "new york", "ohio"])

long_df.loc["2001-05"]

# Time Series with Duplicate Indices

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: mult data obs falling on a particular timestamp

dates = pd.DatetimeIndex(["2000-01-01", "2000-01-02", "2000-01-02",
                        "2000-01-02", "2000-01-03"])

dup_ts = pd.Series(np.arange(5), index=dates)

dup_ts

# we can tell that the index is not unique by checking its is_unique property

dup_ts.index.is_unique

dup_ts["2000-01-03"]    # not duplicated

dup_ts["2000-01-02"]    # duplicated

# spose you wanted to agg the data having nonunique ts. use groupby and pass level=0

grouped = dup_ts.groupby(level=0)

grouped.mean()

grouped.count()

# 11.3 Date Ranges, Frequencies, and Shifting

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: convert the sample time series to fixed daily freq by calling resample:

ts

resampler = ts.resample("D")    # "D" is daily freq

resampler

# Generating Date Ranges

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# pandas.date_range is responsible for generating a DatetimeIndex w/ indicated length according to some freq

index = pd.date_range("2012-04-01", "2012-06-01")

index

# ex: if you only pass a start or end date, you must enter a # of periods to generate. very cool! 

pd.date_range(start="2012-04-01", periods=20)

pd.date_range(end="1989-10-11", periods=20)

# ex: business days only

pd.date_range("2000-01-01", "2000-12-01", freq="BM")

# pandas.date_range by default perserves the time

pd.date_range("1989-10-11 6:11:00", periods=5)

# to get rid of the time, you want to *normalize* to midnight

pd.date_range("1989-10-11 6:11:00", periods=5, normalize=True)

# Frequencies and Date Offsets

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

