import utils
import tweepy
import os
import redis
from models import Tweet,Lyrics,Quotes

def auth():
	return tweepy.API(tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET).set_access_token(ACCESS_KEY, ACCESS_SECRET))

def get_tweet():
	redis_server =  redis.Redis('localhost')
	tweet = redis_server.get('tweet')
	redis_server.delete('tweet')
	return tweet

def post_tweet(tweet):
	#api.update_status(tweet)
	print tweet


	
if __name__ == '__main__':
		
	#access_file = open('/home/avichal/devlopment/twitter_access.txt','r')
	#f= access_file.readlines()
	#access_file.close()

	#CONSUMER_KEY = f[0].strip('\n') 
	#CONSUMER_SECRET = f[1].strip('\n')
	#ACCESS_KEY = f[2].strip('\n')
	#ACCESS_SECRET = f[3].strip('\n')

	#api = auth()
	tweet = get_tweet()
	post_tweet(tweet)
	

	
