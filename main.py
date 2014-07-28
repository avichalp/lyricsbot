import urllib
import lyrics
import quotes
import os
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

	
def create_tweet(raw_lyrics):
	
	tweet = []
	for _ in raw_lyrics:
		if len(str(tweet)) < 140:
			tweet.append(_)		
		if len(str(tweet)) > 140:
			tweet.pop(-1)
			break

	return tweet
	
	
def write_tweet(tweet):
	
	filename = open('tweet_buffer.txt','w+')
	for some in tweet:
		filename.write(some+'\n')


def tweet_lyrics():
	
	artist = get_random_artist()
	ly_tweet_collection = []
	
	#genrate lyrics		
	raw_lyrics = filter(lambda y: y != '\n', lyrics.getlyrics(artist,False))
	
	#collecting all probable tweets and removing them from raw_lyrics
	while raw_lyrics:
		tweet = create_tweet(raw_lyrics)
		ly_tweet_collection.append(tweet)
		raw_lyrics = [x for x in tweet if x not in raw_lyrics ]

	# writes a random tweet from collectoion to txt file
	tweet = ly_tweet_collection[randint(0,len(ly_tweet_collection)-1)]	
	if os.stat('tweet_buffer.txt')[6]==0:
		write_tweet(tweet)
	else:
		filename=open('tweet_buffer.txt','w')
		filename.close()
		print 'file was not empty'
		write_tweet(tweet)

def tweet_quotes():
	
	#genrates quotes
	raw_quote = quotes.get_random_quote()
	if os.stat('tweet_buffer.txt')[6]==0:
		write_tweet(raw_quote)
	else:
		filename=open('tweet_buffer.txt','w')
		filename.close()
		print 'file was not empty'
		write_tweet(raw_quote)	 

	
if __name__ == '__main__':
	
	random_choice = randint(0,1)
	
	if random_choice == 0:
		tweet_quotes()
		
	if random_choice == 1:
		tweet_lyrics()
	
	
	
	
