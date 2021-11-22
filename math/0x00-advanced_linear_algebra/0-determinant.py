#!/usr/bin/env python3
import numpy as np
#use the same shebang that students are using.

def determinant(matrix):
  if matrix:
    innerMatrice = np.array(matrix)
    if innerMatrice.size == 0:
      return 1
    determinantBuffer = np.linalg.det(innerMatrice)
    return (determinantBuffer) #this is wrong
  return 1

