import feedparser


rss_files = ["rss_1.txt" ,"rss_2.txt" ,"rss_3.txt" ,"rss_4.txt"]

file = open("Blog_Links.txt", 'w')

entries= {}
count = 0;
for rss in rss_files:
    feed = feedparser.parse(rss)
    
    for item in feed["items"]:
        file.write(item["link"])
        file.write("\n")
        count = count + 1

file.close()
