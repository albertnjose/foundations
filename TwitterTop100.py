#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
import sys

#Twitter API credentials
consumer_key = "6ntM9rgnj3dpcVliwqHiU4ahr"
consumer_secret = "lreaySlQyZTVrLg0zamhmekqM8svCBFO5q11oZhvYIfRljChHo"
access_key = "346354126-m7hWAVN0UUail5HX9qN2hOHPIZGhGdWGTgWR93nR"
access_secret = "9WbIorL2TPcXV2irZ94nP1gJl79sZmFyzcu7OWDywiN0u"


def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (100 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=100)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(alltweets) < 100:
		print ("getting tweets before %s" % (oldest))
		
		#all subsequent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=100,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print ("...%s tweets downloaded so far" % (len(alltweets)))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[screen_name, tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
	
	#write the csv	
	with open('%s_tweets.csv' % screen_name, 'w') as f:
		writer = csv.writer(f)
		writer.writerow(["user","id","created_at","text"])
		writer.writerows(outtweets)
	
	pass


if __name__ == '__main__':
	#pass in the username of the account you want to download
    twitter_account = input("Insert twitter account name:")	
    get_all_tweets(twitter_account)