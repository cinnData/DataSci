# 6. String data in Pandas

### Pandas string functions

Python was born with a collection of methods for manipulating variables of type `str`. This included not only sequences of **alphanumeric characters**, but also **white space** and **punctuation**. Those basic methods were expanded in the package `re`, taking advantage of regular expressions (see below). Pandas **string functions** are essentially vectorized versions of those old methods. The syntax is typically `s.str.fname(args)`. For a Pandas series `s`, this returns another Pandas series resulting from applying a function term-by-term.

### Some useful functions

* The Pandas function `str.len` returns the **length** of every element of a string series. This is just a vectorized version of the Python function `len`.

* **Substrings** can be extracted term-by-term from a string series just as we extract elements from a list. The syntax is either `s.str[start, end]`, `s.str[:end]` or `s.str[start:]`.  

* Strings are **joined** in Python just as lists, with the plus sign (`+`). The same works for string series. For instance, `s1 + ' ' s2` returns a series in which every term results from pasting the corresponding terms from `s1` and `s2`, with a white space as the glue.

* `str.lower`  **converts to lowercase**. The syntax is `s.str.lower()`.

* `str.contains` **detects the presence or absence of a pattern** in the terms of a string series. The syntax is `s.str.contains(pat)`. This returns a Boolean series indicating, term by term, whether `pat` occurs in `s`. 

* `str.findall` **extracts matching patterns** from the terms of a string series. The syntax is `s.str.findall(pat)`. This returns a series in which every term is a list containing all the occurrences of `pat` in the corresponding term of `s`. Using lists allows for the pattern to occur with different frequency along `s`.

* `str.replace` **replaces matched patterns** in the terms of a string series. The syntax is `s.str.replace(pat, repl)`.

* `str.split` **splits up** into pieces the terms of a string series. The syntax is `s.str.split(pat)`. The default pattern is `pat=''`. This returns a series in which every term is a list containing the words contained in the the corresponding term of `s` (such list is called a bag of words).

### Regular expressions

The patterns used by the functions `str.contains`, `str.findall`, `str.replace` and `str.split` can be plain strings or **regular expressions**. Regular expressions can be used in many computer environments, but they are not exactly the same everywhere. Nevertheless, the basic ones are universal. Among them, **character classes** are the simplest case. They are built by enclosing a collection of characters within square brackets. The square brackets indicate *any* of the characters enclosed. For instance, `[0-9]` stands for any digit, and `[A-Z]` for any capital letter.

Character classes get more powerful when complemented with **quantifiers**. For instance, followed by a plus sign (`+`), a character class indicates a sequence of any length. So, `[0-9]+` indicates any sequence of digits, therefore any number. We can also specify the minimum and maximum length of the sequence, as in `[0-9]{m,n}`.

It is always useful in string data analysis to have a **wildcard** that can match any single character (letter, digit, whitespace, etc). The wilcard of regular expressions in Python is the dot (`.`). 

### Special characters

Text imported from PDF or HTML documents, or from devices like mobile phones, may contain **special characters** like the left/right quotation marks (‘, “, etc), or the three-dot character (…), which is better to control, to avoid confusion. To keep it short, I do not develop this point here, but mind that, if you capture string data on your own, you will probably find some of that in your data. Even when the documents are expected to be in English, they can be contaminated by other languages: Han characters, German umlaut, Spanish eñe, etc.

Another source of trouble is that these special symbols can be encoded by different computers or different text editors in different ways. The preferred **encoding** is **UTF-8** (`utf-8`), which is the default encoding in Macintosh computers. Reading and writing files text files in Pandas, the argument encoding allows you to manage both UTF-8 and the alternative encoding **Latin-1** (`latin1`). Windows computers use their own system, which is region specific. In US and Western Europe, this is **Windows-1252**, which is very close to Latin-1, but not exactly the same. 

