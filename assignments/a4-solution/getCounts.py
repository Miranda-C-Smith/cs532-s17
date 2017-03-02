import tweepy
#from tweepy import Stream
#from tweepy.streaming import StreamListener
from tweepy import OAuthHandler

infile = open("twitterFollowers.txt", 'r')
outfile = open("twitterCounts.txt", 'w')
# Variables that contains the user credentials to access Twitter API 
ACCESS_KEY = '824794440409706496-CGUoqhcZpfk4lOcblNVG1OuubwaCqZp'
ACCESS_SECRET = 'Mgd7wctkwI3nNUL6RHD4Cqjg9HVngccRrynoWfEsTUzlJ'
CONSUMER_KEY = '72haUMMgwOXNNGXXz4G0N7B9m'
CONSUMER_SECRET = 'zSx800UtH7OUTkVUMw2uORB39o1aP59uZgmXMWo8AZpoFkNgJQ'

auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth_handler=auth, wait_on_rate_limit=True)


flist = []
for line in infile:
    line = line.strip()
    flist.append(line)

infile.close()

lower_bound = 0
upper_bound = 99
while lower_bound < len(flist)-1 :
    shortlist = flist[lower_bound: upper_bound]
    followers = api.lookup_users(user_ids = shortlist)
    lower_bound = upper_bound + 1
    upper_bound = lower_bound + 99
    print(len(followers))
    for user in followers:
            
        if user.followers_count:
            outfile.write(str(user.id) + "\t" + str(user.followers_count) + "\n")

outfile.close()
