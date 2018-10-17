# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 12:11:38 2018

@author: Victor Zuanazzi
"""
import numpy as np

#MDP has states
#Each state has actions
#actions take the agent to new states

state = [1,1,0] #0 means terminal state.
action = [[1, -1]]*len(state)
policy = []
reward = []
transition_probability =[]

for i in range(len(state)):
    k = len(action[i])
    policy_probabilities = []
    r= []
    t_p = []
    for j in range(k):
        policy_probabilities.append(1/k)
        r.append(-1)
        t_p.append(1) #
    policy.append(policy_probabilities)
    reward.append(r)
    transition_probability.append(t_p)
    
discount_factor = 1 #called gamma in the Bellman eq.

state_value = np.zeros(len(state))
action_value = np.zeros((len(state),len(action[0])))

agent = [0, 0] #state, reward

time = 0
while state[agent[0]] !=0:
    print(agent)
    chose_action = 0
    for p_i in [0,1]:
        temp = policy[agent[0]][p_i]*np.random.uniform()
        print('temp=', temp)
        if temp > chose_action:
            chose_action = temp
            action_i = p_i
    print('action_i: ', action_i)
        
    agent[0] += action[agent[0]][action_i]
    if agent[0] < 0 :
        agent[0]=0
    agent[1] += -1
print(agent)
    
