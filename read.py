# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 21:05:23 2022

@author: user
"""
data = []
count = 0
count2 = 0
length = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line) #add string of line to data
        count +=1 # count = count + 1
        length = length + len(line) #length of each review of inrequest
        #length = length + len(data) #length of all data
        #if count % 1000 == 0: # count mod 1000 == 0
        if count == 100000:
          print(line)
          print(data[count-1])
          print(len(data))
print('the average length of each review is', round(length/count,2))

#calculate total digital number
sum_len = 0
for d in data:
    sum_len = sum_len + len(d)
print(sum_len)
           
#print('all data was read, there are', len(data), 'data')

#calculate sum of length < 100
new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('total', len(new), 'reviews length < 100')
print(new[0])

#calculate sum of review includes 'good'
good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('total', len(good), 'reviews')
print(good[0])

good = [1 for d in data if 'good' in d] #append in for-loop
print(good)

bad = ['bad' in d for d in data] #boolen in for-loop
print(bad)

bad = [0]
for d in data:
    bad.append('bad' in  d)







