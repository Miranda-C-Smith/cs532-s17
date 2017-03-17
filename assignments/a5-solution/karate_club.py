#!/usr/bin/env python
"""
Zachary's Karate Club graph

Data file from:
http://vlado.fmf.uni-lj.si/pub/networks/data/Ucinet/UciData.htm

Reference:
Zachary W. (1977).
An information flow model for conflict and fission in small groups.
Journal of Anthropological Research, 33, 452-473.
"""
import igraph 

groups = open("karateGroups.txt", "w")

g = igraph.Graph.Read_GML("karate.gml")

#labels done in this weird way so that they wouldn't be floats
g.vs["label"] = g.vs["id"]
numbers = list(map(int, g.vs["label"]))
g.vs["label"] = list(map(str, numbers))
#igraph.plot(g)
clusters = g.community_leading_eigenvector(clusters=2)

#dendrogram = g.community_edge_betweenness(clusters=2)
#clusters = dendrogram.as_clustering()

igraph.plot(clusters, "karateClubModeledGraph.png")

membership = clusters.membership

groups.write("ID Group\n")
for name , membership in zip(g.vs["label"], membership):
    groups.write(name + " " + str(membership) + "\n")

groups.close()
