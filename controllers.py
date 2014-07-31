import models
import os
import tweetprocessor
import abc
import utils
from random import randint

def tweet_lyrics():
	
	ly_tweet_collection = []
	artist = get_random_artist()
		
	raw_lyrics = filter(lambda y: y != '\n', models.getlyrics(artist,False))
	
	while raw_lyrics:
		tweet = utils.create_tweet(raw_lyrics)
		ly_tweet_collection.append(tweet)
		raw_lyrics = [x for x in tweet if x not in raw_lyrics ]

	tweetprocessor.write_tweet(ly_tweet_collection[randint(0,len(ly_tweet_collection)-1)])

					 	
def tweet_quotes():
	
	""""calls writetweet fuunction from tweetprocessor module """
	
	tweetprocessor.write_tweet(models.get_random_quote())
			
	
def get_random_artist():
	
	"""chose a random artist from list of artists in the text file """
	
	artist_list = []
	artist_file = open('artist.txt', 'r+')

	for line in artist_file:
		artist_list.append(line)

	return utils.lyricwikicase(artist_list[randint(0,len(artist_list)-1)])

	
