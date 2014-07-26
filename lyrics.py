import urllib
import sys
import os
import re
import subprocess
import lxml.html
import lxml.cssselect
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

def lyricwikipagename(artist, title):
	
	return "%s:%s" % (lyricwikicase(artist), lyricwikicase(title))


def getlyrics(artist, fuzzy=False):
	
	try:
		doc = lxml.html.parse(get_songs(artist))
	except IOError:
		raise

	try:
		lyricbox = doc.getroot().cssselect(".lyricbox")[0]
	except IndexError:
		raise

	# look for a sign that it's instrumental
	if len(doc.getroot().cssselect(".lyricbox a[title=\"Instrumental\"]")):
		return False

	# prepare output
	lyrics = []
	if lyricbox.text is not None:
		lyrics.append(lyricbox.text)
	for node in lyricbox:
		if str(node.tag).lower() == "br":
			lyrics.append("\n")
		if node.tail is not None:
			lyrics.append(node.tail)
	
	#print lyrics
	#return "".join(lyrics).strip()
	return lyrics

def get_songs(artist):

	url = "http://lyrics.wikia.com/api.php?func=getArtist&artist="+ lyricwikicase(artist)
	
	try:
		disco = lxml.html.parse(url)
		print disco.docinfo.URL
	except IOError:
		raise

	try:
		albums_songs = {}
		ul= disco.getroot().cssselect('.albums')
		for i in range(len(ul[0])):
			album_name = ul[0][i][0].text
			albums_songs[album_name] = ul[0][i][2]
		
		key= albums_songs.keys()[randint(0,len(albums_songs.keys())-1)]
		return albums_songs[key][0][0].get('href')
	
	except IndexError:
		raise

		
	#print songs
	#return song 

def create_tweet(raw):	
	tweet=[]		
	for x in raw:
		if len(str(tweet))<140:
			tweet.append(x)
		if len(str(tweet))>140:
			tweet.pop(-1)
			break
	return tweet

if __name__ == '__main__':
		
	artist = 'tool'
	#get_songs('pink floyd')
	#song = 'russia on ice'
	
	raw_tweet = filter(lambda y: y != '\n', getlyrics(artist,False))
	tweet_collection = []
	
	while raw_tweet:
		c=create_tweet(raw_tweet)
		tweet_collection.append(c)
		for _ in c:
			if _ in raw_tweet:
				raw_tweet.pop(raw_tweet.index( _ ))
	
	for some in tweet_collection[randint(0,len(tweet_collection)-1)]:
		print some
	
	
		
