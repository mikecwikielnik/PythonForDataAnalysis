"""
Chapter 9. Plotting and Visualization

McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 
"""

# 9.1 A Brief matplotlib API Primer

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

# ex: a line plot

data = np.arange(10)

data

plt.plot(data)  # run in interactive window...aka jupyter nb

data2 = np.arange(35)

data2

plt.plot(data2)     # same here

# Figures and Subplots

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# plots in matplotlib reside in a figure object

import matplotlib.pyplot as plt     # nuance of interactive nb, you have to do this everytime

fig = plt.figure()

# you have to create one or more sub plots using add_subplots

ax1 = fig.add_subplot(2, 2, 1)

# this means that the figure should be 2x2 (so up to four plots in total)

ax2 = fig.add_subplot(2, 2, 2)

ax3 = fig.add_subplot(2, 2, 3)

# plt.show()  # for the terminal, it seems you have to run this separately

# ex: making a line plot with the plot method

ax3.plot(np.random.standard_normal(50).cumsum(), color="black", linestyle="dashed")

# plt.show()  # remember just ONE plt.show()

ax1.hist(np.random.standard_normal(100), bins=20, color="black", alpha=0.3);

ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.standard_normal(30));

plt.show()

# Adjusting the spacing around subplots

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

