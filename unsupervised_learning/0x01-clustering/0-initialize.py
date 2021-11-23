#!/usr/bin/env python3
"""
K-means clustering
"""

import numpy as np


# sk.cluster.KMeans
# something somethign 


def initialize(X, k):
    n,d = X.shape #get the shape of the matric
    clusters = np.random.uniform(low=np.min(X, axis=0), high=np.max(X, axis=0), size=(k,d))
    return clusters  

