# [DS-04E] Example - Netflix data

## Introduction

Like some other companies, Netflix posts its job offers at a platform called Lever. **Netflix job postings** can be found at `jobs.lever.co/netflix`. Let us call this page the main page. It will display, the day you visit it, a few hundred postings. These postings can be filtered by location, team and work type. Most of the postings on display are for teams in the *Streaming* division.

The main page contains, for each available position, basic information about the job, such as the job title, the location and the team, and a link to a page specific for that position, such as `jobs.lever.co/netflix/2d11d912-bfb3-4d9d-bfa1-0ce036214284`. This individual page presents a description of the company and the role of the new employee.

## The target data

The objective of this example is to collect data on the positions offered at `jobs.lever.co/netflix` and to export them to a tabular file in which every row corresponds to a job. The tools used are taken from the Python packages **Requests** and **Beautiful Soup**.

We aim at capturing the following fields:

* `title`, the job title. Example: 'Post Production Supervisor (Animation)'.

* `location`, the job location. Example: 'Los Angeles, California'.

* `division`, the first part of the job team. The two parts are separated by an n-dash. Example: 'Animation'.

* `dept`, the second part of the job team. Example: 'Editorial + Post'.

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

To use `.find_all()`, we need to know the name of the tag and, probably, some of the attributes. How can we find this? There are many ways, and every web scraper has his/her own cookbook. The simplest approach is based on browser tools. First, we count the number of times that 'APPLY' appears on the page. This is 253 (you will probably get a different number when you visit the page). So, we know the number of job titles that we have to capture.

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
Out[6]: 253
```

To be sure, we can explore the head and the tail of this list:

```
In [7]: job[:5]
Out[7]: 
[<h5 data-qa="posting-name">Production Pipeline Technical Director</h5>,
 <h5 data-qa="posting-name">Administrative Assistant, Technology - Feature Animation at Netflix</h5>,
 <h5 data-qa="posting-name">Software Engineer (L4), Applications Engineering - Feature Animation at Netflix</h5>,
 <h5 data-qa="posting-name">Software Engineer (L4), Pipeline Engineering - Feature Animation at Netflix</h5>,
 <h5 data-qa="posting-name">Animator - Games Studio</h5>]
```

```
In [8]: job[-5:]
Out[8]: 
[<h5 data-qa="posting-name">Manager, International Tax Compliance &amp; Reporting</h5>,
 <h5 data-qa="posting-name">Manager, Tax Operations</h5>,
 <h5 data-qa="posting-name">Software Engineer (L4) - Developer Tools &amp; Infrastructure</h5>,
 <h5 data-qa="posting-name">Software Engineer (L4) - UI Rendering &amp; Performance</h5>,
 <h5 data-qa="posting-name">Design &amp; Construction Regional Program Manager, APAC</h5>]
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
['Production Pipeline Technical Director',
 'Administrative Assistant, Technology - Feature Animation at Netflix',
 'Software Engineer (L4), Applications Engineering - Feature Animation at Netflix',
 'Software Engineer (L4), Pipeline Engineering - Feature Animation at Netflix',
 'Animator - Games Studio']
```

## Job locations

Now, the job location, which is found, following the same approach as for the job title, as the text within a `span` tag with `class="sort-by-location posting-category small-category-label location"`.

```
In [11]: location = soup.find_all('span', 'sort-by-location posting-category small-category-label location')
    ...: location = [l.string for l in location]
    ...: location[:5]
