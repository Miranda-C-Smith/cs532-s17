#!/usr/bin/env python3
#get the momentoes for all links in file
import urllib.request

urlFile = open('uniqueUrls_1000', 'r')
timeFile = open('timeMapCount_uniqueUrls_1000', 'w')

mementoAgg = 'http://memgator.cs.odu.edu/timemap/link/'

for dirtyline in urlFile:
    line = dirtyline.strip()
    #line = 'http://www.cs.odu.edu/'
    url = mementoAgg + line
    try:
        req = urllib.request.Request(url)
        res = urllib.request.urlopen(req)
        timemap = res.read().decode(res.info().get_param('charset') or 'utf-8')
        timeFile.write(str(timemap.count("rel=\"memento\""))+ "\n")
    except urllib.error.URLError as e:
        if e.reason == 'Not Found':
            timeFile.write("0\n")
    
urlFile.close()
timeFile.close()
