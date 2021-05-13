# 2. Introduction to Python

### What is Python?

**Python** is a programming language, introduced in 1991. There are currently two versions of the Python language: Python 2 and Python 3. These notes use Python 3. Although beginners are currently adopting Python 3, there is a lot of Python 2 code still in circulation, in particular in the older editions of many books. Even if most of the Python 2 code runs in Python 3, one finds trouble from time to time. So, it is recommended to check Python's version before copypasting somebody else's code.

### The Anaconda distribution

There are many distributions of Python. In the data science community, **Anaconda** (`anaconda.com`) is the favorite one. The Anaconda distribution comes with most the packages used in these notes. Downloading and installing Anaconda (choose Python 3 when the choice is presented to you) will leave you with the **Anaconda Navigator**, which opens in the browser and allows you to choose among different interfaces to Python. Alternatively, once Anaconda is installed, you can bypass the navigator using a **command-line interface** (CLI), like Terminal on Mac computers or the Anaconda prompt on Windows.

Among the many interfaces offered by Anaconda, I recommend you the **Jupyter Qt console**, which is an input/output text interface. Jupyter (Julia/Python/R) is a new name for an older project called **IPython** (Interactive Python). IPython's contribution was the IPython shell, which added some features to the mere Python language. The Qt console is the result of adding a graphical interface (GUI), with drop-down menus, mouse-clicking, etc, to the IPython shell, by means of a toolkit called Qt.

Part of the popularity of the IPython shell was due to the **magic commands**, which are extra commands which are written as `%cmd`. For instance, `%cd` allows you to change the home directory. These commands are not part of Python. Some textbooks and tutorials are still very keen on magic commands, but others prefer to skip them. They are mentioned occasionally in these notes. To get more information about magic commands, enter `%quickref` in the console.

Jupyter provides an alternative approach, based on the **notebook** concept. In a notebook, you can combine input, output and ordinary text. In the notebook arena, **Jupyter Notebook** is the leading choice, followed by **Apache Zeppelin**. These two are multilingual, that is, they can be used with other languages, like R, besides Python. Jupyter has powerful supporters and very smart people in the development team, so we will probably see plenty of Jupyter notebooks in the immediate future. Most Pythonistas prefer the console for developing their code, but use notebooks for difusion, specially for posting their work on platforms like GitHub.

Besides the Jupyter tools, Anaconda also provides a Python IDE (Integrated Development Environment) called **Spyder**, where you can manage a console and an text editor for your code. If you have previous experience with this type of interface, for instance from working with R in RStudio, you may prefer Spyder to the QtConsole.

### Python packages

As said above, Python is a programming language to which many additional resources have been added in the form of **modules**. A module is just a text file containing Python code (extension `.py`). Modules are grouped in libraries. These libraries are also called **packages**, because their elements are packed according to some specific rules that allow you to install and call them together. Python can be extended by more than 200,000 packages. Some big packages, like scikit-learn, are not single modules, but collections of modules, which are then called **subpackages**.

Since the basic Python (without any package) is quite limited, you will need additional resources for practically everything. For instance, suppose that you want to do some math, and calculate the square root of 2. You will then **import** the package `math`, whose resources include the square root and many other mathematical functions. Once the package has been imported, all its functions are available. So, you can apply the **function** `math.sqrt`. This notation indicates that `sqrt` is a function of the module `math`.

Packages are imported just for the current session. You finish the session by either closing the console or by restarting the current kernel. You can do this with `Kernel >> Restart current Kernel` or by typing `Ctrl+.`.

If you use the Anaconda distribution, most packages used in these notes can be directly imported. If it is not the case, you have to **install** the package (only once). There is a basic installation procedure in Python, which uses a **package installer** called `pip` (see `pypi.org/project/pip`). Using `pip` you can have a conflict of versions between packages which are related, so I would recommend you to use an alternative installer called  `conda`, which cheks your Anaconda distribution and takes care of the conflicts. It can be run from the console as a magic command (`%conda`).

### The main packages

These notes do not look at Python as a programming language, that is, for developing software applications, but from a very specific perspective. Our approach is mainly based on four packages, NumPy, Matplotlib, Pandas and scikit-learn.

* **NumPy**, released in 1995, is a library adding support for large vectors and matrices.

* Based on NumPy, the library **Matplotlib** is Python's plotting workhorse. In these notes, it will be occasionally used for illustration.

* **Pandas** is a library for data management, inspired in the R language. Due to Pandas, Python's popularity has been growing steadily among data scientists. Current data science courses are typically based on either R or Python/Pandas.

