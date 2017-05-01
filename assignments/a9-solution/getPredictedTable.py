import textwrap
import feedparser
import docclass
import re
import math

rss_files = ["rss_1.txt" ,"rss_2.txt" ,"rss_3.txt" ,"rss_4.txt"]

file = open("Blog_Links_Categories.txt", 'r')
categories = file.readlines()
file.close()

actualData = {}
count = 0
for rss in rss_files:
        feed = feedparser.parse(rss)
        for item in feed["items"]:
      
            line = item["title"].strip()
            actualData[line] = categories[count]
            count = count +1
            
   
predictedData= {}
   
cl=docclass.fisherclassifier(docclass.getwords)
cl.setdb('mln.db')

#TRAINING
print("TRAINING")
count = 0
for rss in rss_files:
        feed = feedparser.parse(rss)
        for item in feed["items"]:
            #train with the first 50 or 90
            line = item["title"].strip()
            c1.train(line, actualData[line])
            if count == 89:
                break
            count = count +1
                



#TESTING on the next 50 or 10

print("TESTING")
count = 0
for rss in rss_files:
    feed = feedparser.parse(rss)
    for item in feed["items"]:
        if count > 89:
            #predict the next 50 or 10
            line = item["title"].strip()
            predictedData[line] = cl.classify(line)
        count = count +1


with open("PredictedvsTruthTable90_10.txt" , 'w') as out:
    out.write ("{:<100} {:<20} {:<20}\n".format('ARTICLE','CLASSIFICATION','PRED CLASSIFICATION'))
    
    for a ,c  in predictedData.items():
        out.write ("{:<100} {:<20} {:<20}\n".format(a,actualData[a].strip(),c.strip()))


    

