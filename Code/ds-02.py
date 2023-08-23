## [DS-02] String data in Python ##

# Strings as sequences #
iese = 'IESE Business School'
len(iese)
iese[5:]
iese[:4] + ', A way to learn'
'IE' in iese

# Python string methods #
iese.lower()
iese.replace('IESE', 'Iese')
iese.split()
iese.split('i')
iese.count('s')

# Pandas string methods #
import pandas as pd
pres = pd.Series(['Donald Trump', 'Joe Biden', '', None])
pres
pres.str.len()
pres.str[0]
pres.str.lower()
pres.str.replace(' ', '-')
pres.str.split()
pres.str.count('e')
pres.str.contains('a')
pres = pres[~(pres.isna())]
pres[~pres.str.contains('a')]
pres.str.findall('e')

# Regular expressions #
bio = pd.Series(['I was born in 1954', 'My phone is +34 932 534 200'])
bio.str.replace('[a-z]', 'x', regex=True)
bio.str.replace('[0-9]', 'x', regex=True)
bio.str.replace('[a-z]+', 'x', regex=True)
bio.str.split('\W+', regex=True)
people = pd.Series(['John - male', 'Nancy - female', 'Bruno - male'])
people.str.replace(' - .+', '', regex=True)
comment = pd.Series(['Sally and Tim came to dinner. A nice couple.'])
comment.str.count('.')
comment.str.count('\.')
