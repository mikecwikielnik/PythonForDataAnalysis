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

