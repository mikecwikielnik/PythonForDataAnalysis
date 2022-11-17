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

