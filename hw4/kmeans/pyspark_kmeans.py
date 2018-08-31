import os
import sys
from pyspark import SparkContext
import numpy as np
from numpy import linalg as LA

def pyspark_kmeans(datafile, initial_centroids):
    """
    find centroids for data points with 10 clusters using 100 iterations
    :param datafile: n-dimension data points
    :param initial_centroids: initial centroids for
    :return: 10 centroids
    """
    data = sc.textFile(datafile).map(lambda line: np.array([float(x) for x in line.split(' ')])).cache()
    centroid = sc.textFile(initial_centroids).map(lambda line: np.array([float(x) for x in line.split(' ')])).collect()
    
    for i in range(100):
        cluster = data.map(lambda l: (np.argmin([LA.norm(np.array(l) - np.array(c)) for c in centroid]), l))
        cluster_sum = cluster.map(lambda v: (v[0], (v[1], 1))).reduceByKey(lambda a,b: (np.array(a[0]) + np.array(b[0]), a[1]+b[1]))
        new_centroid = cluster_sum.map(lambda v: (v[0], np.array(v[1][0])/v[1][1])).sortByKey(ascending = True).map(lambda l: l[1]).collect()    
        centroid = new_centroid
    
    return centroid

if __name__ == '__main__':
    sc = SparkContext(appName = "kmeans")
    datafile = sys.argv[1]
    initial_centroids = sys.argv[2]
    res = pyspark_kmeans(datafile, initial_centroids)
    
    f = open('result.txt', 'w')

    for centroid in res:
        for element in centroid: 
            f.write(str(element) + " ")
        f.write("\n")
    f.close()
