import textwrap
import feedparser

rss_files = ["rss_1.txt" ,"rss_2.txt" ,"rss_3.txt" ,"rss_4.txt"]

file = open("Blog_Links_Categories.txt", 'r')
categories = file.readlines()
file.close()

count = 0

with open("GroundTruthTable.txt" , 'w') as out:
    out.write ("{:<100} {:<20}\n".format('ARTICLE','CLASSIFICATION'))
    for rss in rss_files:
        feed = feedparser.parse(rss)
    
        for item in feed["items"]:
            out.write ("{:<100} {:<20}\n".format(item["title"].strip(),categories[count].strip()))
            count = count + 1



    

