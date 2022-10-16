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

