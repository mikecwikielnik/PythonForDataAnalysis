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