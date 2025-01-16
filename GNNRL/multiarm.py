import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.distributions import Normal
from env import slice_env
import matplotlib.pyplot as plt
import numpy as np
import time
import pandas as pd
import math

def main():

    N = 100
    d = 90
    num = 80
    ads_selected = []
    numbers_of_selections = [0] * num
    sums_of_reward = [0] * num
    total_reward = 0
    
    RAN_env = slice_env()
    RAN_env.initlize()
    score = 0.0
    # train
    RAN_env.init_file()
    
    last_reward = 25


    # 0-80 is 50-90 and then 49-10

    for n in range(200):
        adbb = 50
        ad = 0
        max_upper_bound = 0
        for i in range(0, num):
            if (numbers_of_selections[i] > 0):
                average_reward = sums_of_reward[i] / numbers_of_selections[i]
                delta_i = math.sqrt(2 * math.log(n+1) / numbers_of_selections[i])
                upper_bound = average_reward + delta_i
            else:
                upper_bound = 1e1000
            
            if upper_bound > max_upper_bound and last_reward > 20 and i<40:
                max_upper_bound = upper_bound
                ad = i
                adbb = i+50

            if upper_bound > max_upper_bound and last_reward > 20 and i>=40:
                max_upper_bound = upper_bound
                adbb = 90-i
                ad = i

        ads_selected.append(adbb)
        numbers_of_selections[ad] += 1
            
            
        b = 100 - adbb
        RAN_env.send_action(adbb, b, 0)#
        print(adbb, b)
        time.sleep(0.1)#0.2,
        s_prime123 = RAN_env.get_all_state()
        reward, done = RAN_env.caculate_reward(ad)
        reward = reward*10
        last_reward = reward
        print(reward)
        sums_of_reward[ad] += reward
        total_reward += reward
            
           
    print(pd.Series(ads_selected).head(200).value_counts(normalize=True))


if __name__ == '__main__':
    main()