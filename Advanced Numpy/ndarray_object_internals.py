"""
Appendix A. Advanced NumPy

McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 
"""

import numpy as np

ints = np.ones(10, dtype=np.uint16)
floats = np.ones(10, dtype=np.float32)
np.issubdtype(ints.dtype, np.integer)
np.issubdtype(floats.dtype, np.floating)

# you can see the parent type of a specific data type by calling the type's mro method

np.float64.mro()

# therefore, we have:

np.issubdtype(ints.dtype, np.number)