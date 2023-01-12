# [DS-06] String data in Pandas

## Strings

A **string** is a sequence of **characters**. This includes the (English) alphanumeric characters and also special characters like white space, punctuation, etc. Other symbols, like emoticons, can also appear in your data, specially in social networks data. Besides that, you can also find letters from other languages (Spanish, Portuguese, etc) or alphabets (Cyrillic, hiragana, etc), and even ideographs (such as Han characters).

There is a basic set of 127 characters, called the **ASCII characters**, which are encoded in the same way by all the computers, so you will never have trouble with them. They include the English letters (without accents), the numbers, basic punctuation (not curly quote marks or long dashes), white space, **control characters** such as the new line, represented in programming languages as `\n`, and other symbols familiar to you, such as the dollar (`$`) and the hash (`#`) symbols. The complete list can be easily found in Internet.

Non-ASCII characters can be encoded by different computers or different text editors in different ways. Mind that, if you capture string data on your own, you will probably find some of these characters in your data. Even when the documents are expected to be in English, they can be contaminated by other languages: Han characters, German dieresis, Spanish eñe, etc.

The preferred **encoding** is **UTF-8** (`utf-8`), which is the default encoding in Macintosh computers. Reading and writing text files in Pandas, the argument `encoding` allows you to manage both UTF-8 and the alternative encoding **Latin-1** (`latin1`). Windows computers use their own system, which is region specific. In US and Western Europe, this is **Windows-1252**, which is very close to Latin-1, though not exactly the same.

## Strings as sequences

In Python, strings and lists are two types of **sequences**, and some basic methods are common to both types. Examples: (a) the function `len` gives you the number of characters of a string, (b) the plus sign (`+`) allows you to concatenate strings, and (c) you can extract a **substring** from a string in the same way you extract a sublist from a list using a range of indexes.

A difference between strings and lists is found in the use of the membership operator `in`. If `lst` is a list, `x in lst` means that `x` is an item of `lst`, but, if `str` is a string, `x in str` means that `x` is a substring of `str`.

## Pandas string methods

Pandas **string methods** are vectorized versions of those old methods. The syntax takes, in most cases, the form `s.str.fname(args)`. For a Pandas series `s`, this returns another Pandas series, resulting from applying the function `fname` term-by-term. So, `str.len`, `str.lower`, `str.replace`, `str.split` and `str.count` are vectorized versions of the corresponding string methods. Also, substrings can be extracted term-by-term by with the method `str[range]`, and Pandas series are pasted term by term with the plus sign (`+`). For instance, `s1 + ' ' + s2` returns a series in which every term results from concatenating the corresponding terms from `s1` and `s2`.

Two new methods are:

* `str.contains` **detects the presence of a pattern** in the terms of a series. It returns a Boolean series evaluating, term by term, the occurrence of the pattern.

* `str.findall` **extracts matching patterns** from the terms of a series. It returns a series in which every term is a list containing all the occurrences of the pattern in the corresponding term of the given series. 

## Regular expressions

A **regular expression** is a pattern which describes multiple strings. Regular expressions can be used in many computer languages, including Python. For instance, the regular expression `[a-z]` stands for any lower case (ASCII) letter. 

`[a-z]` is an example of a **character class**. Character classes are built by enclosing a collection of characters within square brackets. The square brackets indicate *any* of the characters enclosed. Also useful are `\w`, which matches word characters (meaning letters, digits and underscore) and `\W`, which matches non-word characters.

Character classes get more powerful when complemented with **quantifiers**. For instance, followed by a plus sign (`+`), a character class indicates a sequence of any length. So, `[a-z]+` indicates any uninterrupted sequence of lower case ASCII letters. 

A **wildcard** is a symbol which can match any single character (letter, digit, whitespace, etc). The wildcard of Python regular expressions is the dot (`.`).

The Pandas methods `str.contains`, `str.findall`, `str.replace` and `str.split` accept a regular expression as a matching pattern, with the argument `regex=True`, but read the pattern as a fixed string with `regex=False`. For instance, 

```
s.str.replace('. ', repl, regex=False)` 
```

replaces every instance of the string made by a dot plus a white space by the string `repl`, but 

```
s.str.replace('. ', repl, regex=True)` 
```

replaces any single character (letter, digit, whitespace, etc), followed by a white space by `repl`.
