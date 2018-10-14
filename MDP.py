# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 14:27:49 2018

@author: Victor Zuanazzi
"""

import random
import matplotlib.pyplot as plt
import numpy as np

class MDP():
    def __init__(self, height = 5, base = 5):
        self.h = height
        self.b = base
        self.grid = np.zeros((self.h, self.b))
        self.state = 0, 0
        self.state_value = np.zeros((self.h, self.b))
        self.n_actions = 4
        self.reward = np.zeros((self.h, self.b, self.n_actions))
        self.init_action_values()
        self.transition_probability = np.ones((self.h, self.b, self.n_actions))
        self.init_policy()
    
    def init_action_values(self,):
        self.action_value = np.zeros((self.h, self.b, self.n_actions))
        for i in range(self.h):
            for j in range(self.b):
                for k in  range(self.n_actions):
                    self.action_value[i,j,k] = k
                    #0 means north
                    #1 means right
                    #2 means south
                    #3 means left

    def init_policy(self):
        self.policy = np.ones((self.h, self.b, self.n_actions))
        for i in range(self.h):
            for j in range(self.b):
                for k in  range(self.n_actions):
                    self.policy[i,j,k] /= 4 
                    #all actions are equally probable.
    def print_MDP(self):
        print(self.grid)
        print(self.state_value)
        print(self.state_value[self.state])
        print(self.action_value)
        print(self.policy)
        print(self.action_value[self.state])

if __name__ == '__main__':
    mdp = MDP()
    mdp.print_MDP()
    