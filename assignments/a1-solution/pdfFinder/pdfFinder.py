#!/usr/bin/env python3
#Webpage PDF Finder
#cs432 Web Science Assignment 1

import sys
import urllib.request
from bs4 import BeautifulSoup, SoupStrainer

#Read in command line argument
args = sys.argv
if len(args) != 2:
    print("Usage: pdfFinder.py url")
    exit()
url = args[1]

#get page
#print(url)

req = urllib.request.Request(url)

try: 
	res = urllib.request.urlopen(req)
except urllib.error.URLError as e:
	print(e.reason)    
	exit()

#for all links in the html
for link in BeautifulSoup(res, parse_only=SoupStrainer('a', href=True)):
	#if link.has_attr('href'):
	try:		
		linkres = urllib.request.Request(link['href'], method='HEAD')
		with urllib.request.urlopen(linkres) as linkresp:
			info = linkresp.info()
			#check if pdf
			if "pdf" in info.get_content_type():
				#print URIs and size in byes
				print("First URI: {}".format(link['href']))
				print("Last URI: {}".format(linkresp.geturl()))
				print("Bytes: {}".format(info.get('Content-Length')))
	except:
		#here incase it gets a weird link that this isn't compatible with
		continue
res.close()
