"""
Appendix A. Advanced NumPy

McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 
"""

# reshaping arrays

# ex: suppose we had a 1D array of values that we wished to rearrange into a matrix

import numpy as np

arr = np.arange(8)

arr

arr.reshape((4, 2)) # rc cola

# a multi-dimensional array can also be reshapped

arr.reshape((4, 2)).reshape((2, 4))

# one of the dimensions can be -1, 
# which the value used for that dim will be inferred from the data

arr = np.arange(15)

arr.reshape((5, -1))

# since an array is a tuple, it can be passed to reshape too

other_arr = np.ones((3, 5))

other_arr.shape

arr.reshape(other_arr.shape)