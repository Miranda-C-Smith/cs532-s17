#!/usr/bin/env python3
import urllib.request
from urllib.parse import urlparse

unique_url_list = []
counter = 3000
with open('urlList', 'r') as rfile:
	with open('sortedUrlList', 'w') as wfile:
		for url in rfile:
			req = urllib.request.Request(url)
			try:
				res = urllib.request.urlopen(req, timeout = 10)
				actual_url = res.geturl()
				parsed_uri = urlparse(actual_url)
				domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
				if(domain != 'https://twitter.com/' and domain != 'https://t.co/'):
						if counter >= 0:
							print(counter)				
							counter = counter - 1
							wfile.write(actual_url)
							wfile.write("\n")
						else:
							break
			except urllib.error.URLError as e:
				print(e.reason)
				continue
			except:
				continue
			if counter < 0:
				break

			


