"""
Chapter 7. Data Cleaning and Preparation

McKinney, Wes. Python for Data Analysis (p. 330). O'Reilly Media. Kindle Edition. 
"""

from sys import float_info
import pandas as pd

import numpy as np

"""
7.1 Handling Missing Data

McKinney, Wes. Python for Data Analysis (p. 330). O'Reilly Media. Kindle Edition. 
"""

# descriptive stats on pandas objects exclude missing data by default

# ex:

float_data = pd.Series([1.2, -3.5, np.nan, 0])

float_data

# ex: isna method

float_data.isna()   # second nature

# ex: analysis on the missing data itself

string_data = pd.Series(["aardvark", np.nan, None, "avocado"])

string_data     # create a series..second nature

# isna() check

string_data.isna()

# ex: 

float_data = pd.Series([1, 2, None], dtype='float64')

float_data

float_data.isna()

# Table 7-1. NA handling object methods

# McKinney, Wes. Python for Data Analysis (p. 333). O'Reilly Media. Kindle Edition. 

# Filtering Out Missing Data

# McKinney, Wes. Python for Data Analysis (p. 333). O'Reilly Media. Kindle Edition. 

