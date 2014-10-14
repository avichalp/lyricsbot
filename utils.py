import tweepy
import urllib
import os
import redis
from random import randint

def auth():
	
	""" fetches authentication details from a file. use them to login twitter """
	
	CONSUMER_KEY = "..." 
	CONSUMER_SECRET = "..."
	ACCESS_KEY = "..."
	ACCESS_SECRET = "..."
	
	return tweepy.API(tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET).set_access_token(ACCESS_KEY, ACCESS_SECRET))


def get_random_artist():
		
	""" choses a random artist from given txt file """
	
	artist_list = []
	for line in open('artist.txt', 'r+'):
		artist_list.append(line)

	return lyricwikicase(artist_list[randint(0,len(artist_list)-1)])


def create_tweet(raw_lyrics):
	
	""" crate a tweet of less than or equal to 100 characters  """

	tweet = []

	for _ in raw_lyrics:
		tweet.append(_)
		if len(str(tweet)) == 100:
			break
		if len(str(tweet)) < 100:
			continue	
		if len(str(tweet)) > 100:
			tweet.pop(-1)
			break

	return tweet


def lyrics_tweet_collection(raw_lyrics):
	
	""" create and put collection of tweets in data store"""
	
	redis_server = redis.Redis('localhost')

	while raw_lyrics:
		tweet = create_tweet(raw_lyrics)	
		redis_server.rpush('tweet_collection',"\n".join(tweet))
		raw_lyrics = [x for x in tweet if x not in raw_lyrics ]


def lyricwikicase(s):
	
	""" format the artist name to make the url """

	words = s.split()
	newwords = []
	for word in words:
		newwords.append(word[0].capitalize() + word[1:])
	s = "_".join(newwords)
	s = s.replace("<", "Less_Than")
	s = s.replace(">", "Greater_Than")
	s = s.replace("#", "Number_") 
	s = s.replace("[", "(")
	s = s.replace("]", ")")
	s = s.replace("{", "(")
	s = s.replace("}", ")")
	s = urllib.urlencode([(0, s)])[2:]
	return s
