#!/usr/bin/env python3

import numpy as np 


class Neuron:
    def __init__(self,nx):
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if (nx) < 1:
            raise ValueError("nx must be a positive integer")
        try:
            self.W = np.random.randn(1, nx)
            self.b = 0
            self.A = 0
            self.nx = nx
        except:
            print("An exception occurred")
        self.data = []
    #make sure to have thre variables here 


