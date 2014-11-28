import models
import os
import abc
import utils
import models
import redis
from models import Quotes, Lyrics
from random import randint


def tweet_lyrics():
	

	"""instantiate lyrics class and write tweet """
	
	redis_server = redis.Redis('localhost')	
	lyrics = Lyrics()
	
	try :
		lyrics.api_call()		
	
	except IOError :
		print 'could not connect to lyrics wiki(artist page)'
	
	else :
		try:
			raw_lyrics = filter(lambda y: y != '\n', lyrics.getlyrics(False))
		except IndexError:
			print 'connection successful but albums_feed is not in proper format'
		except TypeError:
			print 'connection successful but album-feed is not in proper type.'
		else :

			# makes a collection of tweets from raw lyrics and put collection in redis-store
			utils.lyrics_tweet_collection(raw_lyrics)
	
			# randomly extract a tweet from collection in redis and call writetweet from Lyrics class
			lyrics.write_tweet(redis_server.lindex('tweet_collection',randint(0,redis_server.llen('tweet_collection')-1)))

					 	
def tweet_quotes():


	"""intantiate quote class and writes tweet"""
	
	quote = Quotes()
	
	try:
		quote.write_tweet("\n".join(quote.api_call()))
	
	except IOError:
		print 'cannnot fetch the quote'

	
if __name__ == '__main__' :
	
	tweet_quotes() if randint(0,1) == 0 else tweet_lyrics()
