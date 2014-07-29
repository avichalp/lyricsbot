
def create_tweet(raw_lyrics):
	
	tweet = []
	for _ in raw_lyrics:
		if len(str(tweet)) < 140:
			tweet.append(_)		
		if len(str(tweet)) > 140:
			tweet.pop(-1)
			break

	return tweet
	
	
def write_tweet(tweet):
	
	filename = open('tweet_buffer.txt','w+')
	for some in tweet:
		filename.write(some+'\n')

