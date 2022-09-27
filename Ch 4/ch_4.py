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
from re import X
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

from random import normalvariate

samples = np.random.standard_normal(size=(4, 4))

samples

# numpy.random is well over an order of magnitude faster for generating v lg samples:

# Table 4-3. NumPy random number generator methods

# McKinney, Wes. Python for Data Analysis (p. 176). O'Reilly Media. Kindle Edition. 

rng = np.random.default_rng(seed=12345)

data = rng.standard_normal((2, 3))

'''
4.3 Universal Functions: Fast Element-Wise Array Functions

McKinney, Wes. Python for Data Analysis (p. 177). O'Reilly Media. Kindle Edition. 
'''

# ex: many ufuncs are simple element-wise transformations, like numpy.sqrt or numpy.exp:

arr = np.arange(10)

arr

np.sqrt(arr)

np.exp(arr)

# ex: numpy.add or numpy.maximum, takes two arrays (binary ufuncs) & return a single array

x = rng.standard_normal(8)

y = rng.standard_normal(8)

x

y

np.maximum(x, y)

# See Tables 4-4 and 4-5 for a listing of some of NumPy’s ufuncs.

# McKinney, Wes. Python for Data Analysis (p. 180). O'Reilly Media. Kindle Edition. 

'''
4.4 Array-Oriented Programming with Arrays

McKinney, Wes. Python for Data Analysis (p. 182). O'Reilly Media. Kindle Edition. 
'''

# ex: evaluate the function sqrt(x^2 + y^2) across a regular grid of values

points = np.arange(-5, 5, 0.01)     # 100 equally spaced points

xs, ys = np.meshgrid(points, points)

ys

# evaluating the function is a matter of writing the same expression you would write with two points:

# McKinney, Wes. Python for Data Analysis (p. 183). O'Reilly Media. Kindle Edition.

z = np.sqrt(xs ** 2 + ys ** 2)

z

# ex: matplotlib to create visualization of this two-dimensional array:

import matplotlib.pyplot as plt

plt.imshow(z, cmap=plt.cm.gray, extent=[-5, 5, -5, 5])

plt.colorbar()

plt.title("Image plot of $\sqrt{x^2 + y^2} for a grid of values")

plt.show()  # the book doesn't include this, and you got it on the first try! 

# Expressing Conditional Logic as Array Operations

# McKinney, Wes. Python for Data Analysis (p. 186). O'Reilly Media. Kindle Edition. 


# ex: boolean array and two arrays of values

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])

yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])

cond = np.array([True, False, True, True, False])

# A list comprehension might look like this:

result = [(x if c else y)
          for x, y, c in zip(xarr, yarr, cond)]

result

# the ex above has problems 1) not fast for lg arrays (see loops) 2) won't work for multidimensional arrays

result = np.where(cond, xarr, yarr)

result

# A typical use of where in data analysis is to produce a new array of values based on another array.

# McKinney, Wes. Python for Data Analysis (p. 187). O'Reilly Media. Kindle Edition. 

# ex Suppose you had a matrix of randomly generated data and 

# you wanted to replace all positive values with 2 and all negative values with –2. 

# This is possible to do with numpy.where:

# McKinney, Wes. Python for Data Analysis (p. 187). O'Reilly Media. Kindle Edition. 

arr = rng.standard_normal((4, 4))

arr

arr > 0

np.where(arr > 0, 2, -2)

# ex: replace all pos values in arr with the constant 2

np.where(arr > 0, 2, arr)   # set only positive values to 2

# Mathematical and Statistical Methods

# McKinney, Wes. Python for Data Analysis (p. 188). O'Reilly Media. Kindle Edition. 

# ex: generate some normally distributed random data and compute some aggregate statistics:

arr = rng.standard_normal((5, 4))   #RC Cola

arr

arr.mean()

np.mean()

arr.sum()

arr.mean(axis=1)

arr.sum(axis=0)

# Here, arr.mean(axis=1) means “compute mean across the columns,” where arr.sum(axis=0) means “compute sum down the rows.”

# McKinney, Wes. Python for Data Analysis (p. 189). O'Reilly Media. Kindle Edition. 

# ex: cumsum & cumprod don't aggregate, instead producing an array of the intermediate results;

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])

arr.cumsum()

# ex: arr.cumsum(axis=0) computes cumulative sum down the rows. While arr.cumsum(axis=1) computes along the columns:

arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

arr     # lines 494 - 496 should be second nature to you

arr.cumsum(axis=0)

arr.cumsum(axis=1)

# scratch

pArr = np.array([[1, 1, 1], [5, 5, 5], [3, 3, 3]])

pArr

pArr.T  # transpose! hehe

pArr.cumsum(axis=0)

pArr.cumsum(axis=1)     # interesting results!

ppArr = pArr.T

ppArr.cumsum(axis=0)

ppArr.cumsum(axis=1)    # even more interesting results!

# Table 4-6. Basic array statistical methods

# McKinney, Wes. Python for Data Analysis (p. 190). O'Reilly Media. Kindle Edition. 

# Methods for Boolean Arrays

# McKinney, Wes. Python for Data Analysis (p. 191). O'Reilly Media. Kindle Edition. 

# ex: this is a nice example

arr = rng.standard_normal(100)  # seems like the way to generate n random elements

(arr > 0).sum()     # Number of positive values

(arr <= 0).sum()    # Number of non-positive values

# ex: any tests whether one or more values are True, while all checks if every value is True

bools = np.array([False, False, True, False])

bools.any()

bools.all()

# above can work with non-boolean arrays, where nonzero elements are treated as True

# Sorting

# McKinney, Wes. Python for Data Analysis (p. 192). O'Reilly Media. Kindle Edition. 

arr = rng.standard_normal(6)

arr 

arr.sort()

arr

# ex: arr.sort(axis=0) sorts within each column, while arr.sort(axis=1) sorts across each row

arr = rng.standard_normal((5, 3))

arr

arr.sort(axis=0)

arr

# make sure you look at the top row to see the nuance. Don't look for max/min values

arr.sort(axis=1)

arr

# ex: sorting a list?

arr2 = np.array([5, -10, 7, 1, 0, -3])

sorted_arr2 = np.sort(arr2)

sorted_arr2

# Unique and Other Set Logic

# McKinney, Wes. Python for Data Analysis (p. 194). O'Reilly Media. Kindle Edition. 

