# [DS-01] What is data science?

The expression **data scientist** is common nowadays in job descriptions, referred to a mix of data analysis skills and a background of programming languages and databases. It is a broad job title, coming in many forms, with the specific demands depending on the industry, the business and the role. So, certain skillsets suit certain positions better than others. Data scientists do not do anything essentially new. We have long had statisticians, analysts, and programmers. What is new is the way different skills are combined in a single profession.

An ancestor of data science is **data mining**, born in the computer science field. This generic expression applies to a heterogeneous set of methods, used to extract information from large data sets. It is understood as *mining knowledge from data*. The typical applications in management are related to **Customer Relationship Management** (CRM): market basket analysis, churn modeling, credit scoring, etc. From a technical perspective, the content of a data mining course may not differ much from that of a data science course.

## Core competencies

At the business place, the data scientist takes care of the **data pipeline**. A data pipeline is a sequence of data processing elements, in which the output of one element is the input of the next one. Managing these elements involve core competencies such as:

* **Data capture**. This may require managing a data source, using database management skills, and understanding the **data domain**, to formulate relevant questions. It may also require data-modeling skills in order to discover patterns, such as correlation, in the data.

* **Data wrangling** is a generic expression which refers to the operations performed on the data to get them ready for the analysis. Regarded as the preliminary steps in a data pipeline, we call this **data preprocessing**. Typical preprocessing steps are: removing duplicates and redundant variables, renaming and/or combining levels of categorical variables, solving the issues associated to missing data, filtering out parts of the data, combining data sets by means of joins and unions, and aggregating the data based on one or more grouping variables. When the data are extracted from a database, some of these operations can be integrated in the data extraction step, by means of an appropriate query.

* **Analysis**. It typically starts at an exploratory level, using basic statistical tools, much like those that you may have seen in elementary stats courses. In many cases, this is followed by an attack with more advanced **machine learning** tools.

* **Presentation**. Most people do not understand numbers well. They cannot see the patterns that the data scientist sees. So, it is important to provide a graphical presentation of these patterns to visualize what the data reveal and how to exploit them. More important, the presentation must tell a specific story so the impact of the data is not lost.

* **Developing data products**, such as a recommendation system, a pricing algorithm or a fraud detection procedure. Machine learning techniques are typically used here.

This course is mainly concerned with the first three points, which are illustrated with some interesting examples.

## Data science in the computer

Users interact with data science software applications in three possible ways:

* Conventional menus and mouse-clicking, as in Excel or Tableau.

* Programming code (Python, R, etc).

* Visual programming, based on flow charts which are a graphical translation of code.

This course is based on code. More specifically, it uses Python, which is, currently, the leading choice of data scientists. About 15 years ago, data mining textbooks used visual programming and/or menus in their examples, but, nowadays, most data science books are based on Python, and the examples include code.

The majority of the data science tasks are performed on **structured data**, that is, on data sets in tabular form, with rows and columns. The rows correspond to the **samples**, which are typically individuals, companies or transactions, and the columns to **features**. The features are either **numeric** (*e.g.* price) or **categorical** (*e.g.* gender). Nevertheless, there are also methods for dealing with **string** (text) data and **datetimes**. 

In this course, tabular data sets are provided in **CSV files**. In Python, they are typically managed as objects called **data frames**. Roughly speaking, a data frame is a collection of data (column) vectors, all of the same length. All the entries in the same column have the same data type, but the columns of a data frame can have different data types.
