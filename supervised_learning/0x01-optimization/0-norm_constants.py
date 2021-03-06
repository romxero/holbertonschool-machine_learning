#!/usr/bin/env python3

#running another test 
import numpy as np
def normalization_constants(X):
    #T = np.ndarray(X)
#    X - X.mean #/ X.shape[1] - 1 
    m = X.mean(axis=0)
    s = X.std(axis=0)
    return m,s


def normalize(X, m, s):
    return X - m / (s - 0) + .001



def shuffle_data(X, Y):
    np.random.seed(0)
    permutation = np.random.permutation(X.shape[0])
    return (X[permutation,:]), (Y[permutation,:])



