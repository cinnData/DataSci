# [DS-02E] Example - Amazon jobs

## Introduction

Job offers are posted at the **Amazon Jobs** website (`amazon.jobs/en-gb`). Given the interest of these data for the community, a **web scraping** project at IESE Business School was started in 2021, with the focus on that website. At that time (no longer, unfortunately), more than 50,000 job offers were posted there. It was discovered that the information shown at the Amazon Jobs pages was loaded from JSON documents which could be accessed directly at `amazon.jobs/en-gb/search.json`. So the project was reoriented and the data extracted directly from the JSON documents, which were captured by playing with the URL parameters at that site.

This example is based on a data subset resulting from selecting the job category **Software Development** and the business category **Amazon Web Services** (AWS).

## The data set

The file `amzn.csv` (zipped) contains data for 8,116 software developement positions at AWS, captured in November 2021. The variables are:

* `id`, a unique identifier for the position. Example: '996246'.

* `title`, the title of the job, more or less descriptive. Example: 'Senior Software Dev Engineer'.

* `company_name`, the name of the company, within the orbit of AWS. There 65 unique company names in this data set. Example: 'Amazon.com Services LLC'.

* `description`, a description of the job, containing specific detail, but also a dose of bombastic rhetoric. Example: 'Are you passionate about enterprise-wide scale compliance management? Are you excited about impactful technical projects ...'.

* `basic_qualifications`, a list of generic qualifications for the job. Example: '4+ years of professional software development experience. 3+ years of programming experience ...'.

* `preferred_qualifications`, a list of more specific qualifications. Example: '6+ years experience building high scale distributed systems that handle big amounts of data. Strong knowledge of data structures, algorithms, and designing for performance, scalability, availability, and internet and OS security fundamentals ...'.

* `job_type`, either 'full-time' or 'part-time' (a few cases).

* `location`, the location of the position. Example: 'US, WA, Seattle'.

* `posted_date`, the date the position was posted at Amazon Jobs website, as 'yyyy-mm-dd'.

* `updated_time`, time since the data were updated at the website. Example: '3 months'.

* `team`, a generic indication of the team in which the position is offered, in a a specific terminology of Amazon. There are 23 such teams in this data set. Example: 'team-sde-primary'.

### Questions

Q1. Leaving aside the job ID, which is unique for every job posting, how many **duplicates** do you find in this data set? Drop the duplicates, so all the positions are different, in at least one field. 

Q2. Which are the **top-ten locations** for software developement at AWS? 

Q3. Suppose that a potential candidate is interested in finding a **position in India**. Does Amazon have something for him/her? In which locations? 

Q4. **Programming languages** are often mentioned in the basic qualifications field, and C is a classic. Which flavor of C is preferred here, C++ or C#?

# Importing the data

As in the previous example, we use the Pandas funcion `read_csv()` to import the data. First, we import the package:

```
In [1]: import pandas as pd
```

The (zipped) source file is stored in a GitHub repository, so we can use a remote path to get access. We take the first column of the source file (`id`) as the index, so the resulting data frame will have 10 columns.

``` 
In [2]: path = 'https://raw.githubusercontent.com/cinnData/DataSci/main/Data/'
   ...: filename = path + 'amzn.csv.zip'
   ...: df = pd.read_csv(filename, index_col=0)
```

## Exploring the data

To explore the data set, we use the standard Pandas methods. First, the method `.info()` prints a report of the data frame content. There are no missing values.

```
In [3]: df.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 8116 entries, 996246 to 1004288
Data columns (total 10 columns):
 #   Column                    Non-Null Count  Dtype 
---  ------                    --------------  ----- 
 0   title                     8116 non-null   object
 1   company_name              8116 non-null   object
 2   description               8116 non-null   object
 3   basic_qualifications      8116 non-null   object
 4   preferred_qualifications  8116 non-null   object
 5   job_type                  8116 non-null   object
 6   location                  8116 non-null   object
 7   posted_date               8116 non-null   object
 8   updated_time              8116 non-null   object
 9   team                      8116 non-null   object
dtypes: object(10)
memory usage: 697.5+ KB
```

Second, `.head()` extracts the first rows. The data look as expected, so far.

```
In [4]: df.head()
Out[4]: 
                                          title             company_name  \
id                                                                         
996246             Senior Software Dev Engineer  Amazon.com Services LLC   
995357  Senior Embedded SW Development Engineer       Annapurna Labs LTD   
994952     Senior Software Development Engineer  Amazon.com Services LLC   
990063             Senior Software Dev Engineer  Amazon.com Services LLC   
981888                     Chip Design Engineer       Annapurna Labs LTD   

                                              description  \
id                                                          
996246  Are you passionate about enterprise-wide scale...   
995357  AnnapurnaLabs as part of AWS, is looking for t...   
994952  Amazon Web Services (AWS) Virtual Private Netw...   
990063  Are you passionate about open source and engag...   
981888  Looking for exceptional engineers to join the ...   

                                     basic_qualifications  \
id                                                          
996246   4+ years of professional software development...   
995357   Bachelors Degree in Computer Science or Elect...   
994952   4+ years of professional software development...   
990063   4+ years of professional software development...   
981888   5 + years of experience in chip design. B.Sc....   

                                 preferred_qualifications   job_type  \
id                                                                     
996246   6+ years experience building high scale distr...  full-time   
995357   Deep understanding of computer architecture. ...  full-time   
994952  • Knowledge of Computer Science fundamentals i...  full-time   
990063   3+ years experience building high scale distr...  full-time   
981888  Experience / Knowledge in Keywords. an advanta...  full-time   

                 location posted_date updated_time              team  
id                                                                    
996246    US, WA, Seattle  2019-11-19     3 months  team-sde-primary  
995357          IL, Haifa  2019-11-19     6 months  team-sde-primary  
994952    US, VA, Herndon  2019-11-18     4 months  team-sde-primary  
990063  US, VA, Arlington  2019-11-12      14 days  team-sde-primary  
981888       IL, Tel Aviv  2019-11-05      13 days  team-sde-primary  
```

