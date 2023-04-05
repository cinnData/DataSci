# [DS-06] String data in Pandas

## Strings

A **string** is a sequence of **characters**. This includes the (English) alphanumeric characters and also special characters like white space, punctuation, etc. Other symbols, like emoticons, can also appear in your data, specially in social networks data. Besides that, you can also find letters from other languages (Spanish, Portuguese, etc) or alphabets (Cyrillic, hiragana, etc), and even ideographs (such as Han characters).

There is a basic set of 127 characters, called the **ASCII characters**, which are encoded in the same way by all the computers, so you will never have trouble with them. They include the English letters (without accents), the numbers, basic punctuation (not curly quote marks or long dashes), white space, **control characters** such as the new line, represented in programming languages as `\n`, and other well known symbols, such as the dollar (`$`) and the hash (`#`) symbols. The complete list can be easily found in Internet.

Non-ASCII characters can be encoded by different computers or different text editors in different ways. Mind that, if you capture string data on your own, you will probably find some of these characters in your data. Even when the documents are expected to be in English, they can be contaminated by other languages: Han characters, German dieresis, Spanish eñe, etc.

The preferred **encoding** is **UTF-8** (`utf-8`), which is the default encoding in Macintosh computers. Reading and writing text files in Pandas, the argument `encoding` allows you to manage both UTF-8 and the alternative encoding **Latin-1** (`latin1`). Windows computers use their own system, which is region specific. In US and Western Europe, this is **Windows-1252**, which is very close to Latin-1, though not exactly the same.

## Strings as sequences

In Python, strings and lists are two types of **sequences**, and for many purposes, a string can be regarded as a list of characters. So, some basic methods are common to lists and strings. For instance, the function `len` gives you the number of characters of a string:

```
In [1]: iese = 'IESE Business School'
```

```
In [2]: len(iese)
Out[2]: 20
```

Also, a **substring** can be extracted from a string just as a sublist is extracted from a list:

```
In [3]: iese[5:]
Out[3]: 'Business School'
```

In Python, strings are pasted as lists, with the plus sign (`+`):

```
In [4]: iese[:4] + ', A way to learn'
Out[4]: 'IESE, A way to learn'
```

A difference between strings and lists is found in the use of `in`. For strings, it can be used to relate, not only a character to a string, but a substring to a string:

```
In [5]: 'IE' in iese
Out[5]: True
```

## Python string methods

Besides the methods shared with lists, Python has a collection of methods for manipulating strings. For instance, **conversion to lowercase**:

```
In [6]: iese.lower()
Out[6]: 'iese business school'
```

Conversion to uppercase is performed in a similar way. The typical *Find and Replace* method of text editors is implemented in Python by the method `replace`:

```
In [7]: iese.replace('IESE', 'Iese')
Out[7]: 'Iese Business School'
```

You can split a string with the method `split`. The split can be based on any **separator**. If no separator is specified, any white space string (containing only white space, line breaks or tabs) is a separator.

```
In [8]: iese.split()
Out[8]: ['IESE', 'Business', 'School']
```

```
In [9]: iese.split('i')
Out[9]: ['IESE Bus', 'ness School']
```

Finally, the method `count` counts **the number of occurrences** of a pattern within a string:

```
In [10]: iese.count('s')
Out[10]: 3
```

## Pandas string methods

Pandas provides vectorized versions of the above methods for series. They return a series of the same length, in which each term results from applying a string method to the corresponding term of the original series. The syntax is typically `s.str.meth(args)`, where `s` is a Pandas series, `str` is a flag for string methods in Pandas, `meth` is the name of the method and `args` is a set of *ad hoc* arguments. 

In the next example, I include an **empty string** and a **missing value** for diversity. The `None` entry, which stands for a missing value, could be replaced by `numpy.nan` here.

```
In [11]: import pandas as pd
```

```
In [12]: pres = pd.Series(['Donald Trump', 'Joe Biden', '', None])
    ...: pres
Out[12]: 
0    Donald Trump
1       Joe Biden
2                
3            None
dtype: object
```

The method `str.len` is a vectorized version of the method `len` of plain strings. So, it returns the length of every term of a string series. In this example, the **empty string** (`''`) has length zero. Since `None` has no length, a `NaN` value has been returned as the fourth term. Also, the series has then been converted by Python to data type `float`, to cope with that (it would be `int` if all the terms had length).

```
In [13]: pres.str.len()
Out[13]: 
0    12.0
1     9.0
2     0.0
3     NaN
dtype: float64
```

Other examples of the same approach:

```
In [14]: pres.str[0]
Out[14]: 
0       D
1       J
2     NaN
3    None
dtype: object
```

```
In [15]: pres.str.lower()
Out[15]: 
0    donald trump
1       joe biden
2                
3            None
dtype: object
```

```
In [16]: pres.str.replace(' ', '-')
Out[16]: 
0    Donald-Trump
1       Joe-Biden
2                
3            None
dtype: object
```

```
In [17]: pres.str.split()
Out[17]: 
0    [Donald, Trump]
1       [Joe, Biden]
2                 []
3               None
dtype: object
```

The method `str.contains` **detects the occurrence** of a pattern in the terms of a string series. It returns a Boolean series indicating, for every term, whether the pattern occurs in that term.

