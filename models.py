import lxml.html
import lxml.cssselect
from random import randint


def write_tweet(tweet):
	
	filename = open('tweet_buffer.txt','w')
	for some in tweet:
		filename.write(some+'\n')
	filename.close()



def get_random_artist():
	
	"""chose a random artist from list of artists in the text file """
	
	artist_list = []
	artist_file = open('artist.txt', 'r+')

	for line in artist_file:
		artist_list.append(line)

	return utils.lyricwikicase(artist_list[randint(0,len(artist_list)-1)])


def get_random_quote():

	url = "http://www.iheartquotes.com/api/v1/random?max_characters=140&show_source=0&show_permalink=0"
	
	try:
		quote = lxml.html.parse(url)
		
	except IOError:
		raise
	
	try:
		quote = quote.getroot()[0][0].text
	
	except IndexError:
		raise

	raw_qoute = quote.split('\n')
	raw_qoute.pop(-2)
	return raw_qoute

	
def get_song_name(artist):

	url = "http://lyrics.wikia.com/api.php?func=getArtist&artist="+artist
	
	try:
		disco = lxml.html.parse(url)
		
	except IOError:
		print ' could not connect to lyrics wiki(artist page). '

	try:
		albums_songs = {}
	ul= disco.getroot().cssselect('.albums')
		
		for i in range(len(ul[0])):
			album_name = ul[0][i][0].text
			albums_songs[album_name] = ul[0][i][2]
		
		key= albums_songs.keys()[randint(0,len(albums_songs.keys())-1)]
		return albums_songs[key][0][0].get('href')
	
	except IndexError:
		print 'connection successful but artist-feed(discography) is not in proper format.'
	
	except TypeError:
		print 'connection successful but artist-feed(discograpy) is not in proper type.'

def getlyrics(artist, fuzzy=False):
	
	try:
		doc = lxml.html.parse(get_song_name(artist))
	
	except IOError:
		print 'could not connect to lyrics wiki(discogarphy page of an artist).'
		raise
	except TypeError:
		print 'could not connect to the url'
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


	
	
		
