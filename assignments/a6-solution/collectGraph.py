import twitter 

outfile = open("links.txt", "w")

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

#print(userList)

#see if two users have a relationship
#don't check the same people twice
for idx, source in enumerate(userList):
    if idx != (len(userList) - 1):
        for target in userList[idx + 1:]:
            try:
                result = api.ShowFriendship(source_user_id= source ,target_user_id = target)
                following = result["relationship"]["target"]["following"]
                print(following)
                follows   = result["relationship"]["target"]["followed_by"]
                print(follows)
                source_name = result["relationship"]["source"]["screen_name"]
                target_name = result["relationship"]["target"]["screen_name"]
                
                if following:
                    print("TRUE")
                    outfile.write(str(source_name) + "\t" + str(target_name) + "\n")
                if follows:
                    print("TRUE")
                    outfile.write(str(target_name) + "\t" + str(source_name) + "\n")
            except Exception as err:
                print(err)
                print(source)            

outfile.close()
