"""
Chapter 3. Built-In Data Structures, Functions, and Files

McKinney, Wes. Python for Data Analysis (p. 84). O'Reilly Media. Kindle Edition. 
"""

"""
3.1 Data Structures and Sequences

McKinney, Wes. Python for Data Analysis (p. 84). O'Reilly Media. Kindle Edition. 
"""
# Python data structure workhorses: tuples, lists, dictionaries, and sets

'''
Tuple

McKinney, Wes. Python for Data Analysis (p. 84). O'Reilly Media. Kindle Edition. 
'''

from audioop import reverse


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

'''
Dictionary

McKinney, Wes. Python for Data Analysis (p. 96). O'Reilly Media. Kindle Edition. 
'''

empty_dict = {}

d1 = {
    "a": "some value",
    "b": [1, 2, 3, 4]
}

# access, insert, or set elements (you can use this syntax for list/tuple)

d1[7] = "an integer"

d1 

d1["b"]

# check if key exists in dictionary (you can use this syntax for list/tuple)

"b" in d1

# delete values with del or pop method(simultaneously returns the value and deletes the key)

d1[5] = "some value"

d1

d1["dummy"] = "another value"

d1

del d1[5] # d1[key]

d1

ret = d1.pop("dummy")   # removes dummy/ pop removes item at specified location

ret

d1

# Creating dictionaries from sequences

# A dictionary is essentially a collection of 2-tuples, the dict fn accepts a list of 2-tuples:

tuples = zip(range(5), reversed(range(5)))

tuples

mapping = dict(tuples)

mapping

# Default values

# a common thread of logic:

# if key in some_dict:
#     value = some_dict[key]
# else:
#     value = default_value
    
# get and pop can take a default value to be returned, so that the above if-else block can be written simply as:

# McKinney, Wes. Python for Data Analysis (p. 100). O'Reilly Media. Kindle Edition. 

# value = some_dict.get(key, defaul_Value)

# ex: categorize a list of words by their 1st letters as a dict of lists

words = ["apple", "bat", "bar", "atom", "book"]

by_letter = {}

for word in words:
    letter = word[0]
    if letter not in by_letter:
        by_letter[letter] = [word]
    else:
        by_letter[letter].append(word)
        
by_letter

# the preceding for loop can be written like:

by_letter = {}

for word in words:
    letter = word[0]
    by_letter.setdefault(letter, []).append(word)
    
by_letter

# defaultdict

from collections import defaultdict

by_letter = defaultdict(list)

for word in words:
    by_letter[word[0]].append(word)
    
'''
Set

McKinney, Wes. Python for Data Analysis (p. 103). O'Reilly Media. Kindle Edition. 
'''

set([2, 2, 2, 1, 3, 3])     # a

{2, 2, 2, 1, 4, 3}  # b

# set operations: union, intersection, difference, and symmetric difference

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}

# union

a.union(b)
a|b

# intersection

a.intersection(b)
a&b

# Table 3-1. Python set operations

# McKinney, Wes. Python for Data Analysis (p. 104). O'Reilly Media. Kindle Edition. 

# This citation is for reference. 

# in-place counterparts

c = a.copy()

c |= b

c

d = a.copy()

d &= b

d

# to store list-like elements* in a set, you can convert them to tuples:

my_data = [1, 2, 3, 4]

my_set = {tuple(my_data)}

my_set

# verify work

a_set = {1, 2, 3, 4, 5}

{1, 2, 3}.issubset(a_set)
a_set.issuperset({1, 2, 3})

# equality

{1, 2, 3} == {3, 2, 1}

'''
Built-In Sequence Functions

McKinney, Wes. Python for Data Analysis (p. 107). O'Reilly Media. Kindle Edition. 
'''

# enumerate

index = 0

# for value in collection:
#     # do something with value
#     index += 1
    
# Since this is so common, Python has a built-in function, 
# enumerate, which returns a sequence of (i, value) tuples:

# McKinney, Wes. Python for Data Analysis (p. 107). O'Reilly Media. Kindle Edition. 

# for index, value in enumerate(collection):
#     # do something with value

# sorted

sorted([1,2,3])

sorted("horse race")

# zip

seq1 = ["foo", "bar", "baz"]

seq2 = ["one", "two", "three"]

zipped = zip(seq1, seq2)

list(zipped)

# ex:

seq3 = [False, True]

list(zip(seq1, seq2, seq3))

# a common use of zip is 
# simultaneously iterating over multiple sequences,
# possibly also combined with enumerate:

for index, (a, b) in enumerate(zip(seq1, seq2)):
    print(f"{index}: {a}, {b}")
    
# reversed

list(reversed(range(5)))

'''
List, Set, and Dictionary Comprehensions

McKinney, Wes. Python for Data Analysis (p. 109). O'Reilly Media. Kindle Edition. 
'''

# [expr for value in collection if condition]

# is equivalent to:
    
# result = []
# for value in collection:
#     if condition:
#         result.append(expr)

# ex:

strings = ["a", "as", "bat", "car", "dove", "python"]

[x.upper() for x in strings if len(x) > 2]

# ex:

unique_lengths = {len(x) for x in strings}

unique_lengths

# ex: map function

set(map(len, strings))

# ex: 

loc_mapping = {value: index for index, value in
               enumerate(strings)}

loc_mapping

# nested list comprehensions

all_data = [["john", "emily", "mike", "mary", "steven"],
            ["maria", "saul", "javier", "natalie", "pilar"]]

names_of_interest = []

for names in all_data:
    enough_as = [name for name in names if name.count("a") >= 2]    # this is a list comprehension
    names_of_interest.extend(enough_as)
    
names_of_interest

# a single nested list comprehension:

result = [name for names in all_data for name in names
          if name.count("a") >= 2]

result

# ex:

some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

flattened = [x for tup in some_tuples for x in tup]

flattened 

'''
3.2 Functions

McKinney, Wes. Python for Data Analysis (p. 113). O'Reilly Media. Kindle Edition. 
'''