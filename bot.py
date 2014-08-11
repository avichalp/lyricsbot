import utils
import tweepy
import os
import redis
from models import Tweet,Lyrics,Quotes


def get_tweet():

	redis_server =  redis.Redis('localhost')
	tweet = redis_server.get('tweet')
	redis_server.delete('tweet')
	return tweet


def post_tweet(tweet):

	#api.update_status(tweet)
	print tweet

	
if __name__ == '__main__':
		
	#api = utils.auth()
	post_tweet(get_tweet())
	

	
