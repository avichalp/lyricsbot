import lxml.html
import lxml.cssselect
import abc
import utils
import redis
from random import randint


class Tweet(object):
	
	__metaclass__ = abc.ABCMeta
			
	def write_tweet(self,tweet):
		
		redis.Redis('localhost').set('tweet', tweet)

		
	@abc.abstractmethod	
	def api_call(self,url):
		
		pass


class Quotes(Tweet):
	
	url =  "http://www.iheartquotes.com/api/v1/random?max_characters=140&show_source=0&show_permalink=0"

	def api_call(self):

		try:
			quote = lxml.html.parse(self.url).getroot()[0][0].text.split('\n')[:-2]
			
		except IOError:
			raise
	
		return quote



class Lyrics(Tweet):
			
	artist_url =  "http://lyrics.wikia.com/api.php?func=getArtist&artist="+ utils.get_random_artist()
	song_url = ""
	
	def api_call(self):
	
		try:
			disco = lxml.html.parse(self.artist_url)
		
		except IOError:
			print ' could not connect to lyrics wiki(artist page). '
			raise
			
		albums_songs = {}
		ul= disco.getroot().cssselect('.albums')
		
		for i in range(len(ul[0])):
			album_name = ul[0][i][0].text
			albums_songs[album_name] = ul[0][i][2]
		
		key= albums_songs.keys()[randint(0,len(albums_songs.keys())-1)]
		self.song_url = albums_songs[key][0][0].get('href')
		
		return



	def getlyrics(self, fuzzy=False):
	
		try:
			doc = lxml.html.parse(self.song_url)
	
		except IOError:
			raise
	
		try:
			lyricbox = doc.getroot().cssselect(".lyricbox")[0]
	
		except IndexError:
			print 'connection successful but album-feed is not in proper format.'
			raise
		except TypeError:
			print 'connection successful but album-feed is not in proper type.'
			raise

			# look for a sign that it's instrumental
		if len(doc.getroot().cssselect(".lyricbox a[title=\"Instrumental\"]")):
			print 'Instrumental'
	
		# prepare output
		lyrics = []
		if lyricbox.text is not None:
			lyrics.append(lyricbox.text)
		for node in lyricbox:
			if str(node.tag).lower() == "br":
				lyrics.append("\n")
			if node.tail is not None:
				lyrics.append(node.tail)
	
		return lyrics
