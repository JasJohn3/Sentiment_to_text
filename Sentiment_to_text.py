#Twitter Sentiment to text Analysis
#Testing Github Update from pycharm

import tweepy
from textblob import TextBlob

consumer_key = 'ArdXLxDwcRIT1NZoRzfp1B2FT'
consumer_secret = 'dhe5SaWIrqhnoOn6dyWiYMElOH75n3ISeOenvzBgEZh4RR1DcQ'
access_token = '386157913-Fuy6MxHBHlMCuJyQaQ5z8EVJCbImD1hs1IlG8KO1'
access_token_secret = 'HItfC9VQE4CATVlqR36KWJVkMhhgGYcMwXqUW5IDQpiHh'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
Readme_file = open('Readme.txt','r')
message = Readme_file.read()
print(message)
Readme_file.close()
print("Please Enter the Word you would like to perform a sentiment analysis on!")
User_Input = input()
User_Tweet_Search_Size = int(input("Please enter how large you want your search to be: "))


#Retrieve Tweets
public_tweets = api.search(q=User_Input, count= User_Tweet_Search_Size)
counter = 0
file = open(User_Input+'.txt','w')
message = file.write(User_Input)


for tweet in public_tweets:
    counter = counter + 1
    string_counter = str(counter)
    counter_write=file.write(string_counter)
    tweet_message =file.write(tweet.text)
    analysis = TextBlob(tweet.text)
    string_analysis = str(analysis.sentiment)
    Sentiment_message = file.write(string_analysis)


full_sentiment_message = file.read()
print(full_sentiment_message)
file.close()