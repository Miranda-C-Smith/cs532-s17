import clusters
import sys


blognames,words,data=clusters.readfile('blogdata1.txt')
#Question 2 cluster
clust=clusters.hcluster(data)
clusters.drawdendrogram(clust,blognames,jpeg='blogclust.jpg')

orig_stdout = sys.stdout
f = open('blogclust.txt', 'w')
sys.stdout = f

clusters.printclust(clust, labels=blognames)

sys.stdout = orig_stdout
f.close()
