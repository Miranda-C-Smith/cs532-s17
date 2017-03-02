from pygraphml import Graph
from pygraphml import GraphMLParser
import statistics as stat

outfile = open("facebookFriendCount.txt", 'w')
parser = GraphMLParser()
g = parser.parse("mln.graphml")
nodes = g.nodes()

friendcounts = []
for friend in range(0,len(nodes)):
    try:
        outfile.write(str(nodes[friend]['friend_count']) + "\n")
        friendcounts.append( int (nodes[friend]['friend_count']))
        #not all friends will have friend count available
    except KeyError:
        continue

count = len(friendcounts)
mean = stat.mean(friendcounts)
std = stat.pstdev(friendcounts)
median = stat.median(friendcounts)

print("mean: %.1f" % mean)
print("std: %.1f" % std)
print("median: %.1f" % median)

outfile.write(str(count) + "\n")
outfile.close()


