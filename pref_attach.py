#!/usr/bin/python
# pref-attach.py
# Blake Stacey (bstaceyAT.alum.removethis.mit.andthis.edu)
import math, random
import scipy, pylab     # only if you want graphics


dNetwork = {}       # dictionary of lists
iNodes = 1000       # total number of nodes
iLinks = 0

for i in range(iNodes):
	dNetwork[i] = []      # initialize node of key i with empty list
	for node in dNetwork.values():
		fThresh = 1.0 / (iLinks + i + 1) * (len(node) + 1)
		if(random.random() <= fThresh):
			node.append(i)
			iLinks += 1

# calculate the degree distribution
lDegrees = [len(node) for node in dNetwork.values()]
print (lDegrees)

# and draw a histogram
pylab.hist(lDegrees,50)
pylab.xlabel("Node Degree")
pylab.ylabel("Number of Nodes")
pylab.title("Preferential Attachment")
pylab.show()