* **scikit-learn**, released in 2008, is a library of machine learning methods. scikit-learn methods accept both NumPy arrays and but Pandas objects, but they always return NumPy arrays.

### Learning about Python

There are many books for learning about Python, but some of them would not be appropriate for learning how to work with data in Python. It can even happen that you do not find anything about data in many of them. Mind that Python has so many applications that the intersection of the know-how of all Python users is relatively narrow. For an introduction to Python as a programming language, in a computer science context, I would recommend Zelle (2010). For the self-learning data scientist, McKinney (2017) and VanderPlas (2017) are both worth their price. To those who are not afraid of manuals, I would recommend to go for them directly (they are free).

There is also plenty of learning materials in Internet, including MOOC's. For instance, **Coursera** has a pack of courses on Python (see `coursera.org/courses?query=python`). But, probably, the most attractive marketplace for data science courses is **DataCamp**. They offer, under subscription or academic license, an impressive collection of courses, most of them focused on either R or Python (there are also some on SQL). In addition to follow DataCamp courses, you can also benefit from the **DataCamp Community Tutorials**, which are free and cover a wide range of topics. Finally, a good place to start is `learningpython.org`.

### Data types

As in other languages, data can have different **data types** in Python. The type can be learned with the function `type`.

The main types are:

* First, we have **integer numbers** (type `int`). There are subdivisions of this basic type, such as `int64`, but you don't need to know about that to start your Python trip.

* We can also have **floating-point** numbers (type `float`), that is, numbers with decimals. We also have subdivisions here, such as `float64`.

* Under type `bool`, Python admits **Boolean** values, which are either `True` or `False`. In Python, Boolean variables are converted to type `int` or `float` by applying a mathematical operator. So, `True + 0` gives `1`, and `math.sqrt(True)` gives `1.0`. Warning: it is `True` and `False` in Python, but `TRUE` and `FALSE` in R. Mind that these languages are case sensitive.

* Besides numbers, we can also manage **strings**, with type `str`. Strings come in Python with many methods attached. They will be discussed, in the Pandas context, in a specific chapter.

* Python also has type `datetime` for dealing with **dates and times**. This will also be discussed later in a specific chapter.

### Data containers

Python has various **data container** classes, which are used to group together other values. The most versatile is the **list**, which is represented as a sequence of comma-separated values inside square brackets:

`mylist = ['Messi', 'Cristiano', 'Neymar', 'Coutinho']`

An element of a list (or a tuple) is extracted indicating its place between square brackets. For instance, `mylist[1]` would extract `'Cristiano'` (in Python we start at zero). To extract a sublist with several consecutive terms, we indicate the corresponding range. For instance, `mylist[1:3]` extracts the sublist `['Cristiano', 'Neymar']` (in Python, the left limit is included but the right limit is not). 

A **set** is represented in the same way as a list, but with curly braces replacing the square brackets:

`myset = {'Messi', 'Cristiano', 'Neymar', 'Coutinho'}`

A difference between the list and the set is that the elements of a set are not ordered, and repetition is ignored.

A **tuple** is like a list, represented with parentheses instead of square brackets:

`mytuple = ('Messi', 'Cristiano', 'Neymar', 'Coutinho')`

**Dictionaries** are relevant for data scientists, since they provide a simple way to manage data coming in a special format called JSON. In Python, JSON data are just read as a combination of dictionaries and lists.

The following dictionary contains three features of an individual:

`mydict = {'name': 'Joan', 'gender': 'F', 'age': 32}`

A dictionary looks like a set, but the elements are **pairs key/value**.

### Functions

Python is a fully functional language. Part of its power comes from the ability to define the operations that we wish to perform as **functions**, so they can be applied many times. Besides the built-in functions (those available in Python) and those coming in the packages that you may import, you can define your own functions. The definition will be forgotten when the session is closed, so you have to include the definition in your code.

A simple example of a user-defined function follows. Note the indentation after the colon.

`def f(x): return 1/(1 - x**2)`

Longer definitions would take several lines. In that case, all lines after the semicolon must be *indented*. Jupyter interfaces create the indentation by themselves.

### References

1. W McKinney (2017), *Python for Data Analysis --- Data Wrangling with Pandas, NumPy, and IPython*, O'Reilly.

2. J VanderPlas (2017), Python Data Science Handbook, O'Reilly.

3. J Zelle (2010), *Python Programming --- An Introduction to Computer Science*, Franklin, Beedle & Associates.
