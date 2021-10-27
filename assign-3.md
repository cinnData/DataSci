# Assignment 3

### Introduction

IESE Business School displays information of the Faculty members in 11 web pages. The URL of the first one is https://www.iese.edu/search/professors. The objective of this assignment is to scrape professors' data from this page and save them so they can be seen with Excel. 

### Tasks

1. Capture the source HTML code of this page using an appropriate function from the package `requests`.

2. Parse the HTML code using an appropriate function from the package `lxml`.

3. Extract a list with the professors's names (eg "Inés Alegre").

4. The same with the professors' descriptions (eg "Assistant Professor of Managerial Decision Sciences").

5. The same with the links to the professors' individual pages (eg "https://www.iese.edu/faculty-research/faculty/ines-alegre/").

6. Pack these lists as a data frame with the Pandas function `DataFrame`.

7. Export the data frame to a CSV file with the method `.to_csv`.

8. Export the data frame to an Excel file with the method `.to_excel`.

### Submission

1. Submit a document with your code and short comments.

2. Put your name on top of the document.

### Deadline

October 26 (Tuesday), 24:00.
