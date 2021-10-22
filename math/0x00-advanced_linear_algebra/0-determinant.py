#!/usr/bin/env python3

#use the same shebang that students are using.



def determinant(matrix):
  import numpy as np
  innerMatrice = np.array(matrix)
  determinantBuffer = np.linalg.det(innerMatrice)
  return determinantBuffer #this is wrong
