# [DS-02E] Example - Amazon jobs

## Introduction

Job offers are posted at the **Amazon Jobs** website (`amazon.jobs/en-gb`). Given the interest of these data for the community, a **web scraping** project at IESE Business School was started, with the focus on this website. At that time (no longer, unfortunately), more than 50,000 job offers were posted there. It was discovered that the information shown at the Amazon Jobs pages was loaded from JSON documents which could be accessed directly at `amazon.jobs/en-gb/search.json`. So the project was reoriented and the data were extracted directly from the JSON documents, captured by playing with the URL parameters at that site.

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

Q1. Leaving aside the job ID, which is unique for every job posting, how many duplicates do you find in this data set? Drop the duplicates, so all the positions are different, in at least one field. 

Q2. Which are the top-ten locations for software developement at AWS? Suppose that a potential candidate is interested in finding a position in India. Does Amazon have something for him/her? In which locations? 

Q3. Programming languages are often mentioned in the basic qualifications field, and C is a classic. Which flavor of C is preferred here, C++ or C#?

Q4. How often is experience mentioned in the preferred qualifications field?

# Importing the data

We use here the Pandas funcion `read_csv()` to import the data. First, we import the package:

```
In [1]: import pandas as pd
```

The source file is in a GitHub repository, so we use a remote path to get access. The source file comes zipped, but `.read_csv()` can manage this without any specification if the file extension is `.zip`. With the argument `index_col=0`, the first column of the CSV file, whose header is `id` is taken as the index, so te resulting data frame will have 10 columns.

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

Second, `.head()` displays the first five rows. The datqa look as expected, so far.

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

``` 
In [5]: df.duplicated().sum()
Out[5]: 366
``` 

```
In [6]: df.index.duplicated().sum()
Out[6]: 0
```

```
In [7]: df = df.drop_duplicates()
   ...: df.shape
Out[7]: (7750, 10)
```

## Q2. Top locations for software developers at Amazon

The top locations for software developers at Amazon can be spotted with the method `.value_counts()`. First we see that that there 174 distinct locations in the data set. 

```
In [8]: df['location'].value_counts().shape
Out[8]: (174,)
```

Now, with `.head(10)`, we select the top ten.

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

## Q3. Programming languages in the basic qualifications field

```
In [12]: df['basic_qualifications'].str.contains('c#', case=False).mean().round(3)
Out[12]: 0.64
```

```
In [13]: df['basic_qualifications'].str.contains('c+', case=False, regex=False).mean().round(3)
Out[13]: 0.72
```

```
In [14]: df['basic_qualifications'].str.contains('c+', case=False).mean().round(3)
Out[14]: 1.0
```

```
In [15]: df['basic_qualifications'].str.contains('c\+', case=False).mean().round(3)
Out[15]: 0.72
```

An alternative approach.

```
In [16]: bags = df['basic_qualifications'].str.lower().str.findall('\w+\+*')
    ...: bags.head()
Out[16]: 
id
996246     [4+, years, of, professional, software, develo...
995357     [bachelors, degree, in, computer, science, or,...
994952     [4+, years, of, professional, software, develo...
990063     [4+, years, of, professional, software, develo...
981888     [5, years, of, experience, in, chip, design, b...
```

## Q4. Experience mentioned in the preferred qualifications field

```
In [17]: df['preferred_qualifications'].str.contains('experience', case=False).mean().round(3)
Out[17]: 0.903
```

Expressions like '3+ years' or similar, with or without the word experience.

```
In [18]: df['preferred_qualifications'].str.count('\+?[0-9]\+? years').value_counts()
Out[18]: 
0    6160
1    1209
2     251
3      94
4      24
5      10
8       1
7       1
Name: preferred_qualifications, dtype: int64
```

```
In [20]: df['preferred_qualifications'][1542577]
Out[20]: " +10 years' experience developing fully automated end to end test infrastructure. +10 years' experience of scripting languages like Python and Shell. +10 years' experience working with Intel/AMD architecture. +10 years' experience with IPMI. +10 years' experience with I2C and SPI bus devices. +10 years' experience closing code and functional test coverage. +10 years' experience with SW/HW interface. embedded SW, drivers, HW security. Meets/exceeds Amazons leadership principles requirements for this role. Meets/exceeds Amazons functional/technical depth and complexity for this role."
```

```
In [21]: df['preferred_qualifications'][1588664]
Out[21]: ' 5+ years of experience in writing code using C++ or RUST. 3+ years of experience in writing code using C# or Java. Proficient in writing secured code. Test driven development.Basic.4+ years of professional software development experience.3+ years of programming experience with at least one modern language such as Java, C++, or C# including object-oriented design.2+ years of experience contributing to the architecture and design (architecture, design patterns, reliability and scaling) of new and current systems.Bachelor of Science (BS) degree in Computer Science or related field.5+ years of experience building large scale distributed applications.Preferrred. 5+ years of experience in writing code using C++ or RUST. 3+ years of experience in writing code using C# or Java. Proficient in writing secured code. Test driven development.Amazon is committed to a diverse and inclusive workplace. Amazon is an equal opportunity employer and does not discriminate on the basis of race, national origin, gender, gender identity, sexual orientation, protected veteran status, disability, age, or other legally protected status. For individuals with disabilities who would like to request an accommodation, please visit https://www.amazon.jobs/en/disability/us.'
```

## Homework

1. Positions incomplete.

2. What happens if in question Q3 we use 'c++' instead of 'c+'?

3. Is Java more demanded than C++ in the basic qualifications field? Take care of distinguish Java from JavaScript, which is a different beast. 

4. When the basic qualifications specifiy a number of years, which is the most frequent number?
