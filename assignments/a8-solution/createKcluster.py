import clusters
#Question 3 cluster with K means
outfile = open('KClusters.txt', 'w')

blognames,words,data=clusters.readfile('blogdata1.txt')
clust = clusters.kcluster(data, k=5)
outfile.write("K = 5\n" )
for i in range(5):
    outfile.write("\nNode " + str(i) + "\n")
    for r in clust[i]:
            outfile.write(blognames[r] + ", ")


clust2 = clusters.kcluster(data, k=10)
outfile.write("\n\nK = 10\n" )
for i in range(10):
    outfile.write("\nNode " + str(i) + "\n")
    for r in clust2[i]:
            outfile.write(blognames[r] + ", ")


clust3 = clusters.kcluster(data, k=20)
outfile.write("\n\nK = 20\n" )
for i in range(20):
    outfile.write("\nNode " + str(i) + "\n")
    for r in clust3[i]:
            outfile.write(blognames[r] + ", ")
            
outfile.close()
