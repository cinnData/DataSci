## Tutorial - Tweepy ##

# Install Tweepy (if you need it) #
%pip install tweepy
%conda install -c conda-forge tweepy

# Capturing tweets with Tweepy #
consumer_key = '9PQLhrb4ZUvte5Cb2VZRa7wce'
consumer_secret = 'Xxkae5otxok1j30dwPNLgScJKzvLqSKJcvU77D13azYCDmoO1D'
access_key = '2795394087-drbIfGPKwFZTfiNIKYXUqUrUvg1ypC2A7DfdXal'
access_secret = 'FfN5Up4WtArKoLlitGUC2ukXKElmyA7paMpYphVxGQhlP'
import tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
twcursor = tweepy.Cursor(api.search_tweets, q='@AmericanAir OR #americanair', until='2021-11-01', 
  result_type='recent', lang='en', tweet_mode='extended').items(250)
type(twcursor)
twlist = [t._json for t in twcursor]

# Organizing the data #
len(twlist)
twlist[0].keys()
twlist[5].keys()
import pandas as pd
twdf = pd.DataFrame(twlist)
id = [t['id'] for t in twlist]
id[:10]
created_at = [t['created_at'] for t in twlist]
created_at[:10]
is_retweet = [int('retweeted_status' in t.keys()) for t in twlist]
is_retweet[:10]
text = [t['full_text'] for t in twlist]
text[:5]
for i in range(len(twlist)):
  if is_retweet[i] == 1:
    text[i] = twlist[i]['retweeted_status']['full_text']
twdf = pd.DataFrame({'created_at': created_at, 'text': text,
  'is_retweet': is_retweet}, index=id)
twdf.head()
