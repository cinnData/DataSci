# Example - Book recommendations

## Introduction

**Bookcrossing** is defined as *the practice of leaving a book in a public place to be picked up and read by others, who then do likewise*. The term is derived from BookCrossing (`bookcrossing.com`), a free online book club which was founded to encourage the practice, aiming to *make the whole world a library*.

The crossing or exchanging of books may take various forms, including wild-releasing books in public, direct swaps with other members of the websites, or *book rings* in which books travel in a specified order to participants who want to read a certain book. The community aspect of BookCrossing has grown and expanded in the form of blog or forum discussions, mailing lists and annual conventions throughout the world.

BookCrossing was launched on April 21, 2001. By November 2019, there were over 1.9 million members and over 13 million books traveling through 132 countries, of which over 25 thousand books newly "released in the wild" in the previous month across over 60 countries. Over 80% of the books were released in the eight most active countries (Germany, United States, Spain, Italy, Australia, United Kingdom, the Netherlands and Brasil). The world's first official International BookCrossing Day took place on April 21st, 2014.

Cai-Nicolas Zeigler collected over one million ratings of books from the BookCrossing website. Since the books are identified by the ISBN, what we call here a book is, really, an edition of a book. Popular books, such as *Harry Potter and the Sorcerer's Stone*, have several editions in this database. Individual users come mixed with book rings, so some of the users have a very high number of book pickings. Since these rings may also rate the books (with a single rating), they have not been removed. 

## The data set

The data for this example come in three tables. The file `book_users.csv` contains information about 278,858 users. The columns are:

* `user`, the user's ID (anonymized).

* `location`, the user's location, as 'city, state, country'. Example: 'moscow, yukon territory, russia'.

* `age`, the user's age, in years. Almost 40% of the data are missing.

The file `book_items.csv` contains information about 271,360 books on circulation. The columns are: 

* `isbn`, the ISBN code of the book, which works as the book ID. Invalid ISBN's have already been removed.

* `title`, the title of the book.

* `author`, the book's author, obtained from Amazon Web Services. In case of several authors, only the first one is provided. One value is missing.

* `year`, the year of publication, obtained from Amazon Web Services. 1.7% of the values are missing.

* `publisher`, the book's publisher, obtained from Amazon Web Services. Two values are missing.

* `image`, an URL linking to the cover image. These URL's point to the Amazon web site. Two values are missing.

The file `book_ratings.csv` contains 1,031,136 ratings. The columns are:

* `user`, the user's ID.

* `isbn`, the books's ISBN.

* `rating`, either the rating given by the user (1-10 range) or 0, when the user did not provide a rating.

Source: C-N Ziegler, SM McNee, JA Konstan & G Lausen (2005), Improving Recommendation Lists Through Topic Diversification, in *Proceedings of the 14th International World Wide Web Conference*, Chiba, Japan.

## Questions

Q1. How often do bookcrossers rate the books they pick?

Q2. Which titles have been picked more times?

Q3. Which books have been rated highest? Restrict the search to the titles that have been rated by at least 25 users.

Q4. How many editions of the SF classic *The Martian Chronicles* in English are offered by BookCrossing?

Q5. From the data provided, extract a list of 5 books to be recommended to users having picked *The Martian Chronicles*. A simple approach would be to search for the titles that have been picked more often by the users who have also picked *The Martian Chronicles*.