Out[11]: 
['Los Angeles, California',
 'Burbank, California',
 'Burbank, California',
 'Burbank, California',
 ```

## Teams

The team is found in a `span` tag with `class="sort-by-team posting-category small-category-label department"`:

```
In [12]: team = soup.find_all('span', 'sort-by-team posting-category small-category-label department')
    ...: team = [t.string for t in team]
    ...: team[:5]
Out[12]: 
['Animation – Animation',
 'Animation – Technology',
 'Animation – Technology',
 'Animation – Technology',
 'Gaming – Boss Fight Entertainment']
```

The team comes in two parts: (a) a division, such as *Animation* or *Gaming*, and (b) a department, such as *Animation* or *Technology*. It might be interesting to split it in these two parts, which are separated by a symbol which looks like a hyphen but it is a bit longer. It is the **en dash** (see `jkorpela.fi/dashes.html` if you are curious about this). You can copypaste it in a Jupyter interface, or use the Unicode representation `\u2013`.

```
In [13]: team = [t.split(' – ') for t in team]
    ...: team[:5]
Out[13]: 
[['Animation', 'Animation'],
 ['Animation', 'Technology'],
 ['Animation', 'Technology'],
 ['Animation', 'Technology'],
 ['Gaming', 'Boss Fight Entertainment']]
```

Once the split has been performed, we name the two parts:

```
In [14]: division = [t[0] for t in team]
    ...: division[:5]
Out[14]: ['Animation', 'Animation', 'Animation', 'Animation', 'Gaming']
```

```
In [15]: dept = [t[1] for t in team]
    ...: dept[:5]
Out[15]: 
['Animation',
 'Technology',
 'Technology',
 'Technology',
 'Boss Fight Entertainment']
```

## Links

Since we know that every link has to appear as the value of a `href` attribute at an `a` element, we can search directly for these elements. There are two for every job, since you can call the job page from two places. The second one occurs in an `a` element with `class="posting-title"`. So, the links can be captured as:

```
In [16]: link = soup.find_all('a', 'posting-title')
    ...: link = [l['href'] for l in link]
    ...: link[:5]
Out[16]: 
['https://jobs.lever.co/netflix/f0615765-1451-42ae-bf76-7d3dfc1de481',
 'https://jobs.lever.co/netflix/f83c8247-b863-4830-947d-6b5d07220ccc',
 'https://jobs.lever.co/netflix/e8ac657b-05d0-49fb-af9d-1064d4888d71',
 'https://jobs.lever.co/netflix/44912894-f070-4989-9f9f-92ffb2ed210a',
 'https://jobs.lever.co/netflix/64e3cbb4-b6d2-4e1c-aafc-6888219027cc']
```

## Packing

Now, we have the five lists `job`, `location`, `division`, `dept` and `link`. We can pack them as the columns of a Pandas data frame:

```
In [17]: import pandas as pd
```

```
In [18]: df = pd.DataFrame({'job': job, 'location': location, 'division': division, 'dept': dept, 'link': link})
    ...: df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 253 entries, 0 to 252
Data columns (total 5 columns):
 #   Column    Non-Null Count  Dtype 
---  ------    --------------  ----- 
 0   job       253 non-null    object
 1   location  253 non-null    object
 2   division  253 non-null    object
 3   dept      253 non-null    object
 4   link      253 non-null    object
dtypes: object(5)
memory usage: 10.0+ KB
```

```
df.head()
Out[19]: 
                                                 job                 location   
0             Production Pipeline Technical Director  Los Angeles, California  \
1  Administrative Assistant, Technology - Feature...      Burbank, California   
2  Software Engineer (L4), Applications Engineeri...      Burbank, California   
3  Software Engineer (L4), Pipeline Engineering -...      Burbank, California   
4                            Animator - Games Studio    Remote, United States   

    division                      dept   
0  Animation                 Animation  \
1  Animation                Technology   
2  Animation                Technology   
3  Animation                Technology   
4     Gaming  Boss Fight Entertainment   

                                                link  
0  https://jobs.lever.co/netflix/f0615765-1451-42...  
1  https://jobs.lever.co/netflix/f83c8247-b863-48...  
2  https://jobs.lever.co/netflix/e8ac657b-05d0-49...  
3  https://jobs.lever.co/netflix/44912894-f070-49...  
4  https://jobs.lever.co/netflix/64e3cbb4-b6d2-4e...  
```

## Exporting the data to a CSV file

Finally, we can export the data to a CSV file by means of the method `.to_csv()`. You can edit the path of the file if you don't it to be placed in the working directory.

```
In [20]: df.to_csv('netflix.csv', index=False)
```

The argument `index=False` has been used to skip the default of `.to_csv()`, which adds the index as the first column.

## Homework

1. The Netflix Lever page also contains a **workplace type** label, such as *ON-SITE* or *REMOTE*. Add this field to the data set.

2. An additional label, such as *FULL-TIME* or *PIPELINE*, indicates the **commitment**. Add this field to the the data set. Note that this label is sometimes missing, so `.find_all()` will return a shorter list, that will not match the other lists. You have to use a process that allows for placing a `NaN` value where the commitment is missing.
