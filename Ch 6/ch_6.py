'''
Chapter 6. Data Loading, Storage, and File Formats

McKinney, Wes. Python for Data Analysis (p. 286). O'Reilly Media. Kindle Edition. 
'''

# Input and output typically fall into a few main categories:
    
# reading text files and other more efficient on-disk formats, loading data from databases,

# and interacting with network sources like web APIs.

# McKinney, Wes. Python for Data Analysis (p. 286). O'Reilly Media. Kindle Edition. 

'''
6.1 Reading and Writing Data in Text Format

McKinney, Wes. Python for Data Analysis (p. 286). O'Reilly Media. Kindle Edition. 
'''

# pandas.read_csv is just like in R: read.csv("data_file")

# Table 6-1. Text and binary data loading functions in pandas

# McKinney, Wes. Python for Data Analysis (p. 286). O'Reilly Media. Kindle Edition. 

# ex:

import csv
from pickle import FALSE

import pandas as pd 

df = pd.read_csv("../book files/examples/ex1.csv")

df  # second nature

# you can assign default column names or 
# you can specify names yourself:

pd.read_csv("../book files/examples/ex2.csv", header=None)  # this replaces the column names with numbers

pd.read_csv("../book files/examples/ex2.csv", names=["a", "b", "c", "d", "message"])    # this will prove crucial

# ex: index_col puts the message col as the "row names" 

names = ["a", "b", "c", "d", "message"]

pd.read_csv("../book files/examples/ex2.csv", names=names, index_col="message")

# ex: hierarchial index from multiple columns, pass a list of col numbers or col names:

parsed = pd.read_csv("../book files/examples/csv_mindex.csv",
                     index_col=["key1", "key2"])

parsed

# ex: \s+ provides uniform white space?

result = pd.read_csv("../book files/examples/ex3.txt", sep="\s+")

result

# ex: skipping rows

pd.read_csv("../book files/examples/ex4.csv", skiprows=[0, 2, 3])

# ex: missing values

result = pd.read_csv("../book files/examples/ex5.csv")

result

# ex: isna() yields boolean results

pd.isna(result)

# ex: na_values option adds a seq of strings to look for to add as missing:

result = pd.read_csv("../book files/examples/ex5.csv", na_values=["NULL"])

result

# ex: keep_default_na disables default NA value representations

result2 = pd.read_csv("../book files/examples/ex5.csv", keep_default_na=False)

result2

result2.isna()  # boolean check

result3 = pd.read_csv("../book files/examples/ex5.csv", keep_default_na=False,
                      na_values=["NA"])

result3

result3.isna()  # boolean check

# Table 6-2. Some pandas.read_csv function arguments

# McKinney, Wes. Python for Data Analysis (p. 296). O'Reilly Media. Kindle Edition. 

# Reading Text Files in Pieces

# McKinney, Wes. Python for Data Analysis (p. 298). O'Reilly Media. Kindle Edition. 

# ex: make the pandas display settings more compact:

pd.options.display.max_rows = 10    # top 5, and bottom 5

result = pd.read_csv("../book files/examples/ex6.csv")

result

# ex: read a small number of rows

pd.read_csv("../book files/examples/ex6.csv", nrows=5)

# Writing Data to Text Format

# McKinney, Wes. Python for Data Analysis (p. 300). O'Reilly Media. Kindle Edition. 

# ex: 

data = pd.read_csv("../book files/examples/ex5.csv")

data

# ex: using to_csv, we can write the data out to a comma-separated file

data.to_csv("../book files/examples/out.csv")

# ex: sys.stdout prints text to console rather than a file

import sys

data.to_csv(sys.stdout, sep="|")

# ex: here the missing values appear as empty strings, use other sentinel value

data.to_csv(sys.stdout, na_rep="xYz")   # kind of neat!

# ex: with no other options specified, both row/columns are written and can be disabled

data.to_csv(sys.stdout, index=False, header=False)

# Working with Other Delimited Formats

# McKinney, Wes. Python for Data Analysis (p. 302). O'Reilly Media. Kindle Edition. 

