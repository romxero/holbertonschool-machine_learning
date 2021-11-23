#!/usr/bin/env python3
"""
Actually using k-means clustering
"""

def initialize(X, k):
    import numpy as np 
    n,d = X.shape #get the shape of the matrice
    clusters = np.random.uniform(low=np.min(X, axis=0), high=np.max(X, axis=0), size=(k,d))
    return clusters  



def kmeans(X, k, iterations=1000):
    n,d = X.shape #get the shape of the matrice

    return 0
