# [DS-03] HTML data in Python

## What is HTML?

**HTML** (Hypertext Markup Language) is the language in which are written the documents designed to be displayed in a web browser. The web browser receives a HTML document from a web server or from local storage and renders it as a multimedia web page. That HTML document is then called the **page source**.

HTML is assisted by two technologies:

* **CSS** (Cascading Style Sheets) is a language used to describe the style of HTML documents.

* **JavaScript** is a scripting language, that is, one for integrating and communicating with other languages. Scripting languages are used for small jobs. The source of a dynamic web page typically contains JavaScript scripts to perform actions such as accepting cookies or asking for more information. 

An extremely simple example of a HTML document follows. It is easy to see, in this example, why HTML is called a **markup language**. The markup, consisting here of the **tags** `<head>`, `<body>`, `<title>`, `<div>` and `<a>`, is used for creating a structure in the document and for including **links** to web pages, pictures, etc.

```
<html>
<head>
	<title>Data Viz</title>
</head>
<body>
	<div class="course">Data Visualization</div>
	<div class="program">MBA full-time</div>
	<a class="professor" href="faculty-research/faculty/miguel-angel-canela">Miguel Ángel Canela</a>
</body>
</html>
```

Unfortunately, in a HTML document captured from Internet, you will not find such a friendly presentation, with one line for each tag, and indentation to help you see the structure of the document. But there are many tools for rendering HTML documents in this form.

## Tags and attributes

The structure of a HTML document is made by the tags. Every part of the document is opened by a **start tag** (`<tag>`) and closed by an **end tag** (`</tag>`). These parts are called **HTML elements**. The tags create a tree-like structure in the document, with HTML elements nested within HTML elements. The representation of the HTML document as a logical tree is called the **Document Object Model** (DOM). 

*Note*. Though we may insert white space between consecutive elements to make the document readable, as in the example below, white space between tags belonging to different elements is ignored by the HTML interpreter.

The tag `<html>` tells the browser that this is a HTML document. The `html` element is the whole document. It has two **child elements**, `head` and `body`. A HTML document is always split in this way. In the example, the `head` element has one **child**, while the `body` element has three children, which are **siblings**.

Then, the `title` element contains the string `'Data Viz'`, enclosed between the start tag and the end tag (this can also be said of the `head` element). This string is referred to as **text**. Also, most of the start tags have **attributes**. In our example, the `div` elements have one `class` attribute, while the `a` element has two attributes, a `class` attribute and a `href` attribute. `class` attributes, which specify one or more `class` names for some elements of the HTML document, are very frequent. The value of a `class` attribute can be used by CSS and JavaScript to perform certain tasks for the elements with that `class` value.

The `a` tags have a special role, marking hyperlinks. A **hyperlink** is used to link a page to another page, or to download a file. The most important attribute of an `a` element is the `href` attribute, which indicates the link's destination. 

Tags with other names, such as `span`, `img`, `button` and `script`, with specific roles in a HTML document, are usually found in the source files of real web pages.

## What is Beautiful Soup?

**Beautiful Soup** is a Python package for extracting data from HTML files. Other packages, like **scrapy**, provide more powerful toolkits, but, since Beautiful Soup is much friendlier, most **web scraping** practitioners start there and do not leave Beautiful Soup unless their projects get really complex.

You can install Beautiful Soup by entering in the shell (or the console) `pip install bs4`. When the package is already installed, the recommended import style is:

```
In [1]: from bs4 import BeautifulSoup
```

This allows us to use the function `BeautifulSoup`, which can be applied to any string containing HTML code. `BeautifulSoup` **parses** the HTML code, learning the tree structure encoded there, which is then stored in a **soup object**. Let us see how this works in our example. 

