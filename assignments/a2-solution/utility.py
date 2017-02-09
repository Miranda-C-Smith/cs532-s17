import json

CarbonDateTool = "http://cd.cs.odu.edu/cd?url="


with open("CarbonDate_uniqueUrls_1000" , 'r') as ageFile, open("2CarbonDate_uniqueUrls_1000" , 'rw') as ageFile2, open("uniqueUrls_1000", 'r') as urlFile:
    line = ageFile.read().splitlines()
    url= urlFile.read().splitlines()
    writeF= ageFile2.read().splitlines()
    
    if line == "":
        url = url.strip()
        finalurl = CarbonDateTool + url
        try:
            req = urllib.request.Request(finalurl)
            res = urllib.request.urlopen(req)
        except urllib.error.URLError as e:
            print(e.reason)
            ageFile2.write("\n")
            continue
        carbon_data = res.read().decode(res.info().get_param('charset') or 'utf-8')
        json_data = json.loads(carbon_data)
        if json_data["Estimated Creation Date"] == "":
            ageFile2.write("NA")
            ageFile2.write("\n")
        else:
            ageFile2.write(json_data["Estimated Creation Date"])
            ageFile2.write("\n")
    else:
        continue
    

        

