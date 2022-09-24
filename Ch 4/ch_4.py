'''
Chapter 4. NumPy Basics: Arrays and Vectorized Computation

McKinney, Wes. Python for Data Analysis (p. 141). O'Reilly Media. Kindle Edition. 
'''
'''
4.1 The NumPy ndarray: A Multidimensional Array Object

McKinney, Wes. Python for Data Analysis (p. 144). O'Reilly Media. Kindle Edition. 
'''

# ex:

import numpy as np

data = np.array([[1.5, -0.1, 3], [0, -3, 6.5]])

data

# then we write mathematical operations with data

data * 10 # this applies to the mat per element

data + data

# ex:

data.shape

data.dtype

# Creating ndarrays

# McKinney, Wes. Python for Data Analysis (p. 146). O'Reilly Media. Kindle Edition. 

# ex: a list is a good example for this

data1 = [6, 7.5, 8, 0, 1]

arr1 = np.array(data1)

arr1

# ex: lists can be elements of an array

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]

arr2 = np.array(data2)

arr2

# ex: this is how you check dimensions

arr2.ndim

arr2.shape

# ex: how to create higher dimensional arrays

np.zeros(10)

np.zeros((3, 6))

np.empty((2, 3, 2))

'''
Data Types for ndarrays

McKinney, Wes. Python for Data Analysis (p. 150). O'Reilly Media. Kindle Edition. 
'''

