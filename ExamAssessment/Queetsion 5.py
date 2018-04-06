# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 16:09:01 2018

@author: user
"""

import numpy as np
from scripy import stats

x=[11.95,11.91,1186,11.94,12.00,11.93,12.00,11.94,12.10,11.95,11.99,11.94,11.89,12.01,11.99,11.94]        
temp=stats.itemfreq(x)
print("Frequency Distribution of this table is: \n",temp)
mean=np.mean(x)
median=np.median(x)
mode=stats.mode(x)
print("mean,median,mode are",mean(x),median(x),mode(x))   
                    