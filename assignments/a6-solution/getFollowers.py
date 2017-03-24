import twitter

outfile = open("twitterFollowers.txt", 'w')
# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '824794440409706496-CGUoqhcZpfk4lOcblNVG1OuubwaCqZp'
ACCESS_SECRET = 'Mgd7wctkwI3nNUL6RHD4Cqjg9HVngccRrynoWfEsTUzlJ'
CONSUMER_KEY = '72haUMMgwOXNNGXXz4G0N7B9m'
CONSUMER_SECRET = 'zSx800UtH7OUTkVUMw2uORB39o1aP59uZgmXMWo8AZpoFkNgJQ'

api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_SECRET,
                  sleep_on_rate_limit=True)

user = api.GetUser(screen_name="mango964")
userdict = user.AsDict()
userid = userdict["id"]

followerslist=[]
followersdata = api.GetFollowerIDsPaged(user_id=userid)
next_cursor = followersdata[0]
followerslist.extend(followersdata[2])

while next_cursor != 0 :
    followersdata = api.GetFollowerIDsPaged(user_id=userid, cursor=next_cursor)
    next_cursor = followersdata[0]
    followerslist.extend(followersdata[2])

outfile.write(str(userid)+ "\n")
for item in followerslist:
    outfile.write(str(item) + "\n")
    

outfile.close()
