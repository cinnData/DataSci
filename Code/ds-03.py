## [DS-03] HTML data in Python ##

# A toy HTML example #
html_str = '<html>\
<head>\
  <title>Data Viz</title>\
</head>\
<body>\
  <div class="course">Data Visualization</div>\
  <div class="program">MBA full-time</div>\
  <a class="professor" href="faculty-research/faculty/miguel-angel-canela">Miguel Ángel Canela</a>\
</body>\
</html>'
html_str

# Parsing HTML code #
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_str, 'html.parser')
type(soup)
soup

# The tree structure #
soup.head
type(soup.head)
soup.head.title
soup.head.div
soup.div

# The method .find() #
soup.find('div')
soup.find('div', attrs={'class': 'course'})
soup.find('div', 'program')
soup.find('head').find('title')

# The method .find_all() #
soup.find_all('div')
soup.find('head').find_all('div')
soup.find_all('div', 'course')
soup.find_all('div', 'course')[0]

# Extracting information from a tag element #
soup.find('a').string
soup.find_all('div').string
[t.text for t in soup.find_all('div')]
soup.find('a')['href']

# Finding the elements containing a string #
soup.find_all('div', string='Data Visualization')
