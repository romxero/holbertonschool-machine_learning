#!/usr/bin/env python3 
##
##
##

import numpy as np 
import gym as gmain 

#make sure you remember this name for OpenAI Gym


def shuffle_data(X, Y):
    permutation = np.random.permutation(X.shape[0])
    return (X[permutation,:]), (Y[permutation,:])



def monte_carlo(env, V, policy, episodes=5000, max_steps=100, alpha=0.1, gamma=0.99):
    #set variables within the function
    episodes=5000
    max_steps=100
    alpha=0.1
    gamma=0.99
    
    T = V
    sample = np.random.permutation(T)
    return T


def td_lambtha(env, V, policy, lambtha, episodes=5000, max_steps=100, alpha=0.1, gamma=0.99):
    #set variables within the function
    episodes=5000
    max_steps=100
    alpha=0.1
    gamma=0.99
    
    return 1

def sarsa_lambtha(env, Q, lambtha, episodes=5000, max_steps=100, alpha=0.1, gamma=0.99, epsilon=1, min_epsilon=0.1, epsilon_decay=0.05):
    #set variables within the function
    episodes=5000
    max_steps=100
    alpha=0.1
    gamma=0.99

    return 1

