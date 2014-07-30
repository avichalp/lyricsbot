from controllers import Lyrics,Quotes
from random import randint
	
Lyrics().tweet_lyrics() if randint(0,1) == 0 else Quotes().tweet_quotes()		
	
	
	
