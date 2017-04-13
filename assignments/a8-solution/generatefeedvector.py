#!/usr/bin/python
# -*- coding: utf-8 -*-
import feedparser
import re
import math

def getwordcounts(url):
    '''
    Returns title and dictionary of word counts for an RSS feed
    '''
    # Parse the feed
    d = feedparser.parse(url)
    wc = {}

    # Loop over all the entries
    for e in d.entries:
        if 'summary' in e:
            summary = e.summary

        else:
            summary = e.description

        # Extract a list of words
        words = getwords(e.title + ' ' + summary)
        for word in words:
            wc.setdefault(word, 0)
            wc[word] += 1

    return (d.feed.title, wc)


def getwords(html):
    # Remove all the HTML tags
    txt = re.compile(r'<[^>]+>').sub('', html)

    # Split words by all non-alpha characters
    words = re.compile(r'[^A-Z^a-z]+').split(txt)

    # Convert to lowercase
    return [word.lower() for word in words if word != '']


apcount = {}
wordcounts = {}
feedlist = [line for line in open('100blogs.txt')]

for feedurl in feedlist:
    try:
        (title, wc) = getwordcounts(feedurl)
        wordcounts[title] = wc
        for (word, count) in wc.items():
            apcount.setdefault(word, 0)
            if count > 1:
                apcount[word] += 1
    except:
        print ('Failed to parse feed ' + feedurl)

wordlist = []
longwordlist = []
idflist = []
for (w, bc) in apcount.items():
    frac = float(bc) / len(feedlist)
    if frac > 0.15 and frac < 0.75:
        longwordlist.append(w)
        idflist.append(frac)


for item in sorted( zip(idflist, longwordlist), reverse=True)[:1000]:
    wordlist.append(item[1])


out = open('blogdata1.txt', 'w')
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
