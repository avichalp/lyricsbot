import urllib
import sys
import os
import re
import subprocess
import lxml.html
import lxml.cssselect
from random import randint

def lyricwikicase(s):
	"""Return a string in LyricWiki case.
	Substitutions are performed as described at 
	<http://lyrics.wikia.com/LyricWiki:Page_Names>.
	Essentially that means capitalizing every word and substituting certain 
	characters."""

	words = s.split()
	newwords = []
	for word in words:
		newwords.append(word[0].capitalize() + word[1:])
	s = "_".join(newwords)
	s = s.replace("<", "Less_Than")
	s = s.replace(">", "Greater_Than")
	s = s.replace("#", "Number_") # FIXME: "Sharp" is also an allowed substitution
	s = s.replace("[", "(")
	s = s.replace("]", ")")
	s = s.replace("{", "(")
	s = s.replace("}", ")")
	s = urllib.urlencode([(0, s)])[2:]
	return s

def lyricwikipagename(artist, title):
	"""Return the page name for a set of lyrics given the artist and 
	title"""

	return "%s:%s" % (lyricwikicase(artist), lyricwikicase(title))

def lyricwikiurl(artist, title, edit=False, fuzzy=False):
	"""Return the URL of a LyricWiki page for the given song, or its edit 
	page"""

	if fuzzy:
		base = "http://lyrics.wikia.com/index.php?search="
		pagename = artist + ':' + title
		if not edit:
			url = base + pagename
			doc = lxml.html.parse(url)
			return doc.docinfo.URL
	else:
		base = "http://lyrics.wikia.com/"
		pagename = lyricwikipagename(artist, title)
	
	if edit:
		if fuzzy:
			url = base + pagename
			doc = lxml.html.parse(url)
			return doc.docinfo.URL + "&action=edit"
		else:
			return base + "index.php?title=%s&action=edit" % pagename
	
	return base + pagename

def getlyrics(artist, title, fuzzy=False):
	"""Get and return the lyrics for the given song.
	Raises an IOError if the lyrics couldn't be found.
	Raises an IndexError if there is no lyrics tag.
	Returns False if there are no lyrics (it's instrumental)."""

	try:
		doc = lxml.html.parse(lyricwikiurl(artist, title, fuzzy=fuzzy))
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
	
	
	artist = 'porcupine tree'
	
	song = 'russia on ice'
	
	raw_tweet = filter(lambda y: y != '\n', getlyrics(artist,song,False))
	tweet_collection = []
	
	while raw_tweet:
		c=create_tweet(raw_tweet)
		tweet_collection.append(c)
		for _ in c:
			if _ in raw_tweet:
				raw_tweet.pop(raw_tweet.index( _ ))
	
	for some in tweet_collection[randint(0,len(tweet_collection)-1)]:
		print some
	
	
		
