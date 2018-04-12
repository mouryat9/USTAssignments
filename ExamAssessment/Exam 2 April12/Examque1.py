# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 15:14:32 2018

@author: user
"""

import pandas as pd
import numpy as np

data = pd.read_csv("Camera.csv", header=0)

print(data.shape)
print(list(data.columns))

print(data.dtypes)

print(data.iloc[0:25])