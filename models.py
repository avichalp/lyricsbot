import lxml.html
import lxml.cssselect
import abc
import utils
import redis
from random import randint

class Tweet(object):
	

	""" abstract class to represent a tweet"""
	
	__metaclass__ = abc.ABCMeta
			
	def write_tweet(self,tweet):
		
		""" a method to write tweets on Redis data-store """
		
		redis.Redis('localhost').set('tweet', tweet)

		
	@abc.abstractmethod	
	def api_call(self,url):

		""""abstract method to make a api-call """
		
		pass


class Quotes(Tweet):
	

	""" this class exetnds Tweet class and implements its api_call method  """

	__url =  "http://www.iheartquotes.com/api/v1/random?max_characters=140&show_source=0&show_permalink=0"

	def api_call(self):

		"""api-call method implementation for Qoutes class """

		try:
			quote = lxml.html.parse(self.__url).getroot()[0][0].text.split('\n')[:-2]
			
		except IOError:
			raise IOError
	
		else :
			return quote

class Lyrics(Tweet):

		
	"""this class extends Tweet class and impements its api_call method"""

	__artist_url =  "http://lyrics.wikia.com/api.php?func=getArtist&artist="+ utils.get_random_artist()
	__song_url = ""
	
	def api_call(self):

		"""api-call method implementataion of Lyrics class """
	
		try:
			disco = lxml.html.parse(self.__artist_url)
		
		except IOError:
			raise IOError
		
		else:
			albums_songs = {}
			ul= disco.getroot().cssselect('.albums')
		
			for i in range(len(ul[0])):
				album_name = ul[0][i][0].text
				albums_songs[album_name] = ul[0][i][2]
		
				key= albums_songs.keys()[randint(0,len(albums_songs.keys())-1)]
				self.__song_url = albums_songs[key][0][0].get('href')
		
			return
		


	def getlyrics(self, fuzzy=False):

		""" method for html parsing of lyrics page and fetchinhg lyrics """
	
		try:
			doc = lxml.html.parse(self.__song_url)
	
		except IOError:
			raise
	
		else:
			try:
				lyricbox = doc.getroot().cssselect(".lyricbox")[0]
	
			except IndexError:
				raise IndexError
			except TypeError:
				raise TypeError

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
