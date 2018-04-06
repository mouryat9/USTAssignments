# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 16:08:41 2018

@author: user
"""

d={"children":[],"youth":[],"middle age":[],"senior":[]}
for _ in range(5):
    name=input("Enter name")
    age=int(input("Enter age"))
    if age<15:
        d["children"].append(name)
    elif age>=15 and age<30:
        d["youth"].append(name)
    elif age>=30 and age<50:
        d["middle aged"].append(name)
    else:
        d["senior"].append(name)
        print(d)