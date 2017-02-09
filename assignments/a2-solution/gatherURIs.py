#http://socialmedia-class.org/twittertutorial.html

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import urllib.request
from urllib.parse import urlparse

file = open('urlList', 'a') #a = append

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '824794440409706496-CGUoqhcZpfk4lOcblNVG1OuubwaCqZp'
ACCESS_SECRET = 'Mgd7wctkwI3nNUL6RHD4Cqjg9HVngccRrynoWfEsTUzlJ'
CONSUMER_KEY = '72haUMMgwOXNNGXXz4G0N7B9m'
CONSUMER_SECRET = 'zSx800UtH7OUTkVUMw2uORB39o1aP59uZgmXMWo8AZpoFkNgJQ'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.sample()


tweet_count = 9000
for tweet in iterator:
    if 'entities' in tweet:
        entities = tweet['entities']
        for url in entities['urls']:
            try:
                file.write(url['expanded_url'])
                file.write("\n")
                tweet_count = tweet_count - 1
                print(tweet_count)
            except:
                pass
            if tweet_count <= 0:
                break
        if tweet_count <=0:
            break
file.close()

