#!/usr/bin/env python3

#running another test

import numpy as np


def normalization_constants(X):
    m = X.mean(axis=0)
    s = X.std(axis=0)
    return m,s


def normalize(X, m, s):
    return X - m / s 



def shuffle_data(X, Y):
    np.random.seed(0)
    permutation = np.random.permutation(X.shape[0])
    return (X[permutation,:]), (Y[permutation,:])


