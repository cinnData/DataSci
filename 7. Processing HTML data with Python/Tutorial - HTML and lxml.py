## Tutorial - HTML and lxml ##

# Parsing TML code #
page = '<html> \
  <head> \
  <title>Data Viz</title> \
  </head> \
  <body> \
  <div class="course" >Data Visualization</div> \
  <div class="program">MBA full-time</div> \
  <a class="professor", \
  href="https://www.iese.edu/faculty-research/faculty/miguel-angel-canela">Miguel Ángel Canela</a> \
  </body> \
  </html>'
page
from lxml import html
tree = html.fromstring(page)
tree
type(tree)
tree[0]
tree[1]
tree[1][0]
tree[1][0].text
tree[1][0].attrib['class']

# The function xpath #
tree.xpath('/html/body/div')
tree.xpath('//div')
tree.xpath('/html/body/div[@class="course"]')

# Extracting information from the nodes #
tree.xpath('//div/text()')
tree.xpath('//div')[0].text
tree.xpath('//a/@href')[0]
tree.xpath('//a')[0].attrib['href']
