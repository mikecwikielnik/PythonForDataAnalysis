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

