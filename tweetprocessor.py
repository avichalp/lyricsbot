		
def write_tweet(tweet):
	
	filename = open('tweet_buffer.txt','w')
	for some in tweet:
		filename.write(some+'\n')
	filename.close()

