#!/usr/bin/env python3

#running another test 
import numpy as np


class Neuron:
    def __init__(self, nx):
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if (nx) < 1:
            raise ValueError("nx must be a positive integer")
        try:
            self.nx = nx
            self.__W = np.random.randn(1, nx)
            self.__b = 0
            self.__A = 0
        except:
            print("An exception occurred")
    @property
    def W(self):
        return self.__W

    @property
    def b(self):
        return self.__b

    @property
    def A(self):
        return self.__A
    # make sure to have thre variables here
    def forward_prop(self, X):
        if type(X) is not np.ndarray:
            raise TypeError("Value is supposed to be an numpy dimmensional array")
        preAct = np.matmul(self.__W, X) + self.__b #preactivation of the single neuron
        self.__A = 1/(1 + np.exp(-preAct))
        return self.__A
    def cost(self, Y, A):
        #this is also called the loss function 
        if type(A) is not np.ndarray:
            raise TypeError("Value X is supposed to be an numpy dimmensional array")
        if type(Y) is not np.ndarray:
            raise TypeError("Value Y is supposed to be an numpy dimmensional array")
        internalVariable = Y * np.log(A) +  np.log(1.0000001 - A) #calculation should be ok 
        internalVariable = np.sum(internalVariable)
        internalVariable = -internalVariable/A.shape[1]
        return internalVariable #just return a value right now and fill in the variable later 
