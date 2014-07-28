import lxml.html
import lxml.cssselect
from random import randint

def get_random_quote():

	url = "http://www.iheartquotes.com/api/v1/random?max_characters=140&show_source=0&show_permalink=0"
	
	try:
		quote = lxml.html.parse(url)
		
	except IOError:
		raise
	
	quote = quote.getroot()[0][0].text
	raw_qoute = quote.split('\n')
	raw_qoute.pop(-2)
	return raw_qoute




	 
	
		
