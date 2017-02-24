#!usr/bin/env python3
import subprocess

grep = r"grep"
infile = open("trumpFiles.txt", 'r')
TFdict = {}
totalDocs = subprocess.call(["ls", "processedhtml"])
totalDocsCount = subprocess.call(["wc", "-w", totalDocs])
print("Total Docs: " +str(totalDocsCount))
DocsWTerm = 12
for line in infile:
    unnormalizedTF = subprocess.call([grep, "-c", "[T|t]rump", "processedhtml/" +str(line)])
    print(unnormalizedTF)
    WC = subprocess.call(["wc", "-w", line])
    TFdict[line] = unnormalizedTF / WC
    print(TFdict[line])
    
