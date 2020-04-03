pip install tweepy

import os
import tweepy as tw
import pandas as pd


#Keys and Access Tokens
consumer_key       = ''
consumer_secret    = ''
access_token       = ''
access_token_secret= ''


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)




def search_tweets(language, hashtag, date, number): # You must input language, hashtag, date and number
    
    # Define the search term and the date_since date as variables
    search_words = hashtag
    date_since = date
    new_search = search_words + " -filter:retweets" # Do not get retweet of tweets
    
    
    # Collect tweets
    tweets = tw.Cursor(api.search, q=new_search, lang=language, since=date_since  ).items(number)

    users_locs = [[tweet.user.id_str, tweet.user.screen_name, tweet.user.location, 
                    tweet.created_at, tweet.text, tweet.user.followers_count, 
                    tweet.retweet_count, tweet.favorite_count] for tweet in tweets]
    
    
    # Covert to Dataframe
    tweet_text = pd.DataFrame(data=users_locs, columns=[ 'Id', 'username', 'location','time_stamp', 
                                                        'text', 'followers_count', 'retweet_count', 
                                                        'favorite_count'])
    
    
    # return Dataframe
    return tweet_text 


# Call function search_tweets
# Hashtag Covid-19
covid19 = search_tweets('en', '#COVID19', '2020-01-01', 2000)


# Export Dataframe to Excel file
covid19.to_excel(r'path\file_name.xlsx', encoding='utf-8-sig', index = False)


