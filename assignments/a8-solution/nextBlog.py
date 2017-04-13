import feedparser
import urllib.request
import os
#from urllib.parse import urlparse
nextBlogBase = "https://www.blogger.com/next-blog?navBar=true&blogID="
url ='http://f-measure.blogspot.com'
url2 = 'http://ws-dl.blogspot.com'
#broken ='http://lacan-can.blogspot.com'

atomEnd = '/feeds/posts/default'

linkfile = open("100blogs.txt", 'w')

linkfile.write(url + atomEnd + "\n")
linkfile.write(url2 + atomEnd + "\n")

count = 2
while (count < 100):
        url = url + atomEnd
        print(url)
        try:
            d = feedparser.parse(url)
            ID = d.feed.id.split("-")[1]
            nextBlog = nextBlogBase + ID
            req = urllib.request.Request(nextBlog, method="HEAD")
            res = urllib.request.urlopen(req)
        except:
            url = url2
            continue
        
        url = os.path.dirname(res.geturl())
        linkfile.write(url + atomEnd + "\n")
        count = count + 1
linkfile.close()
