import numpredict
import clusters

blognames,words,data=clusters.readfile('blogdata1.txt')


#k={1,2,5,10,20}
print (blognames[0]+ " k =1")
numpredict.knnestimate(blognames[1:], data[1:],data[0], k=1)
print (blognames[0]+ " k =2")
numpredict.knnestimate(blognames[1:], data[1:],data[0], k=2)
print (blognames[0]+ " k =5")
numpredict.knnestimate(blognames[1:], data[1:],data[0], k=5)
print (blognames[0]+ " k =10")
numpredict.knnestimate(blognames[1:], data[1:],data[0], k=10)
print (blognames[0]+ " k =20")
numpredict.knnestimate(blognames[1:], data[1:],data[0], k=20)

blogname = blognames[77]
blogdata = data[77]
blognames.pop(77)
data.pop(77)
print (blogname + " k =1")
numpredict.knnestimate(blognames, data,blogdata, k=1)
print (blogname+ " k =2")
numpredict.knnestimate(blognames, data,blogdata, k=2)
print (blogname+ " k =5")
numpredict.knnestimate(blognames, data,blogdata, k=5)
print (blogname+ " k =10")
numpredict.knnestimate(blognames, data,blogdata, k=10)
print (blogname+ " k =20")
numpredict.knnestimate(blognames, data,blogdata, k=20)
