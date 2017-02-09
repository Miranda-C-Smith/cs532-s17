#!/usr/bin/env python3
import urllib.request
#from urllib.parse import urlparse
import time
import json

urlFile = open("uniqueUrls_1000", 'r')
ageFile = open("CarbonDate_uniqueUrls_1000" , 'w')

CarbonDateTool = "http://cd.cs.odu.edu/cd?url="

for url in urlFile:
    url = url.strip()
    finalurl = CarbonDateTool + url

    #make 10 attempts at connecting before quiting
    try:
        req = urllib.request.Request(finalurl)
        res = urllib.request.urlopen(req)
    except urllib.error.URLError as e:
        print(e.reason)
        if e.reason == "Service Unavailable":
            time.sleep(3)
            try:
                req = urllib.request.Request(finalurl)
                res = urllib.request.urlopen(req)
            except:
                #print ("Skipping, url failed with Service Unavailable:")
                #print(url)
                ageFile.write("\n")
                continue
        if e.reason == "Gateway Time-out":
            #print ("Skipping, url failed with gateway timeout:")
            #print(url)
            ageFile.write("\n")
            continue
    
    carbon_data = res.read().decode(res.info().get_param('charset') or 'utf-8')
    json_data = json.loads(carbon_data)
    if json_data["Estimated Creation Date"] == "":
        ageFile.write("NA")
        ageFile.write("\n")
    else:
        ageFile.write(json_data["Estimated Creation Date"])
        ageFile.write("\n")
    

urlFile.close()
ageFile.close()
