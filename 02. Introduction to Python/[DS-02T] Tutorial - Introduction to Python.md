# [DS-02T] Tutorial - Introduction to Python

## Typing Python code

This tutorial assumes that you are using the Jupyter Qt console, but almost everything is also valid in other interfaces, with minor adjustments. When you start the console, it opens a window where you can type or paste your code. You can resize the window and zoom inside it as in many other applications. 

The console can have several tabs open, just as a browser. To open a new tab, enter either *Cmd+T* (Macintosh) or *Ctrl+T* (Windows), or use the menu *File >> New tab with New Kernel*. Every tab is an interface between you and a Python kernel. These kernels run independently. You can interrupt a running process with *Ctrl+C* or restart a kernel in the same tab with *Ctr+.*.

The console produces input prompts (such as `In[1]:`), where you can type a command and press `Return`. Then Python returns either an output (preceded by `Out[1]:`), a (typically long and difficult) error message, or no answer at all. Here is a supersimple example:

```
In [1]: 2 + 2
Out[1]: 4
```

So, if you enter `2 + 2`, the output will be the result of this calculation. But, when you want to store this result for later use (in the same session), you enter it with a name, as follows:

```
In [2]: a = 2 + 2
```

This creates the **variable** `a`. Note that the value of `2 + 2` is not outputted now. But you can call it:

```
In [3]: a
Out[3]: 4
```

In Pyhton, when you assign a value to a variable that has already been created, the previous assignment is forgotten. So:

```
In [4]: a = 7 - 2

In [5]: a
Out[5]: 5
```

If you copypaste in the console code chunks that you edit in a text editor, you can input several code lines at once. In that case, you will only get the output for the last line. If the cursor is not at the end of the last line, you have to press *Shift+Return* to get the output. Here is a simple example:

```
In [6]: b = 2 * 3
   ...: b - 1
   ...: b**2
Out[6]: 36
```

*Note*. You would probably have written `b^2` for the square of 2, but the caret symbol (`^`) plays a different role in Python.

## Python packages

When you start a new kernel, only a minimal part of the resources coming in your Python distribution will be available. Since this part is quite limited, you will need additional resources for practically everything. These extra resources come in **packages**.

For instance, suppose that you want to do some math involving the square root of 2. You will then **import** the package `math`, which includes the square root and many other mathematical functions. Once the package has been imported, all its functions are available. So, you can apply the **function** `math.sqrt`. This notation indicates that `sqrt` is a function from the package `math`. In the console, the square root calculation shows up as:

```
In [5]: import math
   ...: math.sqrt(2)
Out[5]: 1.4142135623730951
```

Alternatively, you can import only the functions that you plan to use:

```
In [8]: from math import sqrt
   ...: sqrt(2)
Out[8]: 1.4142135623730951
```

Note that packages are imported just for the current kernel. You can only import a package only if it is already installed in your computer. `math` is part of the **Python Standard Library**, so you have it for sure.

## Numeric types

As in other languages, data can have different **data types** in Python. The data type can be learned with the function `type`. Let me start with the numeric types. For the variable `a` defined above:

```
In [9]: type(a)
Out[9]: int
```

So, `a` has type `int` (meaning integer). Another numeric type is that of **floating-point** numbers (`float`), which have decimals:

```
In [10]: b = math.sqrt(2)
type(b)
Out[10]: float
```

There are subdivisions of these two basic types (such as `int64`), but I skip them in this brief tutorial. Note that, in Python, integers are not, as in the mathematics textbook, a subset of the real numbers, but a different type:

```
In [11]: type(2)
Out[11]: int
```

```
In [12]: type(2.0)
Out[12]: float
```

In the above square root calculation, `b` got type `float` because this is what the `math` function `sqrt` returns. The functions `int` and `float` can be used to convert numbers from one type to another type (sometimes at a loss):

```
In [13]: float(2)
Out[13]: 2.0
```

```
In [14]: int(2.3)
Out[14]: 2
```

## Boolean data

We also have **Boolean** (`bool`) variables, whose value is either `True` or `False`:

```
In [15]: d = 5 < a
    ...: d
Out[15]: False
```

```
In [16]: type(d)
Out[16]: bool
```

Even if they don't appear explicitly, Booleans are always under the hood. When you enter an expression involving a comparison such as `5 < a`, the Python interpreter evaluates it, returning either `True` or `False`.  Here, I have defined a variable by means of such an expression, so I got a Boolean variable. Warning: as a comparison operator, equality is denoted by two equal signs. This may surprise you.

```
In [17]: a == 4
Out[17]: True
```

Boolean variables can be converted to `int` and `float` type with the functions mentioned above, but also by applying a mathematical operator:

