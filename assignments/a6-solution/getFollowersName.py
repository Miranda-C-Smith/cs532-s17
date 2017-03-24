import twitter
import json

outfile = open("userNames.txt", "w")

ACCESS_TOKEN = '824794440409706496-CGUoqhcZpfk4lOcblNVG1OuubwaCqZp'
ACCESS_SECRET = 'Mgd7wctkwI3nNUL6RHD4Cqjg9HVngccRrynoWfEsTUzlJ'
CONSUMER_KEY = '72haUMMgwOXNNGXXz4G0N7B9m'
CONSUMER_SECRET = 'zSx800UtH7OUTkVUMw2uORB39o1aP59uZgmXMWo8AZpoFkNgJQ'

api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_SECRET,
                  sleep_on_rate_limit=True)


userList=[]
for line in open('twitterFollowers.txt', 'r'):
    line = line.strip()
    userList.append(line.strip())



#get user names from IDs
results = api.UsersLookup(user_id = userList)

for result in results:
    outfile.write(result.screen_name + "\n")
                        
outfile.close()
