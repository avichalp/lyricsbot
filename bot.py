import tweepy
import os

def auth():
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)
	return api
 
def get_tweet():
	filename = open('tweet_buffer.txt','r')
	f = filename.readlines()
	filename.close()
	tweet = [] 
	for line in f:
		tweet.append(line)
		
	tweet = "".join(tweet)
	return tweet

def post_tweet(api,tweet):
	api.update_status(tweet)
	#print tweet

def flush():
	if not os.stat('tweet_buffer.txt')[6]==0:
		filename=open('tweet_buffer.txt','w')
		filename.close()

	
if __name__ == '__main__':
		
	access_file = open('/home/avichal/devlopment/twitter_access.txt','r')
	f= access_file.readlines()
	access_file.close()

	CONSUMER_KEY = f[0].strip('\n') 
	CONSUMER_SECRET = f[1].strip('\n')
	ACCESS_KEY = f[2].strip('\n')
	ACCESS_SECRET = f[3].strip('\n')

	api = auth()
	tweet = get_tweet()
	post_tweet(api,tweet)
	flush()
		
	