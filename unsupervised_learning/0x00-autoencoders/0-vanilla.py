#!/usr/bin/env python3 

#testing the autoencoders right here 
import tensorflow.keras as keras


def autoencoder(input_dims, hidden_layers, latent_dims):
    #setting up the intiial tensors right here 
    inputEncoder = keras.Input(shape=(input_dims,))
    inputDecoder = keras.Input(shape=(latent_dims,))
    
    #encoded model below
    encodedModelObj = keras.layers.Dense(hidden_layers[0],activation='relu',)(inputEncoder) #I think this is where its supposed to work properly 
    for enc in range(1, len(hidden_layers)):
        encodedModelObj = keras.layers.Dense(hidden_layers[enc],activation='relu',)(encodedModelObj) #take the model and modify it recursively and multiply by encodedState 

    #latent layer stuff 
    latentLayer = keras.layers.Dense(latent_dims,activation='relu')(encodedModelObj) #make sure to use the encoded state right here 
    encoderState = keras.Model(inputs=inputEncoder, outputs=latentLayer) #encoder  state  make sure to grab the other data for this.


    #decoded model goes below 
    decodedModelObj = keras.layers.Dense(hidden_layers[-1],activation='relu',)(inputDecoder) #I think this is where its supposed to work properly 

    #for this thing the hidden layer length must be minus 2 and then it is a tuple with other values (i.e. '-1').. 

    for dec in range(1, len(hidden_layers) - 2, -1  ):
        decodedModelObj = keras.layers.Dense(hidden_layers[dec],activation='relu',)(decodedModelObj) #take the model and modify it recursively and multiply by encodedState 



    last = keras.layers.Dense(input_dims,activation='sigmoid')(decodedModelObj)
    
    decoderState = keras.Model(inputs=inputDecoder, outputs=last) #encoder  state  make sure to grab the other data for this.

    #right here we are getting ready to ouptut the models 
    encoder_output = encoderState(inputEncoder)
    decoder_output = decoderState(encoder_output)
    auto = keras.Model(inputs=inputEncoder, outputs=decoder_output)

    auto.compile(optimizer='adam', loss='binary_crossentropy')

    #decoderState = 0#right here is TEMPORARY
    return encoderState, decoderState, auto
