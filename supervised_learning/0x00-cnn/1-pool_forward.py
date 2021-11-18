import numpy as np

def pool_forward(A_prev, kernel_shape, stride=(1, 1), mode='max'):
    m, h_prev, w_prev, c_prev = A_prev.shape
    kh, kw, = kernel_shape[0], kernel_shape[1]
    sh, sw = stride[0], stride[1]
    ph = pw = 0

    oh = int( ((h_prev - kh  ) / sh  ) + 1)
    ow = int( ((w_prev  - kw  ) / sw  ) + 1)

    output_dim = (m, oh, ow, c_prev)

    conv = np.zeros(output_dim) #convolution return right here 


    padded_images = np.pad(A_prev, pad_width=((0,0),(ph,ph),(pw,pw),(0,0)), mode='constant')

    for i in range(oh):
      for j in range(ow):
        x = i * sh
        y = j * sw
        M = A_prev[:, x:x + kh, y:y + kw, :]
        if mode == 'max':
            conv[:,i,j,:] = np.max(M,axis=(1,2)) 
        else:
            conv[:,i,j,:] = np.max(M,axis=(1,2)) 

    return conv #make sure to return A
