#!/usr/bin/env python3

import numpy as np

"""
This is to work with convolutional neural networks.
"""

def conv_forward(A_prev, W, b, activation, padding="same", stride=(1, 1)):
    m, h_prev, w_prev, c_prev = A_prev.shape
    kh, kw, c_prev, c_new = W.shape
    sh, sw = stride[0], stride[1]
    if padding == 'valid':
        ph = pw = 0
    else:

       ph = int (np.ceil(((h_prev -1 ) * sh + kh - h_prev / 2 ))
       pw = int (np.ceil(((w_prev -1 ) * sw + kw - w_prev / 2 ))

    oh = int( ((h_prev + 2 * ph - kh  ) / sh  ) + 1)
    ow = int( ((w_prev + 2 * pw - kw  ) / sw  ) + 1)

    output_dim = (m, oh, ow, c_new)

    conv = np.zeros(output_dim) #convolution return right here 


    padded_images = np.pad(A_prev, pad_width=((0,0),(ph,ph),(pw,pw),(0,0)), mode='constant')

    for i in range(oh):
      for j in range(ow):
        x = i * sh
        y = j * sw
        M = padded_images[:, x:x + kh, y:y + kw, :]
        for f in range(c_new):
        conv[:,i,j,f] = np.tensordot(M,W[:,:,:,f,axes=3]) 

   A = activation(conv + b)
   return A #make sure to return A
