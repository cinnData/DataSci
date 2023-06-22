# Cheatsheet - Regular expressions

## Character classes

* `[. . .]` : matches any single character or range of characters found between the brackets.

* `[^. . .]`: matches any single character or range of characters not found between the brackets.

* `\d`: matches digits (equivalent to `[0-9]`).

* `\D`: matches non digits (equivalent to `[^0-9]`).

* `\s`: matches white space (equivalent to `[ \t\n\r\f]`).

* `\S`: matches non white space (equivalent to `[^ \t\n\r\f]`).

* `\w`: matches word characters (meaning letters, digits and underscore).

* `\W`: matches non-word characters.

##  Quantifiers

* `expr?`: greedily matches 0 or 1 occurrence of the expression `expr` (but no more).

* `expr*`: greedily matches 0 or more occurrences of the expression `expr`.

* `expr+`: greedily matches 1 or more occurrences of the expression `expr`.

* `expr{n, m}`: matches at least `n` and at most `m` occurrences of the expression.

* `expr{n}`: matches exactly `n` occurrences of the expression `expr`.

* `expr{n,}`: matches `n` or more occurrences of the expression `expr`.

## Variations

* `^expr`: matches the expression `expr` at the beginning of the line.

* `expr$`: matches the expression `expr` at the end of the line.

* `expr1|expr2`: matches either `expr1` or `expr2`.
