# [DS-04E] Example - Netflix data

## Introduction

Like some other companies, Netflix posts its job offers at a platform called Lever. **Netflix job postings** can be found at `jobs.lever.co/netflix`. Let us call this page the main page. It will display, the day you visit it, a few hundred postings. These postings can be filtered by location, team and work type. Most of the postings on display are for teams in the *Streaming* division.

The main page contains, for each available position, basic information about the job, such as the job title, the location and the team, and a link to a page specific for that position, such as `jobs.lever.co/netflix/2d11d912-bfb3-4d9d-bfa1-0ce036214284`. This individual page presents a description of the company and the role of the new employee.

## The target data

The objective of this example is to collect data on the positions offered at `jobs.lever.co/netflix` and to export them to a tabular file in which every row corresponds to a job. The tools used are taken from the Python packages **Requests** and **Beautiful Soup**.

We aim at capturing the following fields:

* `title`, the job title. Example: 'Post Production Supervisor (Animation)'.

* `worktype`, a workplace type label, such as *ON-SITE* or *REMOTE*.

* `location`, the job location. Example: 'Los Angeles, California'.

* `link`, the link to a page specific for that position, which contains a description of the company and the role of the new employee. Example: `jobs.lever.co/netflix/620dd1ad-0345-42dc-a3b1-d94e1a08056b`.

## Capturing the source code

Requests comes with the Anaconda distribution, so you can probably import it directly.

```
In [1]: import requests
```

We apply he Requests function `get()` to the URL of the target web page. When the request is accepted, as in this case, this function returns an object of a special type (type `requests.models.Response`). The attribute `text` of this object is a string which, for an ordinary web page, is the HTML source code.

```
In [2]: html_str = requests.get('https://jobs.lever.co/netflix').text
```

Now, `html_str` is a string containing the source code of the Netflix Lever main page.

## Parsing the source code

To **parse** HTML code, learning the tree structure it conveys, we use the function `BeautifulSoup()` from the package `bs4` (Beautiful Soup, version 4). We import this function with:

```
In [3]: from bs4 import BeautifulSoup
```

`BeautifulSoup()` converts the string `html_str` to a "soup" object:

```
In [4]: soup = BeautifulSoup(html_str)
```

Next, we use the method `.find_all()` to extract from the soup the data on the title, as a list. Every term of the list will be one job title. We will repeat the exercise with the job location and the team for every job. To get extra information that could be found there, we will also extract a list with the links to the individual job pages.

## Job titles

In a web scraping job, we take advantage of the fact that web pages posting information units in a systematic way have a repetitive structure, in which every unit is contained in a set of HTML elelements with the same names and attributes values. So, by means of `.find_all()`, we can capture one of features for all the units in one shot, as a list. Let us see how to do this with the job title.

The key assumption is that all the job titles are stored in HTML elements with the same name and attribute values, and that this is exclusive of job titles. This is, precisely, what allows Lever to update the pages in a programmatic way with the information supplied by Netflix.

To use `.find_all()`, we need to know the name of the tag and, probably, some of the attributes. How can we find this? There are many ways, and every web scraper has his/her own cookbook. The simplest approach is based on browser tools. First, we count the number of times that 'APPLY' appears on the page. This is 377 (you will probably get a different number when you visit the page). So, we know the number of job titles that we have to capture.

Next, we use the *Inspect tool* of the browser. We right-click on the first job title, opening a contextual menu, and we select *Inspect*. This opens a window showing a view of the source code in which the element containing that job title is highlighted. That element is (when this is being written):

```
 <h5 data-qa="posting-name">Production Pipeline Technical Director</h5>
 ```

 So, we try:

 ```
 In [5]: job = soup.find_all('h5', {'data-qa': 'posting-name'})
```

If this is right, we must have a list with 253 items. Indeed:

```
In [6]: len(job)
Out[6]: 377
```

To be sure, we can explore the head and the tail of this list:

```
In [7]: job[:5]
Out[7]: 
[<h5 data-qa="posting-name">Senior Product Manager</h5>,
 <h5 data-qa="posting-name">Senior Technical Producer - Games Studio</h5>,
 <h5 data-qa="posting-name">Director, Business Development, Game Licensing</h5>,
 <h5 data-qa="posting-name">Director, Product Management &amp; Live Service - Internal Games</h5>,
 <h5 data-qa="posting-name">Gameplay/Feature Engineer, Games Studio</h5>]
```

```
In [8]: job[-5:]
Out[8]: 
[<h5 data-qa="posting-name">Android Software Engineer (L4) - Discovery &amp; Viewing Experiences</h5>,
 <h5 data-qa="posting-name">Technical Program Manager (L6) - Algorithms Engineering</h5>,
 <h5 data-qa="posting-name">Administrative Assistant, Enterprise Operations</h5>,
 <h5 data-qa="posting-name">Manager, Security Operations (West Coast)</h5>,
 <h5 data-qa="posting-name">Manager, Space &amp; Occupancy Planning - LA</h5>]
```

The tags `h1`, `h2`, `h3`, `h4`, `h5` and `h6` are used for **headings**. They don't have a `class` attribute because their style is unique, specified in a `style` element within the `head` element. You may not need the attribute value to capture these elements. For instance, in this case, `soup.find_all('h5')` would have given you the same result.

To create a list containing the text from these elements, we use a **list comprehension**:

