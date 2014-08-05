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
	ly = Lyrics()
	ly.api_call()
	raw_lyrics = filter(lambda y: y != '\n', ly.getlyrics(False))
	
	utils.lyrics_tweet_collection(raw_lyrics)
	
	#TODO: get the length of the array from redis server and replace it with count
	ly.write_tweet(redis_server.lindex('tweet_collection',randint(0,count-1)))

					 	
def tweet_quotes():


	q = Quotes()
	q.write_tweet(q.api_call())
			
	
