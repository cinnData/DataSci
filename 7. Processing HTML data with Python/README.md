# 7. Processing HTML data with Python

### What is HTML?

**HTML** (Hypertext Markup Language) is the language in which are written the documents designed to be displayed in a web browser. The web browser receives HTML documents from a web server or from local storage and renders the documents as multimedia web pages.

HTML is typically assisted by two technologies:

* **CSS** (Cascading Style Sheets) is a language used to describe the style of HTML documents.

* **JavaScript** is a scripting language, that is, one for integrating and communicating with other languages. Scripting languages are typically used for "small jobs".

JavaScript code is left aside when processing HTML documents in Python, for instance in web scraping jobs, but **CSS selectors** can be used to identify the pieces of information that we wish to capture from a web page. This course does not cover that system, presenting instead a method based on **XPath expressions**.

An extremely simple example of a HTML document follows. It is easy to see, in this example, why HTML is called a **markup language**. The markup, which consists here of the tags `<head>`, `<body>`, `<title>`, `<div>` and `<a>`, is used for creating a structure in the document and for including **links** to web pages, pictures, etc.

	<html>

	<head>
	
		<title>Data Viz</title>

	</head>

	<body>

		<div class="course">Data Visualization</div>

		<div class="program">MBA full-time</div>`

		<a class="prof", href="https://www.iese.edu/faculty-research/faculty/miguel-angel-canela">Miguel Ángel Canela</a>

	</body>

	</html>

*Note*. In a HTML document captured from Internet, you will not find such a friendly presentation, with one line for each tag, and indentation to help you see the structure of the document. But there are many tools for rendering the XML and HTML documents in this form.

### Tags and attributes

The structure of a HTML document is made by the tags. Every part of the document is opened by a **start tag** (`<tag>`) and closed by an **end tag** (`</tag>`). The tags create a tree-like structure in the document. 

The tag `<html>` tells the browser that this is a HTML document. The `html` node is the **root node**, with two **child nodes**, `head` and `body`. A HTML document is always split in this way. In the example, the `head` node has one child, while the `body` node has three children, which are **siblings**.

In the example, the `title` node contains the string `'Data Viz'`, enclosed between the start tag and the end tag (this can also be said of the `head` node). This string is the **node value**. Also, some nodes have **attributes**. The attributes are contained in the start tag. In our example, the `div` nodes have one `class` attribute, while the `a` node has two attributes, a `class` attribute and a `href` attribute. `class` attributes, which specify one or more `class` names for an HTML element, are very frequent, and can be used in any HTML element. The value of a `class` attribute can be used by CSS and JavaScript to perform certain tasks for elements with that `class` value.

The `a` node has a special role. It marks a **hyperlink**, which is used to link a page to another page, or to download a file. The most important attribute of the this node is the `href` attribute, which indicates the link's destination.

### The package lxml

The package lxml provides many useful tools for parsing XML (and HTML) documents, both local and accessible via HTTP or FTP. It also offers access to a XPath interpreter. 

Suppose that the HTML code displayed above has been imported in Python as a string variable. The function `html.fromstring` can parse that string, learning the tree structure encoded in the HTML document, which is stored in an `lxml` object of type `lxml.html.HtmlElement`. Let us call `tree` that object. Then, `tree[0]` is the `head` node and `tree[1]` is the `body` node. Branching further, `tree[1][0]` and `tree[1][1]` are the two nodes and `tree[1][2]` is the `a` node.

To extract the information from these objects in a format which can be managed by common Python tools, we have two functions: 

* `text` extracts the node value, that is, the text between the node tags. For the first `div` node, the syntax would be `tree[1][0].text`.

* `attrib` extracts the value of an attribute. For the first `div` node, the syntax would be `tree[1][0].attrib['class']` (note the square brackets).

### XML and XPath

HTML is a special case of another language called **XML** (eXtensible Markup Language), which has a wider scope. The markup in XML is also defined by the tags, but these are not predefined as in HTML (`head`, `body`, etc). 

**XPath** is a query language for selecting nodes from a XML document. XPath expressions look like the path expressions in UNIX (Mac/Linux) file systems. For instance, `/html/head` denotes the `head` node, while `/html/body` denotes the `body` node. These two are easy, because there is only one `head` node and one `body` node. But there are typically many `div` nodes. In the example, `/html/body/div` denotes the two `div` nodes. These nodes can be identified as `/html/body/div[1]` and `/html/body/div[2]`.

*Note*. XPath starts counting at 1, not at 0 like Python.

Since HTML documents can be large, it is practical to shorten XPath expressions by omitting intermediate nodes. So, the `div` nodes of the example can be simply identified as `//div`. Although this is very practical, it would not be specific enough in a HTML document containing many `div` nodes in different places. The following three formulas provide unambiguous identification in most cases:

* Specify a substring of a node value, as in `//div[contains(text(), 'MBA')]]`, which identifies the second `div` node of the example.

* Specify an attribute value, as in `//div[@class='course']`, which identifies the first `div` node of the example.

* Specify a substring of an attribute value, as in `//div[contains(@class, 'cour')]`. This is practical with long attribute values.

