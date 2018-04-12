# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 13:54:30 2018

@author: user
"""

import pandas as pd
import numpy as np

data  = {'name': ['Jack','Jill','John','Shaw','Shane'],
        'age': [21,24,37,52,17],
        'gender': ['Male','Female','Male','Male','Male'],
        'height': [156,153,145,167,173,],
         'weight': [76,45,65,72,43],
         'BMI': [0,0,0,0,0],
         'Status':[' ',' ',' ',' ',' ']}

data1  = {'BMI': []}
dt = pd.DataFrame(data ,)
dt1=pd.DataFrame(data1 ,)
print (dt)

print(dt.sort_values(by=['height'], ascending=[False]))

name=dt['name'].values
height=dt['height'].values
weight=dt['weight'].values
e=[]
s=[]


i=0



while i<5:
   
    bmi = weight[i]/(height[i]*height[i])
    e.append(bmi)  
    if bmi <= 18.5:
        s.append('Underweight')
        print("for name of %s" %name[i])
        print('Your BMI is', bmi,'which means you are underweight.')

    elif bmi > 18.5 and bmi < 25:
        s.append('Normal')
        print("for name of %s" %name[i])
        print('Your BMI is', bmi,'which means you are normal.')

    elif bmi > 25 and bmi < 30:
        s.append('Overweight')
        print("for name of %s" %name[i])
        print('your BMI is', bmi,'overweight.')

    elif bmi > 30:
        s.append('Obese')
        print("for name of %s" %name[i])
        print('Your BMI is', bmi,'which means you are obese.')

    else:
        print('There is an error with your input')
        print('Please check you have entered whole numbers\n'
              'and decimals were asked.')
    i=i+1


se = pd.Series(e)
dt['BMI'] = se.values

se1 = pd.Series(s)
dt['Status'] = se1.values

dt.groupby(['Status'])

print(dt)



