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

data = pd.DataFrame({
    'x0': [1, 2, 3, 4, 5],
    'x1': [0.01, -0.01, 0.25, -4.1, 0.],
    'y': [-1.5, 0., 3.6, 1.3, -2.]})

data

import patsy

y, x = patsy.dmatrices('y ~ x0 + x1', data)

# now we have:

y

x   # both x,y yield interesting results

# patsy DesignMatrix instances are numpy ndarrays with additional metadata

np.asarray(y)

np.asarray(x)

"""
in line 96: x gives an intercept term. 

This is a convention for LINEAR MODELS like ORDINARY LEAST SQUARES (OLS) REGRESSION.

You can supress this term by adding the term + 0 to the model
"""

patsy.dmatrices('y ~ x0 + x1 + 0', data)[1]

# patsy objects can be passed directly into algos like 
# numpy.linalg.lstsq !! 
'''
numpy.linalg.lstsq performs OLS regression. 
'''

coef, resid, _, _ = np.linalg.lstsq(x, y)

# ex: you can reattach the model col names to the fitted coefs to obtain a Series

coef

coef = pd.Series(coef.squeeze(), index=x.design_info.column_names)

coef    # this is very nice looking. 

# Data Transformations in Patsy Formulas

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

y, x = patsy.dmatrices('y ~ x0 + np.log(np.abs(x1) + 1)', data)

x

"""
Some commonly used variable transformations include 

a) standardizing (to mean 0 and variance 1)
b) centering (subtracting the mean)

patsy had built-in fn's for this purpose
"""

# ex:

y, x = patsy.dmatrices('y ~ standardize(x0) + center(x1)', data)

x

"""
when you are training your data to later score your models. 

patsy.build_design_matrices fn can apply the transformations (statistics from the training data)
to the scoring data. 
"""

# ex:

new_data = pd.DataFrame({
    'x0': [6, 7, 8, 9],
    'x1': [3.1, -0.5, 0, 2.3],
    'y': [1, 2, 3, 4]})

new_x = patsy.build_design_matrices([x.design_info], new_data)

new_x

# when you want to add cols from a dataset by name, you must wrap them in the special I fn

y, x = patsy.dmatrices('y ~ I(x0 + x1)', data)

x

# Categorical Data and Patsy

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

