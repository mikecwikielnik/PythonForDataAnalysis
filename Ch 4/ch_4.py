'''
Chapter 4. NumPy Basics: Arrays and Vectorized Computation

McKinney, Wes. Python for Data Analysis (p. 141). O'Reilly Media. Kindle Edition. 
'''
'''
4.1 The NumPy ndarray: A Multidimensional Array Object

McKinney, Wes. Python for Data Analysis (p. 144). O'Reilly Media. Kindle Edition. 
'''

# ex:

from array import array
from unicodedata import name
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

# ex: convert data types

arr = np.array([1, 2, 3, 4, 5])

arr.dtype

float_arr = arr.astype(np.float64)

float_arr

float_arr.dtype

# ex: float to integer

arr = np.array([3.7, -1.2])

arr

arr.astype(np.int32)

# ex: strings to float

numeric_strings = np.array(["1.25", "-9.6"], dtype=np.string_)  # use pandas for non-numeric data

numeric_strings.astype(float)

# Arithmetic with NumPy Arrays

# McKinney, Wes. Python for Data Analysis (p. 155). O'Reilly Media. Kindle Edition. 

arr = np.array([[1., 2., 3.], [4., 5., 6.,]])

arr

arr * arr

arr - arr

1 / arr

arr ** 2

arr2 = np.array([[0, 0, 1], [5, 15, 26]] )

arr2

arr > arr2

# Basic Indexing and Slicing

# McKinney, Wes. Python for Data Analysis (p. 156). O'Reilly Media. Kindle Edition. 

# one-dimensional arrays are simple; they act similarly to python lists:

arr = np.arange(10)

arr

arr[5]

arr[5:8]

arr[5:8] = 12   # replace elements 5, 6, 7 (Start counting from zero && one off error!)

arr

arr_slice = arr[5:8]     # start counting from zero

arr_slice

arr_slice[1]=12345

arr

arr_slice[:] = 64

arr

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

arr2d[2]

arr2d[0][2]

arr2d[0, 2]

# ex:

arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

arr3d

# arr3d[0] is a 2x3 array, we know this

# below is copying the values so we can replace them later

old_values = arr3d[0].copy()

arr3d[0] = 42

arr3d

arr3d[0] = old_values

arr3d

# indexing with slices

arr

arr[0:3]    # you could leave the first element blank like below

arr2d

arr2d[:2]

# ex: you can pass multiple slices just like you can pass multipe indexes:

arr2d[:2, 1:]

# ex: assigning values to a slice expression

arr2d[:2, 1:] = 0

arr2d

# Boolean Indexing

# McKinney, Wes. Python for Data Analysis (p. 166). O'Reilly Media. Kindle Edition. 

names = np.array(["bob", "joe", "will", "bob", "will", "joe", "joe"])

data = np.array([[4, 7], [0, 2], [-5, 6], [0, 0], [1, 2], [-12, -4], [3, 4]])

names

data 

# ex: boolean array

names == "bob"

data[names == "bob"]    # match the data element with the name "bob"- output array will make sense

# ex: select from the rows where names == "bob" and index the columsn, too

data[names == "bob", 1:]

# another way 

data[names == "bob", 1]

# ex: negation of the statement

names != "bob"

~(names == "bob")

data[~(names == "bob")]

# ex: ~ operator

cond = names == "bob"

data[~cond]

# ex: & (and) and | (or):

mask = (names == "bob")|(names == "will")

mask

data[mask]

# ex: setting all of the negative numbers in data to 0:

data[data < 0] = 0

data

# ex: set whole rows or columns

data[names != "joe"] = 7

data

# Fancy Indexing

# McKinney, Wes. Python for Data Analysis (p. 170). O'Reilly Media. Kindle Edition. 

# ex: 

arr = np.zeros((8, 4))

for i in range(8):
    arr[i] = i
    
arr

# to select a subset of the rows in an order, pass a list or ndarray of integers

arr[[4, 3, 0, 6]]

arr[[-3, -5, -7]]

# ex: passing multiple index arrays does something slightly different

arr = np.arange(32).reshape((8, 4))

arr 

arr[[1, 5, 7, 2], [0, 3, 1, 2]]

# ex:

arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]]

# ex: if you assign values with fancy indexing, the indexed values will be modified

arr[[1, 5, 7, 2], [0, 3, 1, 2]]

arr[[1, 5, 7, 2], [0, 3, 1, 2]] = 0

arr

# Transposing Arrays and Swapping Axes

# McKinney, Wes. Python for Data Analysis (p. 173). O'Reilly Media. Kindle Edition. 

arr = np.arange(15).reshape((3, 5))

arr

arr.T   # transpose 

# ex: compute the inner matrix product using numpy.dot:

arr = np.array([[0, 1, 0], [1, 2, -2], [6, 3, 2], [-1, 0, -1], [1, 0, 1]])

arr

np.dot(arr.T, arr)

# ex: @ infix operator is another way to do matrix mult:

arr.T @ arr

# Simple transposing with .T is a special case of swapping axes. ndarray has the method swapaxes,

# McKinney, Wes. Python for Data Analysis (p. 174). O'Reilly Media. Kindle Edition. 

arr

arr.swapaxes(0, 1)

'''
4.2 Pseudorandom Number Generation

McKinney, Wes. Python for Data Analysis (p. 175). O'Reilly Media. Kindle Edition. 
'''

