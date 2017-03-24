#format the friendships and people from the twitter data into json
#so that the graphing program can read it
import json
from random import randint


data = []
node= {}
with open("userNames.txt", "r") as nodefile:
    for node in nodefile:
        node = node.strip()
        data.append({"id" : node, "group" : str(randint(1,5))})
data2= []
with open("links.txt", "r") as linkfile:
    for link in linkfile:
        link = link.strip()
        wordlist = link.split("\t")
        data2.append({"source" : wordlist[0], "target" : wordlist[1], "value" : "4"})
final = {"nodes": data, "links" : data2}
#create node dictionary
with open("data.json", "w") as fp:
    json.dump(final, fp, sort_keys = True, indent = 4)


