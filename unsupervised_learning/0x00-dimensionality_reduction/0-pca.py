#!/usr/bin/env python3 
"""
PCA analysis for dimensionality reduction 
"""

import numpy as np

def pca(X, var=0.95):
    u,s, vh  = np.linalg.svd(X) #singulaur value decomposition returns u, s and vh
    W = vh.T #W = vh.T
    sCummulativeSum = np.cumsum(s) #sum up the singular values 
    totalVariance = np.cumsum(s)/np.sum(s) # I know we need to get the variance somewhere here 
    idx = np.argmax(totalVariance >= var) + 1 
    return W[:,:idx]
