# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 01:17:13 2018

@author: moury
"""

#import numpy as nd
lowrange = 1
highrange = 500
n = int(input("Enter N number"))
array=[]
for i in range(1,n+1):
    #print(i.sepe=" " , end = " ")
    array.append(i)
print("=",sum(array))
print()
#print divisble by n from 1 to 500
for i in range(lowrange, highrange+1):
    if(i%n == 0) : 
        print(i)
#multiply n+nn+nnn
temp = str(n)
t1 = temp+temp
t2 = temp + temp + temp
comp = n+int(t1)+int(t2)
print("value of n+nn+nnn:", comp)
'''
for n in range(1,n+1):
    array.append(1)
    for i in range(n-2 , 0,-1):
        array[i] += array[i-1]
    print("ROW",n,array)
'''
#Pascal traingle
array=[]
for i in range(n):
    array.append([])
    array[i].append(1)
    for j in range(1,i):
        array[i].append(array[i-1][j-1]+array[i-1][j])
    if(n!=0):
        array[i].append(1)
for i in range(n):
    print("   "*(n-i),end=" ",sep=" ")
    for j in range(0,i+1):
        print('{0:6}'.format(array[i][j]),end=" ",sep=" ")
    print()
    
#Find the sum of series, 1 + ½ + 1/3 +……. + 1/n 
sum1=0
for i in range(1,n+1):
    sum1=sum1+(1/i)
print("The sum of series is",round(sum1,2))