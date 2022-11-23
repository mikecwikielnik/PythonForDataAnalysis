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

# base freq is M for monthly or H for hourly

# ex: the hour class

from pandas.tseries.offsets import Hour, Minute

hour = Hour()

hour

# you can define a multiple of an offset by passing an int

four_hours = Hour(4)

four_hours

# instead use 4H

pd.date_range("2000-01-01", "2000-01-03 23:59", freq="4H")

# you can combined these offsets by addition

Hour(2) + Minute(30)

# otherwise, you can pass freq str like 130min

pd.date_range("2000-01-01", periods=10, freq="130min")

# Week of month dates

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# one useful freq is "week of month", WOM. This allows you to get things like third Friday of each mo

monthly_dates = pd.date_range("2012-01-01", "2012-09-01", freq="WOM-3FRI")

list(monthly_dates)

# Shifting (Leading and Lagging) Data

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# shift method

ts = pd.Series(np.random_standard_normal(4),
                index=pd.date_range("2000-01-01", periods=4, freq="M"))

ts

ts.shift(2)     # the items shifted down a "cell" like in excel

ts.shift(-2)    # same, except up

# A common use of shift is computing consecutive percent changes 

# in a time series or multiple time series as DataFrame columns. 

# This is expressed as: 

# ts / ts.shift(1) - 1

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex:

ts.shift(2, freq="M")

# other freq can be passed too, giving flexibility

ts.shift(3, freq="D")

ts.shift(1, freq="90T")     # T = minutes

# Shifting dates with offsets

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# pandas date offsets can be used with datetime or Timestamp obj

from pandas.tseries.offsets import Day, MonthEnd

now = datetime(2011, 11, 17)

now + 3 * Day()

# ex: 

now + MonthEnd()

now + MonthEnd(1)   # same as MonthEnd()

now + MonthEnd(2)

# ex: rollforward // rollback methods

offset = MonthEnd()

offset.rollforward(now)

offset.rollback(now)

# ex: date offsets & groupby

ts = pd.Series(np.random.standard_normal(20),
                index=pd.date_range("2000-01-15", periods=20, freq="4D"))   # 20 4-day periods

ts

ts.groupby(MonthEnd().rollforward).mean()

# resample does this easier, and faster

ts.resample("M").mean()

# 11.4 Time Zone Handling

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

import pytz

pytz.common_timezones[-5:]

# to get a tz obj from pytz, use pytz.timezone

tz = pytz.timezone("America/New_York")

tz

# Time Zone Localization and Conversion

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: time series in pandas are tz naive. consider:

dates = pd.date_range("2012-03-09 09:30", periods=6)

ts = pd.Series(np.random.standard_normal(len(dates)), index=dates)

ts

print(ts.index.tz)  # None

# date ranges can be generated w/ a tz set:

pd.date_range("2012-03-09 09:30", periods=10, tz="UTC")

# ex: conversion from naive to localized (observed in some tz) is done by tz_localize method

ts

ts_utc = ts.tz_localize("UTC")

ts_utc

ts_utc.index    

# once a time series has been localized to a particular tz, it can be converted to another tz w/
# tz_convert

ts_utc.tz_convert("America/New_York")

# how to localize to us eastern and convert to, utc or berlin

ts_eastern = ts.tz_localize("America/New_York")

ts_eastern.tz_convert("UTC")

ts_eastern.tz_convert("Europe/Berlin")

# ex: tz_localize and tz_convert are also instance methods on DatetimeIndex

ts.index.tz_localize("Asia/Shanghai")

# Operations with Time Zone-Aware Timestamp Objects

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: timestamp obj can be localized from naive to tz-aware & converted from one tz to another

stamp = pd.Timestamp("2011-03-12 04:00")

stamp_utc = stamp.tz_localize("utc")

stamp_utc.tz_convert("America/New_York")

# you can pass a tz when creating the Timestamp

stamp_moscow = pd.Timestamp("2011-03-12 04:00", tz="Europe/Moscow")

stamp_moscow

# ex: 30 min before transiting to Daylight Savings Time

stamp = pd.Timestamp("2012-03-11 01:30", tz="US/Eastern")

stamp

stamp + Hour()

# then 90 minutes before transitioning out of Daylight Savings Time

stamp= pd.Timestamp("2012-11-04 00:30", tz="US/Eastern")

stamp

stamp + 2 * Hour()

# Operations Between Different Time Zones

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# if two time series w/ diff tz are combined, the result will be utc

# ex: straight-forward operation 

dates = pd.date_range("2012-03-07 09:30", periods=10, freq="B")

ts = pd.Series(np.random.standard_normal(len(dates)), index=dates)

ts

ts1 = ts[:7].tz_localize("Europe/London")

ts2 = ts1[2:].tz_convert("Europe/Moscow")

result = ts1 + ts2

result.index

# 11.5 Periods and Period Arithmetic

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# periods are time spans like days, months, quarters or years.

p = pd.Period("2011", freq="A-DEC")

p   # represents 1/1/2011 - 12/31/2011

# ex: effect of shifting their frequency

p + 5

p - 2

# ex: period_range method

periods = pd.period_range("2000-01-01", "2000-06-30", freq="M")

periods

# ex: PeriodIndex class stores a seq of periods and serves as an axis index

pd.Series(np.random.standard_normal(6), index=periods)

# ex: array of str, use PeriodIndex class, where all of its values are periods

values = ["2001Q3", "2002Q2", "2003Q1"]

index = pd.PeriodIndex(values, freq="Q-DEC")

