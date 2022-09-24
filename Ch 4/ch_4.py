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

