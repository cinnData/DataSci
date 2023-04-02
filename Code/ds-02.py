## [DS-02] Introduction to Python ##

# Typing Python code #
2 + 2
a = 2 + 2
a
a = 7 - 2
a
b = 2 * 3
b - 1
b**2

# Python packages #
import math
math.sqrt(2)
from math import sqrt
sqrt(2)

# Numeric types #
type(a)
b = math.sqrt(2)
type(b)
type(2)
type(2.0)
float(2)
int(2.3)

# Boolean data #
d = 5 < a
d
type(d)
a == 4
math.sqrt(d)
1 - d

# Strings #
c = 'Messi'
type(c)

# Lists #
mylist = ['Messi', 'Cristiano', 'Neymar', 'Coutinho']
len(mylist)
newlist = mylist + [2, 3]
newlist
len(newlist)
mylist[0:2]
mylist[2:]
mylist[:3]

# Ranges #
myrange = range(0, 10, 2)
list(myrange)
list(range(5, 12))
list(range(10))

# Dictionaries #
my_dict = {'name': 'Joan', 'gender': 'F', 'age': 32}
my_dict.keys()
my_dict['name']

# Functions #
def f(x):
    y = 1/(1 - x**2)
    return y
f(2)
f(1)
f('Mary')
def g(x, y): return x*y/(x**2 + y**2)
g(1, 1)

# For loops #
squares = []
for i in range(1, 5):
    squares = squares + [i**2]
squares
squares = [i**2 for i in range(1, 5)]
squares
[len(name) for name in mylist]

# If statements #
if 3 < 5:
    print('Minor')
else:
    print('Major')
if math.sqrt(1) < 1:
    print('Minor')
elif math.sqrt(1) == 1:
    print('Equal')
else:
    print('Major')
[len(name) for name in mylist if name[0] != 'M']
