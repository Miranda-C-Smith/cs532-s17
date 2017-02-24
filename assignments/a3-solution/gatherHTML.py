#!/usr/bin/python3
import subprocess

curl = r"curl"
counter = 1
with open('uniqueUrls_1000' , 'r') as infile:
    for url in infile:
        try:
            filename = 'html/' + str(counter)
            print(filename)
            url = url.strip()
            outfile = open(filename, 'w')
            subprocess.call([curl, url], stdout=outfile)
            counter = counter + 1
            outfile.close()
        except:
            continue
