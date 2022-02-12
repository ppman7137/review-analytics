# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 21:05:23 2022

@author: user
"""
data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count +=1 # count = coiunt + 1
        if count % 1000 == 0: # count mod 1000 == 0
           print(len(data))

print(len(data))
print(data[0])
print('-----------------------------')
print(data[1])