import feedparser


diving_rss="https://sharkdivers.blogspot.com/feeds/posts/default"


count = 0;
while count < 100:
    feed = feedparser.parse(diving_rss)
    print(diving_rss)
    
    for item in feed["items"]:
        count = count + 1
    
    
    fed = feed["feed"]
    for link in fed["links"]:
        if link["rel"] == "next":
            diving_rss = link["href"]

