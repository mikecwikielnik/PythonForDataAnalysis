"""
Chapter 3. Built-In Data Structures, Functions, and Files

McKinney, Wes. Python for Data Analysis (p. 84). O'Reilly Media. Kindle Edition. 
"""

# 3.1 Data Structures and Sequences

# McKinney, Wes. Python for Data Analysis (p. 84). O'Reilly Media. Kindle Edition. 

# Python data structure workhorses: tuples, lists, dictionaries, and sets

# Tuple

# McKinney, Wes. Python for Data Analysis (p. 84). O'Reilly Media. Kindle Edition. 

tup = (4, 5, 6)

# or you can type it like this:

tup = 4, 5, 6

# you can invoke a tuple like this:

tuple([4, 0, 2])

tup = tuple('string')
tup

# When you’re defining tuples within more complicated expressions, 

# it’s often necessary to enclose the values in parentheses, as in this example of creating a tuple of tuples:

# McKinney, Wes. Python for Data Analysis (p. 86). O'Reilly Media. Kindle Edition. 

nested_tup = (4, 5, 6), (7, 8)

nested_tup
nested_tup[0]
nested_tup[1]

# if an object inside a tuple is mutable (like list, etc), you can modify in place:

tup = tuple(['foo', [1, 2], True])

tup[1].append(3)
tup

# unpacking tuples

tup = (4, 5, 6)

a, b, c = tup
b

# nested tuples can be unpacked

tup = 4, 5, (6, 7)

a, b, (c, d) = tup
d

# swapping variable names

d, a = a, d
a

# a loop for unpacking

seq = [(1,2,3), (4,5,6), (7,8,9)]

for a, b, c in seq:
    print(f'a={a}, b={b}, c={c}')
    

# count is available for tuples or lists

a = (1,2,5,5,5)

a.count(5)