```
In [9]: job = [j.string for j in job]
```

Now:

```
In [10]: job[:5]
Out[10]: 
['Senior Product Manager',
 'Senior Technical Producer - Games Studio',
 'Director, Business Development, Game Licensing',
 'Director, Product Management & Live Service - Internal Games',
 'Gameplay/Feature Engineer, Games Studio']
```

## Workplace types

The workplace type is found, following the same approach as for the job title, as the text within a `span` tag with `class="display-inline-block small-category-label workplaceTypes"`.

```
In [11]: worktype = soup.find_all('span', 'display-inline-block small-category-label workplaceTypes')
    ...: worktype = [w.string for w in worktype]
    ...: worktype[:5]
Out[11]: 
['Remote\xa0—\xa0',
 'Remote\xa0—\xa0',
 'On-site\xa0—\xa0',
 'Remote\xa0—\xa0',
 'Remote\xa0—\xa0']
 ```

What is the substring `\xa0—\xa0`? It corresponds to the dash, with white space on both sides, that separates the workplace type from another label that indicates the commitment (see the homework). The white space is not plain white space, but a special character called **Unicode non-breaking space**, which in HTML is denoted by `&nbsp;`. We can easily eliminate this with:

```
In [12]: worktype = [w.replace('\xa0—\xa0', '') for w in worktype]
    ...: worktype[:5]
Out[12]: ['Remote', 'Remote', 'On-site', 'Remote', 'Remote']
```

## Job locations

Now, the job location, which is found as the text within a `span` tag with `class="sort-by-location posting-category small-category-label location"`.

```
In [13]: location = soup.find_all('span', 'sort-by-location posting-category small-category-label location')
    ...: location = [l.string for l in location]
    ...: location[:5]
Out[13]: 
['Remote, United States',
 'Remote, United States',
 'Los Angeles, California',
 'Los Angeles, California',
 'Remote, United States']
 ```

## Links

Since we know that every link has to appear as the value of a `href` attribute at an `a` element, we can search directly for these elements. There are two for every job, since you can call the job page from two places. The second one occurs in an `a` element with `class="posting-title"`. So, the links can be captured as:

```
In [14]: link = soup.find_all('a', 'posting-title')
    ...: link = [l['href'] for l in link]
    ...: link[:5]
Out[14]: 
['https://jobs.lever.co/netflix/637f1ab3-a84b-4b6c-b6d7-d079a7888562',
 'https://jobs.lever.co/netflix/4354a21c-3d18-4cd9-bac6-436cdbd5ee9d',
 'https://jobs.lever.co/netflix/28e5b8e3-b7f3-4578-8862-6ba49ad65166',
 'https://jobs.lever.co/netflix/5e057849-5de6-4b41-92f0-62ed3908a41a',
 'https://jobs.lever.co/netflix/d1813381-ecde-48fa-8626-45c4a9ff2c6a']
```

## Packing

Now, we have the five lists `job`, `location`, `division`, `dept` and `link`. We can pack them as the columns of a Pandas data frame:

```
In [15]: import pandas as pd
```

```
In [16]: df = pd.DataFrame({'job': job, 'worktype': worktype, 'location': location, 'link': link})
    ...: df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 377 entries, 0 to 376
Data columns (total 4 columns):
 #   Column    Non-Null Count  Dtype 
---  ------    --------------  ----- 
 0   job       377 non-null    object
 1   worktype  377 non-null    object
 2   location  377 non-null    object
 3   link      377 non-null    object
dtypes: object(4)
memory usage: 11.9+ KB
```

```
In [17]: df.head()
Out[17]: 
                                                 job worktype   
0                             Senior Product Manager   Remote  \
1           Senior Technical Producer - Games Studio   Remote   
2     Director, Business Development, Game Licensing  On-site   
3  Director, Product Management & Live Service - ...   Remote   
4            Gameplay/Feature Engineer, Games Studio   Remote   

                  location                                               link  
0    Remote, United States  https://jobs.lever.co/netflix/637f1ab3-a84b-4b...  
1    Remote, United States  https://jobs.lever.co/netflix/4354a21c-3d18-4c...  
2  Los Angeles, California  https://jobs.lever.co/netflix/28e5b8e3-b7f3-45...  
3  Los Angeles, California  https://jobs.lever.co/netflix/5e057849-5de6-4b...  
4    Remote, United States  https://jobs.lever.co/netflix/d1813381-ecde-48...  
```

## Exporting the data to a CSV file

Finally, we can export the data to a CSV file by means of the method `.to_csv()`. You can edit the path of the file if you don't it to be placed in the working directory.

```
In [18]: df.to_csv('netflix.csv', index=False)
```

The argument `index=False` has been used to skip the default of `.to_csv()`, which adds the index as the first column.

## Homework

1. An additional label, such as *FULL-TIME* or *PIPELINE*, indicates the **commitment**. Add this field to the the data set. Note that this label is sometimes missing, so `.find_all()` will return a shorter list, that will not match the other lists. You have to use a process that allows for placing a `NaN` value where the commitment is missing.

2. Coupa Software is a technology platform for Business Spend Management, headquartered in San Mateo, California, with offices throughout Europe, Latin America, and Asia Pacific. Coupa also posts job positions in Lever (`https://jobs.lever.co/coupa`). Capture data on these job posts as we have done for Netflix and save them to a CSV file. Do you find positions in India whose job titles are related to data?
