# [DS-02] What is Python?

## What is Python?

**Python** is a programming language, introduced in 1991. The latest version (when I'm writing this) is Python 3.10.0. To work with Python, you will pick an interface to a Python interpreter among the many available choices. You can have several instances of the interpreter, called **kernels**, running independently in your computer. 

Warning: Python is **case sensitive**. For instance, `type` is a Python function which returns the type of an object, but `Type` is not recognized (unless you create a new object with this name), and will return an error message.

## The Anaconda distribution

There are many distributions of Python. In the data science community, **Anaconda** (`anaconda.com`) is the favorite one. The current Anaconda distribution comes with Python 3.9. Downloading and installing Anaconda leaves you with the **Anaconda Navigator**, which opens in the browser and allows you to choose among different interfaces to the Python interpreter. 

Among the many interfaces offered by Anaconda, I recommend you the **Jupyter Qt console**, which is a shell-like app with some extra features. Jupyter (Julia/Python/R) is a new name for an older project called **IPython** (Interactive Python). IPython's contribution was the IPython shell, which added some features to the mere Python language. The Qt console is the result of adding a graphical interface (GUI), with drop-down menus, mouse-clicking, etc, to the IPython shell, with a toolkit called Qt.

Jupyter provides an alternative approach, based on the **notebook** concept. Though popular in data science courses, Jupyter notebooks are rarely used in web scraping jobs, though you can use them in this course if they make you feel more at home. Web scraping is difficult enough, so there is no need of adding extra hurdles.

Besides the Jupyter tools, Anaconda also provides a Python IDE (Integrated Development Environment) called **Spyder**, where you can manage a console and an text editor for your code. If you have previous experience with this type of interface, for instance from working with R in RStudio, you may prefer Spyder to the QtConsole.

Alternatively, you can bypass the navigator calling those interfaces in a **shell** app. To start the Qt console, enter `jupyter qtconsole`. To get access to the notebooks in the default browser, enter `jupyter notebook`. To start Spyder, enter ``spyder``.

*Note*. Use *Terminal* in Mac and *Anaconda Prompt* in Windows. Don't use the standard Windows prompt, because it will not find the Anaconda apps unless you specify the path.

## Python packages

Python is modular. When a kernel is started, only a few basic resources are available. Many additional resources can be added in the form of **modules**. A module is just a text file containing Python code. The **Python Standard Library** is a basic collection of modules included in any Python distribution. Some of them, like the module `re`, which provides regular expression operations, will appear in this course.

Modules are grouped in libraries, also called **packages**, because their elements are packed according to some specific rules which allow you to install and call them together. Plain Python can be extended by more than 350,000 packages. 

Since plain Python (without any extra module) is quite limited, you will need additional resources for practically everything. For instance, suppose that you want to do some math, calculating the square root of 2. You will then **import** the module `math`, included in the standard library, whose resources include the square root and many other mathematical functions. Once the module has been imported, all its functions are available. You can then apply the function `math.sqrt`. This notation indicates that `sqrt` is a function of the module `math`.

Modules are imported just for the current kernel. You finish the session by either closing or restarting the kernel. The Anaconda distribution contains many packages, besides the standard library, in particular those which are most popular among data scientists. With Anaconda, most packages used in this course are already available and can be directly imported. If it were not the case, you would have to **install** the package (only once). There is a basic installation procedure in Python, which uses a **package installer** called **pip** (see `pypi.org/project/pip`). You don't need this in this course if you use the Anaconda distribution.

**Pandas** (2008) is a popular library for data management, used in all the examples of this course. Pandas is built on top of two older libraries, NumPy and Matplotlib. **NumPy** (1995) is a library for dealing with vectors and matrices, called there **arrays**. **Matplotlib** is a graphics library, based on NumPy.

## Data types

The **data types** in Python are similar to those of other languages. The data type can be learned with the function `type`. Let me review the main data types:

* First, we have **integer numbers** (type `int`). There are subdivisions of this basic type, such as `int64`, but you don't need to know about that to start using Python.

* We can also have **floating-point** numbers (type `float`), that is, numbers with decimals. We also have subdivisions here, such as `float64`.

* Under type `bool`, Python admits **Boolean** values, which are either `True` or `False`.

* Besides numbers, we can also manage **strings**, with type `str`.

## Data containers

Python has various **data container** types. The most versatile is the **list**, which is represented as a sequence of comma-separated values inside square brackets:

```
`mylist = ['Messi', 'Cristiano', 'Neymar', 'Coutinho']`
```

An item is extracted from a list by indicating its place between square brackets. For instance, `mylist[1]` would return `'Cristiano'` (in Python we start at zero). To extract a sublist with several consecutive terms, we indicate the corresponding range. For instance, `mylist[1:3]` returns the sublist `['Cristiano', 'Neymar']` (in Python, the left limit is included but the right limit is not).

A **range** is like a sequence of integers, but the terms of the sequence are not saved as in a list. Instead, only the procedure to create the sequence is saved. The syntax is:

`myrange = range(start, end, step)`

If the step is omitted, it is assumed to be `step=1`. If the start is also omitted, it is assumed to be `start=0`.

A **dictionary** is a set of **pairs key/value**. For instance, the following dictionary contains three features of an individual:

`mydict = {'name': 'Joan', 'gender': 'F', 'age': 32}`

An item is extracted from a dictionary using the corresponding key. For instance, `mydict['name']` would return `'Joan'`. 

The packages used in data science come with new data container types: NumPy arrays, Pandas series and Pandas data frames. Dealing with so many types of objects is a bit challenging for the beginner. The elements of the Python data containers (eg lists) can have different data types, but NumPy and Pandas data containers have consistency constraints. So, an array has a unique data type, while a data frame has a unique data type for every column.

## Functions

A **function** takes a collection of **arguments** and performs an action. The functions that appear in this course will **return** a value. For instance, `len(mylist)` returns `4`. In addition to the built-in functions (such as `len` or `int`) and those coming in the packages that you may import (such as `math.sqrt`), you can define your own functions. The definition will work only for the current kernel. If you are happy with your function, you will save it in a source file for future use.

A simple example of a user-defined function would be:

`def f(x): return 1/(1 - x**2)`

Longer definitions can involve several lines of code. In that case, all the lines after the colon must be *indented*. Jupyter interfaces create the indentation automatically when we press the *Return* key after
