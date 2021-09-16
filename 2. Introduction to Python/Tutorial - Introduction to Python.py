## Tutorial - Introduction to Python ##

# Typing Python code #
2 + 2               # In [1]
a = 2 + 2           # In [2]
a                   # In [3]
b = 2 * 3           # In [4]
b - 1
b**2

# Python packages #
import math         # In [5]
math.sqrt(2)
from math import * # In [6]
sqrt(2)

# Numeric types #
type(a)             # In [7]
b = math.sqrt(2)    # In [8]
type(b)
type(2)             # In [9]
type(2.0)           # In [10]
float(2)            # In [11]
int(2.3)            # In [12]

# Boolean variables #
d = 5 < a           # In [13]
d
type(d)             # In [14]
a == 4              # In [15]
math.sqrt(d)        # In [16]
1 - d               # In [17]

# Strings #
c = 'Messi'         # In [18]
type(c)

# Lists #
mylist = ['Messi', 'Cristiano', 'Neymar', 'Coutinho']    # In [19]
len(mylist)                                              # In [20]
newlist = mylist + [2, 3]                                # In [21]
newlist
len(newlist)                                        # In [22]
mylist[0:2]                                         # In [23]
mylist[3:]                                          # In [24]
mylist[:3]                                          # In [25]

# Other data containers #
set(newist)                                        # In [26]
list(set([1, 0, 1, 0, 7]))                         # In [27]
mytuple = tuple(mylist)                            # In [28]
mytuple
muylist[3] = 'Griezmann'                           # In [29]
muylist
mytuple[3] = 'Griezmann'                           # In [30]
mytuple
my_dict = {'name': 'Joan', 'gender': 'F', 'age': 32}   # In [31]
my_dict.keys()                                         # In [32]
my_dict['name']                                        # In [33]

# Functions #
def f(x):                                   # In [34]
    y = 1/(1 - x**2)
    return(y)
f(2)                                        # In [35]
f(1)                                        # In [36]
f('Mary')                                   # In [37]
def g(x, y): return x*y/(x**2 + y**2)       # In [38]
g(1, 1)
f = lambda x: 1/(1 - x**2)                  # In [39]
