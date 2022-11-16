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