We create a string variable, whose value is the HTML document. Note that the end of the line is marked with the backslash (`\`).

```
In [2]: html_str = '<html>\
   ...: <head>\
   ...:   <title>Data Viz</title>\
   ...: </head>\
   ...: <body>\
   ...:   <div class="course">Data Visualization</div>\
   ...:   <div class="program">MBA full-time</div>\
   ...:   <a class="professor" href="faculty-research/faculty/miguel-angel-canela">Miguel Ángel Canela</a>\
   ...: </body>\
   ...: </html>'
```
This is stored as:

```
In [2]: html_str
Out[2]: '<html><head>  <title>Data Viz</title></head><body>  <div class="course">Data Visualization</div>  <div class="program">MBA full-time</div>  <a class="professor" href="faculty-research/faculty/miguel-angel-canela">Miguel Ángel Canela</a></body></html>'
```

## Parsing HTML code

To parse the string `html_str`, learning the tree structure, we enter:

```
In [4]: soup = BeautifulSoup(html_str, 'html.parser')
```

`BeautifulSoup` returns a soup object, which stores the contents of `html_str` in a way that the different HTML elements, called here **tags**, can be extracted. To get this, it uses a **parser**, which is a program which breaks the string into substrings based on the tags. 

Beautiful Soup does not come with a parser. It uses the one that it prefers among those available in your computer. If `'html.parser'` is specified, the choice is the parser provided by the Python Standard Library, so you do not need any additional package. Since this is a rather technical issue, Iwe follow here the recommended practice. 

The object `soup` has a special type:

```
In [5]: type(soup)
Out[5]: bs4.BeautifulSoup
```

The contents of `soup` can be displayed (don't do this for the source of a real web page, which will be too big to be read on the screen):

```
In [6]: soup
Out[6]: <html> <head> <title>Data Viz</title> </head> <body> <div class="course">Data Visualization</div> <div class="program">MBA full-time</div> <a class="professor" href="https://www.iese.edu/faculty-research/faculty/miguel-angel-canela">Miguel Ángel Canela</a> </body> </html>
```

The same is true por the elements contained in `soup`, as we will see below. But we have to see first how to extract this elements from the soup.

## The tree structure

Once you have a soup, you can easily explore the the content. For instance:

```
In [7]: soup.head
Out[7]: <head> <title>Data Viz</title> </head>
```

```
In [8]: type(soup.head)
Out[8]: bs4.element.Tag
```

Though, formally, `BeautifulSoup` and `Tag` are different types, a tag works in practice as a smaller soup, so you can extract elements within elements:

```
In [9]: soup.head.title
Out[9]: <title>Data Viz</title>
```

If you ask for a nonexisting element, you get `None`:

```
In [10]: soup.head.div
```

When there are several elements satisfying the requirements, you get the first one. This is the logic of Beautiful Soup:

```
In [11]: soup.div
Out[11]: <div class="course">Data Visualization</div>
```

HTML elements are called **tags** in Beautiful Soup. The simplest way to extract tags from the soup is based on the methods `.find()` and `.find_all()`. The method `.find_all()` returns a list containing all the tags that satisfy a specification (eventually empty), while `.find()` returns only the first one (or `None`, if there is no tag satisfying it). Let us see how to use in this method in our example.

## The method find

A first example of `.find()` follows.
 
```
In [12]: soup.find('div')
Out[12]: <div class="course">Data Visualization</div>
```

Note that there are two `div` tags in this soup, and `.find()` has extracted the first one. But we can use the attribute values to distinguish among tags with the same name:

```
In [13]: soup.find('div', attrs={'class': 'course'})
Out[13]: <div class="course">Data Visualization</div>
```

For the attribute `class`, this is can be shortened, as in: 

```
In [14]: soup.find('div', 'program')
Out[14]: <div class="program">MBA full-time</div>
```

Since a tag works as a smaller soup, you can iterate the method `.find()`:

```
In [15]: soup.find('head').find('title')
Out[15]: <title>Data Viz</title>
```

## The method .find_all()

The method `.find_all()` uses the same syntax as `.find()` but, instead of a single tag, it returns a list with all the tags that satisfy the specification:

```
In [16]: soup.find_all('div')
Out[16]: 
[<div class="course">Data Visualization</div>,
 <div class="program">MBA full-time</div>]
```

Note that `.ind_all()` *always* returns a list. The list can be empty (`.find()` would return `None` in that case) 

```
In [17]: soup.find('head').find_all('div')
Out[17]: []
```

When there is only one tag in the list, that tag is precisely the one returned by `.find()`:

```
In [18]: soup.find_all('div', 'course')
Out[18]: [<div class="course">Data Visualization</div>]
```

Note that, even when there is exactly one tag in the list returned by `.find_all()`, you have to extract it from the list:

```
In [19]: soup.find_all('div', 'course')[0]
Out[19]: <div class="course">Data Visualization</div>
```

## Extracting information from the tags

The information we wish to extract from a HTML element can come as the text enclosed by the start tag and the end tag, or as the value of an attribute. With `.string`, we can extract the text enclosed by the tags:

```
In [20]: soup.find('a').string
Out[20]: 'Miguel Ángel Canela'
```

Note that this method cannot be applied directly to a list returned by `find_all`: 

```
In [21]: soup.find_all('div').string
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[9], line 1
----> 1 soup.find_all('div').string

File /opt/homebrew/lib/python3.11/site-packages/bs4/element.py:2428, in ResultSet.__getattr__(self, key)
   2426 def __getattr__(self, key):
   2427     """Raise a helpful exception to explain a common code fix."""
-> 2428     raise AttributeError(
   2429         "ResultSet object has no attribute '%s'. You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?" % key
   2430     )

AttributeError: ResultSet object has no attribute 'string'. You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?
```

But we can use a comprehension list to extract the text from every item of the list and store it in a new list:

```
In [22]: [t.string for t in soup.find_all('div')]
Out[22]: ['Data Visualization', 'MBA full-time']
```

In certain cases, we are interested in the value of an attribute. A frequent example is that of an `a` tag whose
attribute `href` contains a relevant link. The link is then extracted as:

```
In [23]: soup.find('a')['href']
Out[23]: 'faculty-research/faculty/miguel-angel-canela'
```

## Finding the elements containing a string

In `find_all`, the parameter `string` allows searching elements by the text enclosed:

```
In [24]: soup.find_all('div', string='Data Visualization')
Out[24]: [<div class="course">Data Visualization</div>]
```


```
<div class="col-12 col-md-4 col-lg-3 employee-card-box">
<a href="https://www.iese.edu/faculty-research/faculty/miguel-angel-canela/" class="employee-card-link">
<figure class="row employee-card employee-card--subdirector">
<div class="col-12 col-employee-card">
<figcaption class="employee-card__description">
<p class="employee-card__description__name">Miguel Ángel Canela</p>
<div class="employee-jobs">
<p class="employee-card__description__job">Associate Professor of Managerial Decision Sciences</p>
</div>
</figcaption>
</div>
</figure>
</a>
</div>
```