```
In [18]: math.sqrt(d)
Out[18]: 0.0
```

```
In [19]: 1 - d
Out[19]: 1
```

## Strings

Besides numbers, we can also manage **strings** with type `str`:

```
In [20]: c = 'Messi'
    ...: type(c)
Out[20]: str
```

The quote marks indicate type `str`. You can use single or double quotes, but take care of using the same on both sides of the string. Strings come in Python with many methods attached. These methods will be discussed later in this course.

## Lists

Python has several types for objects that work as **data containers**. The most versatile is the **list**, which is represented as a sequence of comma-separated values inside square brackets. Lists can contain items of different type. A simple example of a list, of length 4, follows.

```
In [21]: mylist = ['Messi', 'Cristiano', 'Neymar', 'Coutinho']
```

```
In [22]: len(x)
Out[22]: 4
```

Lists can be concatenated in a very simple way in Python:

```
In [23]: newlist = mylist + [2, 3]
    ...: newlist
Out[23]: ['Messi', 'Cristiano', 'Neymar', 'Coutinho', 2, 3]
```

Now, the length of `newlist` is 6:

```
In [24]: len(newlist)
Out[24]: 6
```

The first item of `mylist` can be extracted as `mylist[0]`, the second item as `mylist[1]`, etc. The last item can be extracted either as `mylist[3]` or as `mylist[-1]`. Sublists can be extracted by using a colon inside the brackets, as in:

```
In [25]: mylist[0:2]
Out[25]: ['Messi', 'Cristiano']
```

Note that `0:2` includes `0` but not `2`. This is a general rule for indexing in Python. Other examples:

```
In [26]: mylist[2:]
Out[26]: ['Neymar', 'Coutinho']
```

```
In [27]: mylist[:3]
Out[27]: ['Messi', 'Cristiano', 'Neymar']
```

The items of a list are ordered, and can be repeated. This is not so in other data containers.

## Ranges

A **range** is a sequence of integers which in many aspects works as a list, but the terms of the sequence are not saved as in a list. Instead, only the procedure to create the sequence is saved. The syntax is `range(start, end, step)`. Example:

```
In [28]: myrange = range(0, 10, 2)
    ...: list(myrange)
Out[28]: [0, 2, 4, 6, 8]
```

Note that the items from a range cannot printed directly. So, I have converted the range to a list here with the function `list`. If the step is omitted, it is assumed to be 1:

```
In [29]: list(range(5, 12))
Out[29]: [5, 6, 7, 8, 9, 10, 11]
```

If the start is also omitted, it is assumed to be 0:

```
In [30]: list(range(10))
Out[30]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Dictionaries

A **dictionary** is a set of **pairs key/value**. For instance, the following dictionary contains three features of an individual:

```
In [31]: my_dict = {'name': 'Joan', 'gender': 'F', 'age': 32}
```

The keys can be listed:

```
In [32]: my_dict.keys()
Out[32]: dict_keys(['name', 'gender', 'age'])
```

In the dictionary, a value is not extracted using an index which indicates its order in a sequence, as in the list, but using the corresponding key:

```
In [33]: my_dict['name']
Out[33]: 'Joan'
```

##  Functions

A **function** takes a collection of **arguments** and performs an action. Let me present a couple of examples of value-returning functions. They are easily distinguished from other functions, because the definition's last line is a `return` clause. 

A first example follows. Note the **indentation** after the colon, which is created automatically by the console.

```
In [34]: def f(x):
    ...:     y = 1/(1 - x**2)
    ...:     return y
```

When we define a function, Python just takes note of the definition, accepting it when it is syntactically correct (parentheses, commas, etc). The function can be applied later to different arguments.

```
In [35]: f(2)
Out[35]: -0.3333333333333333
```

If we apply the function to an argument for which it does not make sense, Python will return an error message which depends on the values supplied for the argument.

```
In [36]: f(1)
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-34-281ab0a37d7d> in <module>
----> 1 f(1)

<ipython-input-32-4f34043eb656> in f(x)
      1 def f(x):
----> 2     y = 1/(1 - x**2)
      3     return(y)

ZeroDivisionError: division by zero
```

```
In [37]: f('Mary')
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-35-8547eae46f78> in <module>
----> 1 f('Mary')

<ipython-input-32-4f34043eb656> in f(x)
      1 def f(x):
----> 2     y = 1/(1 - x**2)
      3     return(y)

TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
```

Functions can have more than one argument, as in:

```
In [38]: def g(x, y): return x*y/(x**2 + y**2)
    ...: g(1, 1)
Out[38]: 0.5
```

Note that, in the definition of `g`, I have used a shorter way. Most programmers would make it longer, as I did previously for `f`. 
