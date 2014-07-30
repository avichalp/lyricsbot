import urllib
import lyrics
import quotes
import os
import tweetprocessor
import abc
from random import randint

def tweet_lyrics():
	
	ly_tweet_collection = []
	artist = get_random_artist()
		
	raw_lyrics = filter(lambda y: y != '\n', lyrics.getlyrics(artist,False))
	
	while raw_lyrics:
		tweet = tweetprocessor.create_tweet(raw_lyrics)
		ly_tweet_collection.append(tweet)
		raw_lyrics = [x for x in tweet if x not in raw_lyrics ]

	tweetprocessor.write_tweet(ly_tweet_collection[randint(0,len(ly_tweet_collection)-1)])

					 	
def tweet_quotes():
	
	""""write a random quote in the text file """
	
	tweetprocessor.write_tweet(quotes.get_random_quote())

		
def lyricwikicase(s):
	
	"""format the artist name to make the url """

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
	
	
def get_random_artist():
	
	"""chose a random artist from list of artists in the text file """
	
	artist_list = []
	artist_file = open('artist.txt', 'r+')

	for line in artist_file:
		artist_list.append(line)

	artist = artist_list[randint(0,len(artist_list)-1)]
	return lyricwikicase(artist)

	
