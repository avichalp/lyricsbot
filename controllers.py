import models
import os
import tweetprocessor
import abc
import utils
import models
from random import randint

def tweet_lyrics():
	
	ly_tweet_collection = []
	artist = models.get_random_artist()
		
	raw_lyrics = filter(lambda y: y != '\n', models.getlyrics(artist,False))
	
	while raw_lyrics:
		tweet = utils.create_tweet(raw_lyrics)
		ly_tweet_collection.append(tweet)
		raw_lyrics = [x for x in tweet if x not in raw_lyrics ]

	models.write_tweet(ly_tweet_collection[randint(0,len(ly_tweet_collection)-1)])

					 	
def tweet_quotes():
	
	""""calls writetweet fuunction from models """
	
	models.write_tweet(models.get_random_quote())
			
	
