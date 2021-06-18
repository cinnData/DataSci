# 9. Twitter data in Python

### The Twitter API

The main social networks, including Twitter, have an **application programming interface** (API). The API allows accessing the network database in a programmatic way (see `developer.twitter.com/en/docs/twitter-api` for an overview of the Twitter API). The Twitter API involves the user **authentication**, which is carried out by means of a standard protocol called **OAuth** (see `oauth.net`).

In practice, the procedure is simple: an authorization server issues a set of passwords, called **tokens**, to the API client, which uses them to access the resources hosted by a resource server. In the case of Twitter, you have to make two steps:

* Register in Twitter, if you are not already registered, by creating an account under a Twitter username.

* Create an application in the Twitter Applications website (`apps.twitter.com`). As a result, you get four tokens: the **Consumer Key**, the **Consumer Secret**, the **Access Token** and the **Access Token Secret**. The tokens are needed to authenticate you before starting a tweet search.

Strictly speaking, the Twitter API is not an API, but a set of API's. There is the **REST API**, for downloads one-at-a-time, and the **Streaming API**, for real-time tweet processing. In this note, I use the **Twitter Search API**, which is an element of the REST API which allows queries by content. 

### Capturing Twitter data

You can capture Twitter data by querying the page `api.twitter.com/1.1/search/tweets.json`, using your favorite language. Let me assume that you are using Python. 

It is worth refreshing some facts about the limitation for the length of the tweets. The initial 140-character limit set to tweets made them manageable, and no normalization for the document length was needed. Moreover, although tweets could look as poor writing (they were), the length limit forced the writer to use a simple style which facilitated the analysis. By October 2017, Twitter raised the limit to 280 characters. A year later, they observed that people tweeted more under the new limit, but the tweets were not longer.

Since this change is still recent, you may find in tutorials and books traces of the old 140-character limitation. Also, some programming tools were designed to deal with the old Twitter, and they truncate the tweets that are longer than 140 characters. Their maintenance may have been discontinued owing to this fact. 

In Python, if you wish to capture just a few tweets every day, you will have enough with the Requests function `get`, which has already appeared in this course. If you are more ambitious, you will find more powerful Twitter-focused packages in the Python ecosystem. The current favorite is Tweepy (`tweepy`). 

### How do Twitter data look?

Before giving more detail, let me be specific. THis note deals with the **Standard Search API**, which is free and has limitations, which can be overcome with the premium and enterprise search API's. Also, we discuss here version v1.1. When this is being written, version 2 has already been released, but it is not yet supported by Tweepy. You can follow the track of the new version in  `developer.twitter.com/en/docs/twitter-api/migrate`.

A visit to `developer.twitter.com/en/docs/twitter-api/v1/tweets/search/api-reference/get-search-tweets` can give you an idea of what kind of data can be extracted with the Twitter Search API. The data format is JSON, which makes Python welcome, since JSON documents are easily converted into lists and dictionaries. You get these data by querying the site `api.twitter.com/1.1/search/tweets.json`. 

An example of the server response is displayed on the reference page. This example has probably not been updated since the times of the 140-character limitation, so it is not exactly what you would get right now, though it still helps to understand the structure of the data released by Twitter. 

Even if the current response format is a bit different, you will notice that the server delivers a JSON document which can be managed in Python as a dictionary with two elements, `statuses` and `search_metadata`. Note that a **status** is a Twitter data unit.