index

# Period Frequency Conversion

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: annual period -> monthly period either at the start or end of the year

p = pd.Period("2011", freq="A-DEC")

p

p.asfreq("M", how="start")

p.asfreq("M", how="end")

p.asfreq("M")

# ex: fiscal year ending on a month other than december, the corresponding monthly subperiods are different

p = pd.Period("2011", freq="A-JUN")

p

p.asfreq("M", how="start")

p.asfreq("M", how="end")

# ex:

periods = pd.period_range("2006", "2009", freq="A-DEC")

ts = pd.Series(np.random.standard_normal(len(periods)), index=periods)

ts

ts.asfreq("M", how="start")

# ex: "B" frequency indicates that we want the end of the period

ts.asfreq("B", how="end")

# Quarterly Period Frequencies

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

p = pd.Period("2012Q4", freq="Q-JAN")

p

# ex: where the fiscal year is not a calendar year

p.asfreq("D", how="start")

p.asfreq("D", how="end")

# ex: get a timestamp on the 2nd-to-last business day of the quarter

p4pm = (p.asfreq("B", how="end") - 1).asfreq("T", how="start") + 16 * 6

p4pm

p4pm.to_timestamp()

# to_timestamp() method returns the Timestamp at the start of the period by default

# ex: generate quarterly ranges using pandas.period_range. The arithmetic is identical, too

periods = pd.period_range("2011Q3", "2012Q4", freq="Q-JAN")

ts = pd.Series(np.arange(len(periods)), index=periods)

ts

new_periods = (periods.asfreq("B", "end") - 1).asfreq("H", "start") + 1

ts.index = new_periods.to_timestamp()

ts

# Converting Timestamps to Periods (and Back)

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: series, df indexed by timestamps can be converted to periods w/ the to_period method

dates = pd.date_range("2000-01-01", periods=3, freq="M")

ts = pd.Series(np.random.standard_normal(3), index=dates)

ts

pts = ts.to_period()

pts

# ex: specify any supported frequency

dates = pd.date_range("2000-01-29", periods=6)

ts2 = pd.Series(np.random.standard_normal(6), index=dates)

ts2

ts2.to_period("M")

# ex: convert back to timestamps, use the to_timestamp method, which returns a DatetimeIndex

pts = ts2.to_period()

pts

pts.to_timestamp(how="end")

# Creating a PeriodIndex from Arrays

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: fixed freq datasets are sometimes stored w/ time span information spread across multiple columns
# year & qtr are in different columns

data = pd.read_csv("../book files/examples/macrodata.csv")

data.head(5)

data["year"]

data["quarter"]

# passing these arrays to PeriodIndex w/ a freq, you can combine them to form an index for the df

index = pd.PeriodIndex(year=data["year"], quarter=data["quarter"], freq="Q-DEC")

index

data.index = index

data["infl"]

# 11.6 Resampling and Frequency Conversion

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# higher to lower = downsampling
# lower to higher = upsampling 
# not all resampling falls into either of these categoris

# pandas objects are equipped w/ a resample method, which is the workhorse fun for all frequency conversion
# resample is like groupby. you call resample to group the data, then call an aggregation fn

dates = pd.date_range("2000-01-01", periods=100)

ts = pd.Series(np.random.standard_normal(len(dates)), index=dates)

ts

ts.resample("M").mean()

ts.resample("M", kind="period").mean()

# Downsampling

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# things to think about when using resample to downsample data:

# 1) which side of each interval is closed?
# 2) how to label each aggregated bin, either w/ the start of the interval or the end

# to illustrate, lets look at some one-minute freq data

dates = pd.date_range("2000-01-01", periods=12, freq="T")

ts = pd.Series(np.arange(len(dates)), index=dates)

ts

# spose you wanted to aggregate this data into five-min chunks or bars by taking the sum of each group

ts.resample("5min").sum()

# simple inequalites
# by default, the left bin edge is inclusive, so 00:00 value is included
# but 00:05 value is excluded

ts.resample("5min", closed="right").sum()

# passing label="right", you can label them with the right bin edge

ts.resample("5min", closed="right", label="right").sum()

# ex: shifting the result index by some amount,
# say subtracting 1s from the right edge to make it more clear which interval the ts refers to

from pandas.tseries.frequencies import to_offset

result = ts.resample("5min", closed="right", label="right").sum()

result.index = result.index + to_offset("-1s")

result

# Open-high-low-close (OHLC) resampling

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

"""
In finance, a popular way to aggregate a time series is to compute four values for each bucket: 


*the first (open), last (close), maximum (high), and minimal (low) values.*


By using the ohlc aggregate function, you will obtain a DataFrame having columns containing these four aggregates, 

which are efficiently computed in a single function call:

McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 
"""

ts = pd.Series(np.random.permutation(np.arange(len(dates))), index=dates)

ts.resample("5min").ohlc()

# Upsampling and Interpolation

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: unsampling is converting from a lower freq to a higher freq, where no aggregation is needed. 
# let's consider a df w/ some weekly data

frame = pd.DataFrame(np.random.standard_normal((2, 4)),
                        index=pd.date_range("2000-01-01", periods=2,
                                        freq="w-WED"),
                        columns=["colorado", "texas", "new york", "ohio"])

frame

# ex:

df_daily = frame.resample("D").asfreq()

df_daily

# fillna, reindex methods are available for resampling

frame.resample("D").ffill()

# you can fill a certain number of periods 

frame.resample("D").ffill(limit=2)

# Resampling with Periods

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

