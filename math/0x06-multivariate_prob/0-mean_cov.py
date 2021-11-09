#!/usr/bin/env python3

#test out multinomial probability density functionm 

#camel case notation


def mean_cov(matrix): 
    if matrix is 0:
        return -1 #short circuit
    import numpy as np
    import math as mat
    npInternalArray = np.array(matrix) #grab the numpy array
    internalMean = np.mean(npInternalArray)


    C = [[]] #make a null matrix 

    for i in range(6):
        for j in range(6):
    #manual calculation of covariant possibly can't compute if its not a square matrix
            C[i][j] = npInternalArray[i][j]/(mat.sqrt(npInternalArray[i][i] * npInternalArray[j][j])) #test 
    return internalMean, C #aleph null


    
