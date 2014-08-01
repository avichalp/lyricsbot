import models
import os
import tweetprocessor
import abc
import utils
import models
from models import Quotes, Lyrics
from random import randint

def tweet_lyrics():
	
	ly_tweet_collection = []
	ly = Lyrics()
	ly.api_call()
	
	raw_lyrics = filter(lambda y: y != '\n', ly.getlyrics(False))
	
	while raw_lyrics:
		tweet = utils.create_tweet(raw_lyrics)
		ly_tweet_collection.append(tweet)
		raw_lyrics = [x for x in tweet if x not in raw_lyrics ]

	ly.write_tweet(ly_tweet_collection[randint(0,len(ly_tweet_collection)-1)])

					 	
def tweet_quotes():
	q = Quotes()
	q.write_tweet(q.api_call())
			
	
