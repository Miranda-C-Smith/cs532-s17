import os

def getSize(filename):
    return os.path.getsize(filename)

out = open("RawFileSizes.txt" ,'w')
out2 = open("ProcessedFileSizes.txt" ,'w')

out.write("Old\tNew\n")
for i in range(1,1001):
    new = getSize("rawhtml\\" + str(i))
    old = getSize("..\\a3-solution\\rawhtml\\"+ str(i))
    out.write(str(old) + "\t" +str(new) +"\n")
    
    new2 = getSize("processedhtml\\" + str(i))
    old2 = getSize("..\\a3-solution\\processedhtml\\"+ str(i))
    out2.write(str(old2) + "\t" +str(new2) +"\n")


out.close()
out2.close()
