import lxml.html
import lxml.cssselect
from random import randint

def get_song_name(artist):

	url = "http://lyrics.wikia.com/api.php?func=getArtist&artist="+artist
	
	try:
		disco = lxml.html.parse(url)
		
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

def getlyrics(artist, fuzzy=False):
	
	try:
		doc = lxml.html.parse(get_song_name(artist))
	except IOError:
		raise

	try:
		lyricbox = doc.getroot().cssselect(".lyricbox")[0]
	except IndexError:
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


	
	
		
