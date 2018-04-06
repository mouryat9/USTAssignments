# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 16:07:32 2018

@author: user
"""

para=input()
print(para)
sen=para.split(".")

sen[len(sen)]="UST Global specializes in Healthcare,Retail & Consumer Goods,Banking & Financial Telecom,Media & Technology,Insurance,Transportation & Logistics and Manufacturing & Utilities."
print("". join(sen))
print(para)



d={"vowels","upper","lower","special character"}
str_copy=""
str_copy=para
for i in para:
   
    if i in ("a","e","i","o","u"):
        d["vowels"]+=1
    elif i.isupper():
        d["upper"]+=1
    elif i.islower():
        d["lower"]+=1
    elif i in ("!","@","#","$","%","^","&","*","(",")","<",">","?","+","-","_","'","."):
              d["special character"]+=1
              print(d)
              str_copy=str_copy.replace(i,"")
              print("Updated paragraph is - \n",str_copy)
             