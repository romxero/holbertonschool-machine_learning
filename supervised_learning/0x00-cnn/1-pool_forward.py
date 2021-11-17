def pool_forward(A_prev, kernel_shape, stride=(1, 1), mode='max'):
    m, h_prev, w_prev, c_prev = A_prev.shape
    kh, kw, = kernel_shape[0], kernel_shape[1]
    sh, sw = stride[0], stride[1]
    ph = pw = 0

#    ph = int (np.ceil(((h_prev -1 ) * sh + kh - h_prev / 2 )))
#    pw = int (np.ceil(((w_prev -1 ) * sw + kw - w_prev / 2 )))

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
