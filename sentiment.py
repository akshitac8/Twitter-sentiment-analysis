# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 18:33:12 2017

@author: asdmin
"""

import tweepy
from textblob import TextBlob
import csv

# Step 1 - Authenticate
consumer_key= ' '
consumer_secret= ''

access_token=''
access_token_secret=''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('',count=100)

def get_label(analysis,threshold=0):
    if  analysis.sentiment.polarity >threshold:
        return "postive"
    else:
        return "negative"
        
file=open('sentiment.csv','w')
file.write('tweet,sentiment_label\n')
for tweet in public_tweets:
    print(tweet.text)
     #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment.polarity)     
    print("")
    file=open('sentiment.csv','a')
    with file as f:
        writer = csv.writer(f)
        writer.writerow([tweet.text.encode("Utf8"),get_label(analysis)])