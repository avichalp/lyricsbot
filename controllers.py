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
	lyrics = Lyrics()
	lyrics.api_call()
	raw_lyrics = filter(lambda y: y != '\n', lyrics.getlyrics(False))
	
	utils.lyrics_tweet_collection(raw_lyrics)
	
	lyrics.write_tweet(redis_server.lindex('tweet_collection',randint(0,redis_server.llen('tweet_collection')-1)))

					 	
def tweet_quotes():


	quote = Quotes()
	quote.write_tweet("\n".join(quote.api_call()))
			
	
if __name__ == '__main__' :
	
	tweet_quotes() if randint(0,1) == 0 else tweet_lyrics()
