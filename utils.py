import urllib
import os


def create_tweet(raw_lyrics):
	
	tweet = []
	for _ in raw_lyrics:
		if len(str(tweet)) < 140:
			tweet.append(_)		
		if len(str(tweet)) > 140:
			tweet.pop(-1)
			break

	return tweet


def flush():
	if not os.stat('tweet_buffer.txt')[6]==0:
		filename=open('tweet_buffer.txt','w')
		filename.close()


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