```
In [18]: pres.str.contains('a')
Out[18]: 
0     True
1    False
2    False
3     None
dtype: object
```

This can be used to filter out documents. For instance:

```
In [19]: pres = pres[~(pres.isna())]
    ...: pres[~pres.str.contains('a')]
Out[19]: 
1    Joe Biden
2             
dtype: object
```

* Note*. `~` is the logical operator `not` for Boolean series. It turns `True` into `False` and conversely.

The function `str.findall` **extracts matching patterns** from the terms of a string series. It returns, for every term, a list containing all the occurrences of that pattern. This allows for the pattern to occur with different frequency along the original series. The series returned has then data type `object`, which in Pandas means anything that is not Boolean or numeric.

```
In [20]: pres.str.findall('e')
Out[20]: 
0        []
1    [e, e]
2        []
dtype: object
```

## Regular expressions

Quite often, the transformations performed by the methods described above can be simplified by means of **regular expressions**. More specifically, they can be used as the first argument in the methods `str.contains`, `str.findall`, `str.replace`, `str.split` and `str.count`.

A regular expression is a pattern which describes a collection of strings. Among them, **character classes** are the simplest case. They are built by enclosing a collection of characters in square brackets. The square brackets indicate *any of the characters enclosed*. For instance, `[0-9]` stands for any digit, and `[A-Z]` for any capital letter. Two simple examples follow.

```
In [21]: bio = pd.Series(['I was born in 1954', 'My phone is +34 932 534 200'])
    ...: bio.str.replace('[a-z]', 'x', regex=True)
Out[21]: 
0             I xxx xxxx xx 1954
1    Mx xxxxx xx +34 932 534 200
dtype: object
```

```
In [22]: bio.str.replace('[0-9]', 'x', regex=True)
Out[22]: 
0             I was born in xxxx
1    My phone is +xx xxx xxx xxx
dtype: object
```

The default value of `regex` is currently `True`, but will change to `False` in a future version. To avoid confusion, it is better to specify it. While `str.replace` `str.split` and `str.contains` admit the regex argument, `str.findall`  and `str.count` don't, and they always read the pattern as a regular expression.
 
Character classes get more powerful when complemented with **quantifiers**. For instance, followed by a plus sign (`+`), a character class indicates a sequence of any length. So, `[0-9]+` indicates any sequence of digits, therefore any number, and `[a-z]+` indicates any word in lower case (using only English letters). We can also specify the length of the sequence, as in `[A-Z]{2}`, or the minimum and maximum length, as in `[0-9]{1,3}`.

Let us see next the quantifier effect in one of the preceding examples:

```
In [23]: bio.str.replace('[a-z]+', 'x', regex=True)
Out[23]: 
0              I x x x 1954
1    Mx x x +34 932 534 200
dtype: object
```

The regular expressions `\w` and `\W`, which stand for any character that can be part of a word and the contrary, respectively, are useful in practice. The following example uses `\W`, with a quantifier, to split by either white space or punctuation (or both). 

```
In [24]: bio.str.split('\W+')
Out[24]: 
0              [I, was, born, in, 1954]
1    [My, phone, is, 34, 932, 534, 200]
dtype: object
```

With **wildcards**, you can match pieces of text whose exact content you do not know, other than the fact that they share a common pattern or structure (*e.g*. phone numbers or zip codes). The wildcard of Python regular expressions is the **dot** (`.`), which matches any single character. 

```
In [25]: people = pd.Series(['John - male', 'Nancy - female', 'Bruno - male'])
    ...: people.str.replace(' - .+', '', regex=True)
Out[25]: 
0     John
1    Nancy
2    Bruno
dtype: object
```

Some symbols, like the quantifier `+` or the wildcard `.` have a special role in regular expressions. You have to be careful when using them in patterns for the methods `str.findall` and `str.count`, because they can give unexpected results. The following example illustrates this. 

```
In [26]: comment = pd.Series(['Sally and Tim came to dinner. A nice couple.'])
    ...: comment.str.count('.')
Out[26]: 
0    44
dtype: int64
```

But, if you write these characters with a **escape character** (`\`), they are read literally:

```
In [27]: comment.str.count('\.')
Out[27]: 
0    2
dtype: int64
```

## Homework

1. Write a function which anonymizes credit card numbers, turning, for instance, '2875765488882745' into 'Credit card ****745'. Check that your function does the job with a short series containing credit card numbers.

2. A VISA Electron card number has 16 digits. As in any credit card, the first digits identify the card issuer. In the case of VISA Electron, the **issuer identification number** (IIN) can be 4026, 417500, 4508, 4844, 4913 or 4917. Write a function which identifies VISA Electron card numbers. Check that your function does the job with a short series containing credit card numbers.

3. You can see below a list containing the URL's for some **job postings** at the London-based financial technology company Wise. The sequence of digits in the middle of the URL make the ID of the position. Write a function which extracts a list of such URL's to a list containing their ID's.

```
['https://www.wise.jobs/role/3093508-design-director-onboarding-growth',
'https://www.wise.jobs/role/3234541-senior-implementation-manager',
'https://www.wise.jobs/role/3276007-senior-product-designer',
'https://www.wise.jobs/role/3350217-product-analyst-northam']
```
