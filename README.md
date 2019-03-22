# K_means

This repo houses my first KMeans algorithm that I had made during my time in college during my undergrad studies.  The repo uses numpy and Pandas other than that it is built from the ground up.

The KMeans algorithm is a clustering algorithm that finds similar data point and groups them together.  The algorithm takes K
which is an arbitary number that corresponseds to the number of clusters that the user wants. The way this works is by putting a point in the middle of each cluster known as a centroid.  Afterwards determining which point is closest to the centroid and then adding that point to the cluster that the centroid belongs too.  The process continues until the centroids do not move within a cluster.  Now the centroids generally are floats so an epsilon value, AKA threshold, is used to say "if the distance the centroid has moved less than than the specified epsilon stop running the algorithm."

An example usage of this algorithm is when you want to find similar classes.  E.g, If I have boats and I have features of those boats yet they are of multiple different classes
I can use the KMeans algorithm to find boats with similar features and group them together.  This creates groupings of boats and if some
boats that happen to be dangerous fall in to a specific cluster that has known dangerous boats then we can blacklist some of those boats
and add security measures for those particular boats.
