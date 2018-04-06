# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 16:08:15 2018

@author: user
"""

import numpy as np
names=[]
marks=[]
sub1=[]
sub2=[]
sub3=[]
for i in range(10):
    names.append(input("Enter the names of students"))
    x,y,z=map(int,input("Enter marks for 3 subjects: ").split())
    sub1.append(x)
    sub2.append(y)
    sub3.append(z)
    print(names,sub1,sub2,sub3)
    
    mean_sub1=np.mean(sub1)
    mean_sub2=np.mean(sub2)
    mean_sub3=np.mean(sub3)
    
    med_sub1=np.median(sub1)
    med_sub2=np.median(sub2)
    med_sub3=np.median(sub3)
    d={}
    for i in range(3):
        d[names[i]]=(sub1[i]+sub2[i]+sub3[i])/3
        print(sub1.sort(),sub2.sort(),sub3.sort())
        
        for i in d:
            if d[i]>90:
                print("A+")
            elif d[i]>80:
                print("A")
            elif d[i]>70:
                print("B+")
            elif d[i]>50:
                print("C")
            elif d[i]<50:
                print("D")