import models
import os
import tweetprocessor
import abc
import utils
import models
import redis
from models import Quotes, Lyrics
from random import randint


def tweet_lyrics():
	
	redis_server = redis.Redis('localhost')	
	#ly_tweet_collection = []
	ly = Lyrics()
	ly.api_call()
	
	raw_lyrics = filter(lambda y: y != '\n', ly.getlyrics(False))
	count = 0
	while raw_lyrics:
		tweet = utils.create_tweet(raw_lyrics)
		#ly_tweet_collection.append(tweet)
		redis_server.rpush('tweet_collection',tweet)
		count+=1
		raw_lyrics = [x for x in tweet if x not in raw_lyrics ]

	ready_tweet = redis_server.lindex('tweet_collection',randint(0,count-1))

	ly.write_tweet(ready_tweet)

					 	
def tweet_quotes():
	q = Quotes()
	q.write_tweet(q.api_call())
			
	
