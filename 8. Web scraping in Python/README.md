# 8. Web scraping in Python

### What is web scraping?

**Web scraping** is concerned with extracting data from websites, in particular data that would be difficult to get on a large scale using traditional data collection methods. There is a whole industry built around web scraping, as it is used to track product price changes or discounts, to gather data from social profiles, to capture real estate listings, in search engine optimization (SEO), etc.

Scraping a web page involves downloading the page and extracting data from it. Both things can be done with many languages, in particular with Python. There are also specialized web scraping software applications, such as **Octoparse**. This course covers only those pages that are rendered to the browser in a single step (explained below). Although we use in this course the package `lxml`, you can use other Python packages, such as Beautiful Soup (`bs4`) and Scrapy (`scrapy`).

### HTML and the browser

Suppose that your browser (let me assume that you use either Chrome or Firefox) is displaying a web page on the screen. You can get the source code of the page through the contextual menu that opens when right-clicking anywhere on the page. A new tab will open, displaying a HTML document. In most pages, this HTML document corresponds to the page that the browser displayed for you. These pages are the ones covered here. But not all pages are that simple. Some use a technology called **AJAX** (Asynchronous JavaScript And XML), which, in a few words, works as follows:

1. The page corresponding to the URL that you have entered is loaded.

2. A JavaScript program creates a XMLHttpRequest object.

3. The XMLHttpRequest object sends a request to a web server.

4. The server sends a new HTML document back to the browser, which is displayed on the screen. This second document corresponds to the page that you see.

The problem is that neither the Python methods discussed in this course capture this second document, which is, probably, from where you wish to scrape, but the first one. To get the second one, web scrapers use a tool called **Selenium**, which in Python can be accessed through the package `selenium`.

### The package Requests

With Python, files can be downloaded from Internet sources in multiple ways. Many tutorials suggest using the package `urllib`, which is part of the Python Standard Library (ie plain Python). More popular, nowadays, is the package Requests (`requests`), briefly introduced here. Requests comes with the Anaconda distribution, so you do not have to install it.

Let us refresh the context. You have probably noticed the string `'https'` (sometimes `'http'`) at the beginning of a URL. The **Hypertext Transfer Protocol** (HTTP) was designed to enable communications between clients and servers. For instance, a client (such as your browser) sends a **HTTP request** to the server. Then the server returns the response to the client. The response contains status information about the request and, if the request is accepted, the requested content.

**GET** is one of the most common HTTP methods. It is used to request data from a specified resource. The function `requests.get` is a Python implementation of the GET request. You can manage this as follows.

`import requests`

`page = requests.get(urlname).text`

`requests.get` returns a `requests` object (type `requests.models.Response`). The attribute `text` of this object is a string which, for an ordinary web page, is the HTML source code. Now you can parse this string with the function `lxml.html.fromstring`, which has already appeared in this course, and then extract the information you are interested in by means of appropriate XPath expressions.

### What is JSON?

The **JSON** (JavaScript Object Notation) format is very practical for storing certain types of information, such as Twitter or news data, for which the tabular format is not adequate. It is used in some NoSQL databases like **MongoDB**. 

A JSON document is a collection of **pairs key/value**, organized in a special way, which accounts for a hierarchy of information. For instance, the following example stores family information:

	[{"Name": "John", "Age": 27},

	 {"Name": "Peter", "Age": 32, "Children": "Louis"},

	 {"Name": "Maria", "Age": 29, "Children": ["Edward", "Christine"]}]

In this example, you can see how to include information about the children in a flexible way, allowing for zero, one or more children. To use a standard tabular format for these data, you should create a collection of columns "Child1", "Child2", etc, with many missing values. The flexible structure of JSON allows you to cope with different family sizes in a simple way. 

To the Pythonista, the JSON document looks like a nested structure of lists and dictionaries. So, importing and exporting JSON data in Python is straightforward. The package `json`, which is part of the Python Standard Library, allows this functionality.

Some webpages include a JSON document in a `script` node. In general, `script` nodes are used in HTML documents to embed executable code or data. Although most of those nodes embed or refer to JavaScript code, they can also be used to store metada in JSON format. In this case, they have the attribute `type= "application/ld+json"`. Sometimes, these JSON documents contain information which can also be found in other parts of the web page, but they may contain information that is not displayed by the browser. They are used to mark up web contents so that they can be understood by major search engines as Google and Bing. The data stored in `script` nodes is not displayed by the browser.
