#!/usr/bin/env python3
#get the momentoes for all links in file

import urllib.request

urlFile = open('uniqueUrls_1000', 'r')
timeFile = open('timeMapCount_uniqueUrls_1000', 'w')

mementoAgg = 'http://memgator.cs.odu.edu/timemap/link/'

for line in urlFile:
    #line = 'http://www.cs.odu.edu/'
    url = mementoAgg + line
    try:
        req = urllib.request.Request(url)
        res = urllib.request.urlopen(req)
        #string = res.read().decode(res.info().get_param('charset') or 'utf-8')
        timemap = res.read().decode(res.info().get_param('charset') or 'utf-8')
        print(timemap.count("rel=\"memento\""))
    except urllib.error.URLError as e:
        if e.reason == 'Not Found':
            timeFile.write("0\n")
    
urlFile.close()
timeFile.close()
