import urllib
import lyrics
import quotes
import os
import tweetprocessor
from random import randint

def lyricwikicase(s):

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
	
	artist_list = []
	artist_file = open('artist.txt', 'r+')

	for line in artist_file:
		artist_list.append(line)

	artist = artist_list[randint(0,len(artist_list)-1)]
	return lyricwikicase(artist)


def tweet_lyrics():
	
	artist = get_random_artist()
	ly_tweet_collection = []
	
	#genrate lyrics		
	raw_lyrics = filter(lambda y: y != '\n', lyrics.getlyrics(artist,False))
	
	#collecting all probable tweets and removing them from raw_lyrics
	while raw_lyrics:
		tweet = tweetprocessor.create_tweet(raw_lyrics)
		ly_tweet_collection.append(tweet)
		raw_lyrics = [x for x in tweet if x not in raw_lyrics ]

	# writes a random tweet from collectoion to txt file
	tweet = ly_tweet_collection[randint(0,len(ly_tweet_collection)-1)]	
	if os.stat('tweet_buffer.txt')[6]==0:
		tweetprocessor.write_tweet(tweet)
	else:
		filename=open('tweet_buffer.txt','w')
		filename.close()
		print 'file was not empty'
		tweetprocessor.write_tweet(tweet)


def tweet_quotes():
	
	#genrates quotes
	raw_quote = quotes.get_random_quote()
	if os.stat('tweet_buffer.txt')[6]==0:
		tweetprocessor.write_tweet(raw_quote)
	else:
		filename=open('tweet_buffer.txt','w')
		filename.close()
		print 'file was not empty'
		tweetprocessor.write_tweet(raw_quote)	
