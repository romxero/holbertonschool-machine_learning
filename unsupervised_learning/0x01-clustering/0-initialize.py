#!/usr/bin/env python3
"""
K-means clustering
"""


# sk.cluster.KMeans
# something somethign 


def initialize(X, k):
    import numpy as np 
    n,d = X.shape #get the shape of the matric
    clusters = np.random.uniform(low=np.min(X, axis=0), high=np.max(X, axis=0), size=(k,d))
    return clusters  

