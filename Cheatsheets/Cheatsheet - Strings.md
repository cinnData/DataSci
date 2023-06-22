# Cheatsheet - Strings

## Slicing

* `str[n]`: returns the character of the string `str` whose index is `n`. Since Python starts counting at zero, this would be the character placed in the `n-1`-th place.

* `str[-n]`: returns the character of the string `str` whose index is equal to the length of `str` minus `n`. So, `str[-1]` returns the last character, `str[-2]` the penultime character, etc.

* `str[n:m]`: returns the characters of the string `str` whose indexes go from `n` to `m-1`. If `n` is missing, it is assumed to be `0`. If `m` is missing, it is assumed to be the length of `str`.

* `str[n:m:s]`: picks the characters of the string `str` from index `n` to index `m-1`, making steps of `s`. So, `str[2:10:3]` returns the characters with indexes `2`, `5` and `8`. If `s` is negative, steps are made backwards. So `str[::-1]` returns `str` reversed.

## String methods

* `str.capitalize()`: returns a copy of `str` with its first character capitalized and the rest lowercased.

* `str.count(substr)`: returns the number of times the substring `substr` occurs in a string `str`, without overlapping.

* `str.endswith(suffix)`: returns a Boolean indicating whether the last characters of `str` coincide with the string `suffix`.

* `str.find(substr)`: returns the index of the first character of the first occurrence of a substring in a string. If the substring does not occur, it returns `-1`.

* `str.join(strlist)`: returns the string resulting from pasting the elements of the list of strings `strlist` with the glue `str`. So, `' '.join(['Joe', 'Biden'])` returns `'Joe Biden'`.

* `str.lower()`: returns a copy of `str` with all the cased characters converted to lowercase.

* `str.replace(old, new)`: returns a copy of `str` with all occurrences of `old` replaced by `new`.

* `str.split(sep)`: returns the list of substrings of `str` resulting from a split based on the separator specified. The default is `sep=''`.

* `str.startswith(prefix)`: returns a Boolean indicating whether the first characters of `str` coincide with the string `prefix`.

* `str.strip(chars)`: returns a copy of `str` with the leading and trailing characters removed. The `chars` argument is a string specifying the set of characters to be removed. The default is `chars=' '`.

* `str.upper()`: returns a copy of `str` with all the cased characters converted to uppercase.

* `substr in str`: returns a Boolean indicating whether the substring `substr` is contained in the string `str`.

## Methods from the package re

* `re.findall(pat, str)`: returns all non-overlapping matches of the pattern `pat` in the string `str`, as a list of strings. The pattern is read as a regular expression. `str` is scanned left-to-right, and the matches are returned in the order found. Empty matches (strings of zero length) are included in the result.

* `re.split(pat, str)`: splits the string `str` by the occurrences of the pattern `pat`, which are returned as a list. The pattern is read as a regular expression.

* `re.sub(pat, repl, str)`: returns the string obtained by replacing the non-overlapping occurrences of the pattern `pat` in the string `str` by the replacement string `repl`. The pattern is read as a regular expression. If it is not found, `str` is returned unchanged.

## Methods from the package Pandas

* `s.str.contains(pat)`: returns a Boolean series indicating, term by term, the occurrence of the pattern `pat` in the terms of the series `s`. With the default argument `regex=True`, the pattern is read as regular expression.

* `s.str.counts(pat)`: returns a numeric series with the number of occurrences of the pattern `pat` in the terms of `s`, without overlapping. With the default argument `regex=True`, the pattern is read as regular expression. A vectorized form of `str.count(substr)`.

* `s.str.endswith(pat)`: returns a Boolean series indicating, term by term, the occurrence of the pattern `pat` at the end. Regular expressions are not accepted as patterns.

* `s.str.findall(pat)`: extracts all patterns matching the patterns `pat`, as a series whose terms are lists. With the default argument `regex=True`, the pattern is read as regular expression. A vectorized form of `re.findall(pat, str)`.

* `s.str.isalnum()`: returns a Boolean series indicating, term by term, whether all the characters in every term of the series `s` are alphanumeric (letters and digits).

* `s.str.isalpha()`: returns a Boolean series indicating, term by term, whether all the characters in every term of the series `s` are alphabetic (letters).

* `s.str.len()`: returns a numeric series containing the number of characters of every term of the series `s`. A vectorized form of `len`.

* `s.str.lower()`: converts the terms of `s` to lowercase.

* `s.str.lstrip()`: removes white space from the left side of every term of `s`.

* `s.str.replace(pat, repl)`: replaces all the occurrences of the pattern `pat` by the replacement string `repl` in every term of `s`. With the default argument `regex=True`, the pattern is read as regular expression. A vectorized form of `re.sub(pat, repl, str)`.

* `s.str.rstrip()`: removes white space from the right side of every term of `s`.

* `s.str.split(pat)`: splits into pieces every term of `s` by the occurrences of the pattern `pat`. With the default argument `regex=True`, the pattern is read as regular expression. A vectorized form of `re.split(pat, str)`.

* `s.str.startswith(pat)`: returns a Boolean series indicating, term by term, the occurrence of the pattern `pat` at the beginning. Regular expressions are not accepted as patterns.
