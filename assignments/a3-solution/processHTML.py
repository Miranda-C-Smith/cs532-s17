#http://stackoverflow.com/questions/1936466/beautifulsoup-grab-visible-webpage-text
import urllib
import re
from bs4 import BeautifulSoup

for i in range(1000):

    filename = "rawhtml\\" + str(i+1)
    print(filename)
    outfilename = "processedhtml\\" + str(i+1)
    infile = open(filename , 'r', errors='ignore', encoding='utf8')
    outfile = open(outfilename, 'w', encoding="utf8")
    
    html = infile.read()
    #print(html)
    soup = BeautifulSoup(html, 'html.parser')
    [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
    visible_text = soup.getText()
    
    outfile.write(visible_text)
    
    infile.close()
    outfile.close()

        
    
