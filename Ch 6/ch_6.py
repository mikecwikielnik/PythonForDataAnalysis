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


from ast import parse
import csv

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

# ex:

import csv

f = open("../book files/examples/ex7.csv")

reader = csv.reader(f)

# iterating through the reader yields lists of values with quotes removed

for line in reader:
    print(line)
    
f.close()

# It is now up to us to do the wrangling needed

# ex:

# 1) read files into a list of lines

with open("../book files/examples/ex7.csv") as f:
    lines = list(csv.reader(f))
    
# 2) then we split the lines into the header line and the data lines:

header, values = lines[0], lines[1:]

# 3) then we create a dictionary of columns using a dict commprehension(one line program) & the expression zip(*values),
# tranposes rows to columns:

data_dict = {h: v for h, v in zip(header, zip(*values))}

data_dict

# ex:

# 1) create a simple subclass of csv.Dialect

class my_dialect(csv.Dialect):
    lineterminator: str = "\n"
    delimiter = ";"
    quotechar = '"'
    quoting = csv.QUOTE_MINIMAL
    
reader = csv.reader(f, dialect=my_dialect)

# ex: we can give individual CSV dialect params as keywords to csv.reader w.o a subclass

reader = csv.reader(f, delimiter="|")

# Table 6-3. CSV dialect options

# McKinney, Wes. Python for Data Analysis (p. 304). O'Reilly Media. Kindle Edition. 

# ex: writing delimited files manually, use csv.writer

with open("mydata.csv", "w") as f:
    writer = csv.writer(f, dialect=my_dialect)
    writer.writerow(("one", "two", "three"))
    writer.writerow(("1", "2", "3"))
    writer.writerow(("4", "5", "6"))
    writer.writerow(("7", "8", "9"))
    
# JSON Data

# McKinney, Wes. Python for Data Analysis (p. 306). O'Reilly Media. Kindle Edition. 

obj = """
{"name": "Wes",
"cities_lived": ["Akron", "Nashville", "New York", "San Francisco"],
"pet": null,
"siblings": [{"name": "Scott", "age": 34, "hobbies": ["guitars", "soccer"]},
             {"name": "Katie", "age": 42, "hobbies": ["diving", "art"]}]
}
"""

# ex: JSON

import json

result = json.loads(obj)

result

# ex: json.dumps

asjson = json.dumps(result)

asjson

# ex: pass a list of dictionaries to the df constructor & select a subset

siblings = pd.DataFrame(result["siblings"], columns=["name", "age"])

siblings    # very cool

# ex: default options for pandas.read_json assume each object in the json array is a row in a table

data = pd.read_json("../book files/examples/example.json")

data

# XML and HTML: Web Scraping

# McKinney, Wes. Python for Data Analysis (p. 309). O'Reilly Media. Kindle Edition. 

# ex: 

tables = pd.read_html("../book files/examples/fdic_failed_bank_list.html")

len(tables)

failures = tables[0]

failures.head()

failures.value_counts()

a = failures["Bank Name"].unique()

# ex: computing the number of bank failures by year

close_timestamps = pd.to_datetime(failures["Closing Date"])

close_timestamps.dt.year.value_counts()     # really nice insights

# Parsing XML with lxml.objectify

# McKinney, Wes. Python for Data Analysis (p. 311). O'Reilly Media. Kindle Edition. 

# ex: 

from lxml import objectify

path = "../book files/datasets/mta_perf/Performance_MNR.xml"

with open(path) as f:
    parsed = objectify.parse(f)
    
root = parsed.getroot()

data = []

skip_fields = ["PARENT_SEQ", "INDICATOR_SEQ",
               "DESIRED_CHANGE", "DECIMAL_PLACES"]

for elt in root.INDICATOR:
    el_data = {}
    for child in elt.getchildren():
        if child.tag in skip_fields:
            continue
        el_data[child.tag] = child.pyval
    data.append(el_data)
    
# lastly, convert this list of dictionaries into a df

perf = pd.DataFrame(data)

perf.head()

perf2 = pd.read_xml(path)

perf2

# 6.2 Binary Data Formats

# McKinney, Wes. Python for Data Analysis (p. 316). O'Reilly Media. Kindle Edition. 

# ex: pickle module

frame = pd.read_csv("../book files/examples/ex1.csv")

frame

frame.to_pickle("../book files/examples/frame_pickle")

# ex: pandas.read_pickle

pd.read_pickle("../book files/examples/frame_pickle")

# Reading Microsoft Excel Files

# McKinney, Wes. Python for Data Analysis (p. 317). O'Reilly Media. Kindle Edition. 