## Q1. Count and drop duplicates

Applied to a data frame, the method `.duplicated()` returns a Boolean series, indicating the rows (not including the index) which are duplicated. The default reads the data top-down, returning `False` for the rows occurring for the first time, and `True` for those having occurred before. Applying `.sum()` to that series, we get the number of duplicated rows.

``` 
In [5]: df.duplicated().sum()
Out[5]: 366
``` 

The same can be applied to the index:

```
In [6]: df.index.duplicated().sum()
Out[6]: 0
```

So, we have 366 job postings which are repetitions, but with a different ID. They may be errors, or positions which are identical. As suggested in question Q1, we drop them. The method `.drop_duplicates()` works in a straightforward way, dropping the rows for which `df.duplicated() == True`. So, the default of this methods keeps only the first occurrence of a every unique row.

```
In [7]: df = df.drop_duplicates()
   ...: df.shape
Out[7]: (7750, 10)
```

## Q2. Top locations for software developers at Amazon

The method `.value_counts()` counts the occurrences of every unique value of a series, sorting the counts top down. the length of the series returned by `.value_counts()` is the number of unique values. 

```
In [8]: df['location'].value_counts().shape
Out[8]: (174,)
```

So, there are 174 distinct locations for software developers at Amazon. The top ten can be extracted with `.head(10)`.

```
In [9]: df['location'].value_counts().head(10)
Out[9]: 
US, WA, Seattle           3009
US, VA, Arlington          562
CA, BC, Vancouver          530
US, MA, Boston             297
US, NY, New York           291
US, VA, Herndon            269
US, CA, East Palo Alto     258
US, WA, Bellevue           200
US, TX, Austin             169
DE, BE, Berlin             152
Name: location, dtype: int64
```

## Q3. Positions in India

Since, in the location, the country comes first, as a two-letter code, the Indian locations must be those starting with 'IN'. We can capture them easily by slicing the location, as follows.

```
In [10]: df['location'][df['location'].str[:2] == 'IN'].value_counts()
Out[10]: 
IN, KA, Bangalore      129
IN, TS, Hyderabad       41
IN, TN, Chennai          6
IN, MH, Maharashtra      1
IN                       1
IN, HR, Gurgaon          1
IN, Hyderabad            1
Name: location, dtype: int64
```

Note. we have already found two examples showing that some locations do not have the expected three parts, country, state and town. See the homework for an exercise on this.

An alternative (and more involved) approach would be to use `.str.contains()`, specifying the substring 'IN' to be at the beginning. Under `regex=True`, we can do this by inserting a **caret** symbol (`^`):

```
In [11]: df['location'][df['location'].str.contains('^IN', regex=True)].value_counts()
Out[11]: 
IN, KA, Bangalore      129
IN, TS, Hyderabad       41
IN, TN, Chennai          6
IN, MH, Maharashtra      1
IN                       1
IN, HR, Gurgaon          1
IN, Hyderabad            1
Name: location, dtype: int64
```

## Q4. Programming languages in the basic qualifications field

Search for the postings including 'C#' in the basic qualifications is easy with `.str.contains()`. Since computer languages are sometimes written in lowercase, we include here the argument `case=False`, with the search string in lowercase.

```
In [12]: df['basic_qualifications'].str.contains('c#', case=False).mean().round(3)
Out[12]: 0.64
```

Searching for C++, we have to be careful, because the default of  `.str.contains()` is `regex=True`, and the plus symbol (`+`) has a special role in regular expressions. A solution is to specify `regex=False`, as we see next.

```
In [13]: df['basic_qualifications'].str.contains('c+', case=False, regex=False).mean().round(3)
Out[13]: 0.72
```

So, C++ is mentioned more often than C#. The same result could be obtained with the default version of `.str.contains()` but the search string `'c\+'`. The backslash symbol (`\`) makes Python to read the plus sign literally.


```
In [14]: df['basic_qualifications'].str.contains('c\+', case=False).mean().round(3)
Out[14]: 0.72
```

Note that, as a regular expression, `'c+'` covers any string that contains the letter 'c' at least once, so you get lost if you don't pay attention to this technicality:

```
In [15]: df['basic_qualifications'].str.contains('c+', case=False).mean().round(3)
Out[15]: 1.0
```

## Homework

1. As we have seen in question Q3, some positions are incomplete. How often does this happen?

2. What happens if in `In [15]` we use `'c++'` instead of `'c+'`? Why?

3. In question Q4, we have just counted the postings mentioning C# and C++ in the basic qualifications field, irrespective of the number of times they were mentioned? Can you refine the analysis counting the postings that mention these languages one, two, three, etc times?

4. Is Java more demanded than C++ in the basic qualifications field? Take care of distinguishing Java from JavaScript, which is a different beast. 

5. How often is experience mentioned in the preferred qualifications field? 

6. Expressions like '3+ years' or similar, with or without the word experience. For instance, you can find '4+ years of professional sotware development ...'. When the basic qualifications specifiy a number of years of experience, which is the top frequent number?
