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

import matplotlib.pyplot as plt   
import numpy as np

fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
for i in range(2):
    for j in range(2):
        axes[i, j].hist(np.random.standard_normal(500), bins=50, color="black", alpha=0.5)

fig.subplots_adjust(wspace=0, hspace=0)

# Colors, Markers, and Line Styles

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: to plot x versus y with green dashes:

# ax.plot(x, y, linestyle="--", color="green")

# ex: more styling options

fig = plt.figure()

ax = fig.add_subplot()

ax.plot(np.random.standard_normal(30).cumsum(), color="black", linestyle="dashed", marker="o");

plt.show()

# ex: drawstyle option

fig = plt.figure()

ax = fig.add_subplot()

data = np.random.standard_normal(30).cumsum()

ax.plot(data, color="black", linestyle="dashed", label="Default");
ax.plot(data, color="black", linestyle="dashed", drawstyle="steps-post", label="stephs-post");
ax.legend()

# Ticks, Labels, and Legends

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# Setting the title, axis labels, ticks, and tick labels

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

fig, ax = plt.subplots()    # fig is the canvas (axis included) if u will // ax is the data

ax.plot(np.random.standard_normal(1000).cumsum());

# to change the x-axis ticks, use set_xticks and set_xticklabels

ticks = ax.set_xticks([0, 250, 500, 750, 1000])

labels = ax.set_xticklabels(["one", "two", "three", "four", "five"], rotation=30, fontsize=8)

# set_xlabel gives a name to the x-axis and set_title is the subplot title

ax.set_xlabel("Stages")

ax.set_title("My first matplotlib plot")

ax.set(title="My first matplotlib plot", xlabel="Stages")   # is another way to write it

# Adding legends

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: easiest way is to pass the label arg when adding each piece of the plot

fig, ax = plt.subplots()    # fig == canvas, ax == data

ax.plot(np.random.standard_normal(1000).cumsum(), color="black", label="one");
ax.plot(np.random.standard_normal(1000).cumsum(), color="black", linestyle="dashed", label="two");
ax.plot(np.random.standard_normal(1000).cumsum(), color="black", linestyle="dotted", label="three");

ax.legend()

# Annotations and Drawing on a Subplot

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ax.text(x, y, "Hello world!", family="monospace", fontsiz=10)

# ex: plot the closing s&p 500 index 

from datetime import datetime
import pandas as pd

fig, ax = plt.subplots()

data = pd.read_csv("../book files/examples/spx.csv", index_col=0, parse_dates=True)
spx = data["SPX"]

spx.plot(ax=ax, color="black")

crisis_data = [
    (datetime(2007, 10, 11), "Peak of bull market"),
    (datetime(2008, 3, 12), "Bear Stearns fails"),
    (datetime(2008, 9, 15), "Lehman Bankruptcy")
]

for date, label in crisis_data:
    ax.annotate(label, xy=(date, spx.asof(date) + 75),
                xytext=(date, spx.asof(date) + 225),
                arrowprops=dict(facecolor="black", headwidth=4, width=2, headlength=4),
                horizontalalignment="left", verticalalignment="top")

# Zoom in on 2007 - 2010

ax.set_xlim(["1/1/2007", "1/1/2011"])
ax.set_ylim([600, 1800])
ax.set_title("Important dates in the 2008-2009 financial crisis")

# ex: to add a shape to a plot

fig, ax = plt.subplots()

rect = plt.Rectangle((0.2, 0.75), 0.4, 0.15, color="black", alpha=0.3)
circ = plt.Circle((0.7, 0.2), 0.15, color="Blue", alpha=0.3)
pgon = plt.Polygon([[0.15, 0.15], [0.35, 0.4], [0.2, 0.6]], color="green", alpha=0.5)

ax.add_patch(rect)
ax.add_patch(circ)
ax.add_patch(pgon)

# Saving Plots to File

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# ex: save an SVG version of a figure

fig.savefig("figpath.svg")

# matplotlib Configuration

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

plt.rc("figure", figsize=(10, 10))

# write it as a dictionary

plt.rc("font", family="monospace", weight="bold", size=9)

# 9.2 Plotting with pandas and seaborn

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# Line Plots

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

s = pd.Series(np.random.standard_normal(10).cumsum(), index=np.arange(0, 100, 10))

s.plot()

# ex:

df = pd.DataFrame(np.random.standard_normal((10, 4)).cumsum(0),
                columns=["A", "B", "C", "D"],
                index=np.arange(0, 100, 10))

plt.style.use('grayscale')

df.plot()

# Bar Plots

# McKinney, Wes. Python for Data Analysis . O'Reilly Media. Kindle Edition. 

# plot.bar() and plot.barh() // x (bar) or y (barh) ticks

fig, axes = plt.subplots(2, 1)

data = pd.Series(np.random.uniform(size=16), index=list("abcdefghijklmnop"))

data.plot.bar(ax=axes[0], color="black", alpha=0.7)

data.plot.barh(ax=axes[1], color="black", alpha=0.7)

# ex: with a df, bar plots group the values, side by side:

df = pd.DataFrame(np.random.uniform(size=(6, 4)),
                index=["one", "two", "three", "four", "five", "six"],
                columns=pd.Index(["A", "B", "C", "D"], name="Genus"))

df

df.plot.bar()   # genus is in the legend

df.plot.barh(stacked=True, alpha=0.5)   # very pretty

# ex: restaurant tipping

tips = pd.read_csv("../book files/examples/tips.csv")

tips.head()

party_counts = pd.crosstab(tips["day"], tips["size"])

party_counts

party_counts = party_counts.reindex(index=["Thur", "Fri", "Sat", "Sun"])    # capitalization matters here

party_counts

# remove 1 & 6 person parties

party_counts = party_counts.loc[:, 2:5]

# normalize so that each row sums to 1, and then plot. 

# normalize to sum to 1

party_pcts = party_counts.div(party_counts.sum(axis="columns"), axis="index")

party_pcts

party_pcts.plot.bar(stacked=True)   # gorgeous 

# ex: look at the pct of tipping by day w/ seaborn


import seaborn as sns

tips["tip_pct"] = tips["tip"] / (tips["total_bill"] - tips["tip"])

tips.head()

sns.barplot(x="tip_pct", y="day", data=tips, orient="h")    # v nice

# ex: seaborn.barplot has a hue option

sns.barplot(x="tip_pct", y="day", hue="time", data=tips, orient="h")    # another beaut

# ex: switch plot appearances using seaborn.set_style

sns.set_style("whitegrid")

sns.set_palette("Greys_r")
