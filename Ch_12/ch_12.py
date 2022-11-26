"""
Chapter 12. Introduction to Modeling Libraries in Python

McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 
"""

import numpy as np
import pandas as pd

# 12.1 Interfacing Between pandas and Model Code

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# a common workflow for models is to use pandas for data loading, cleaning 
# before switching over to a modeling library to build the model itself

# feature engineering in machine learing is any data transformation or analytics that extract
# info from a raw dataset that may be useful in a modeling context. 
# data aggregation/grouby tools explored here are often used in a feature engineering context

# point of contact bet pandas and other analysis libraries is numpy arrays. 

# ex: to turn a df into a numpy array, use the to_numpy method

data = pd.DataFrame({
    'x0': [1, 2, 3, 4, 5],
    'x1': [0.01, -0.01, 0.25, -4.1, 0.],
    'y': [-1.5, 0., 3.6, 1.3, -2.]})

data

data.columns

data.to_numpy()

# to convert back to a df, as mentioned earlier, you can pass a two-dimensional ndaarry w/ optional col names

df2 = pd.DataFrame(data.to_numpy(), columns=['one', 'two', 'three'])

df2

# to_numpy method is intended to be used when your data is homogeneous
# if your data is heterogeneous, the result will be an ndarray of pythong obj

df3 = data.copy()

df3['strings'] = ['a', 'b', 'c', 'd', 'e']

df3

df3.to_numpy()

# for subsets of data, use loc indexing w/ to_numpy

model_cols = ['x0', 'x1']

data.loc[:, model_cols].to_numpy()

# ex: spose we had a nonnumeric col

data['category'] = pd.Categorical(['a', 'b', 'a', 'a', 'b'], categories=['a', 'b'])

data

# if we wanted to replace the 'category' col w/ a dummy var,
# we create dumy var, drop the 'category' col, and then join the result

dummies = pd.get_dummies(data.category, prefix='category')

data_with_dummies = data.drop('category', axis=1).join(dummies)

data_with_dummies

# there are nuance to fitting models w/ dummy var
# it's easier to use patsy when you have more than simple numeric col

# 12.2 Creating Model Descriptions with Patsy

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

