#!/usr/bin/python
# -*- coding: utf-8 -*-
import feedparser
import re
import math

def getwordcounts(title):
    '''
    Returns title and dictionary of word counts for an RSS feed
    '''
    wc = {}

    # Extract a list of words
    words = getwords(title)
    for word in words:
        wc.setdefault(word.strip(), 0)
        wc[word] += 1

    return (title, wc)


def getwords(html):
    # Remove all the HTML tags
    txt = re.compile(r'<[^>]+>').sub('', html)

    # Split words by all non-alpha characters
    words = re.compile(r'[^A-Z^a-z]+').split(txt)

    # Convert to lowercase
    return [word.lower() for word in words if word != '']


apcount = {}
wordcounts = {}

rss_files = ["rss_1.txt" ,"rss_2.txt" ,"rss_3.txt" ,"rss_4.txt"]

for rss_file in rss_files:
    feed = feedparser.parse(rss_file)
    for item in feed["items"]:     
        (title, wc) = getwordcounts(item["title"])
        wordcounts[title] = wc
        for (word, count) in wc.items():
            apcount.setdefault(word, 0)
            if count > 1:
                apcount[word] += 1

wordlist = []
longwordlist = []
idflist = []
for (w, bc) in apcount.items():
    frac = float(bc) / 100
    if frac > 0.15 and frac < 0.75:
        longwordlist.append(w)
        idflist.append(frac)


for item in sorted( zip(idflist, longwordlist), reverse=True)[:1000]:
    wordlist.append(item[1])


out = open('RSSdata.txt', 'w')
out.write('Blog')
for word in wordlist:
    out.write('\t' + word)
out.write('\n')
for (blog, wc) in wordcounts.items():
    #print (blog)
    try:
        out.write(blog)
        for word in wordlist:
            if word in wc:
                out.write('\t%d' % wc[word])
            else:
                out.write('\t0')
        out.write('\n')
    except:
        #cant encode
        print ("Error- cannot write blog " + blog ) 
out.close()
