# -*- coding: utf-8 -*-
"""
Created on Fri May 20 10:08:51 2022

@author: p42597
"""
import datetime
import time
import numpy as np
import pandas as pd
from scipy.stats import randint
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


tic = time.perf_counter()


number_of_trial = 1000
p = np.zeros( shape=(100) )
d = np.zeros( shape=(100) )
max_number_of_people = 100

for number_of_people in range(0,max_number_of_people):
    xbirtday = np.zeros( shape=(number_of_people) )
    sum_havethesameday = 0
    sum_thesameday = 0
    
    for i in range(0,number_of_trial):
        for j in range(0,number_of_people):
            xbirtday[j] = randint.rvs(1,365)
        xbirthdaycount = np.asarray( np.unique(xbirtday, return_counts=True) ).T
        number_of_sameday = len( xbirthdaycount[ xbirthdaycount[:,1] > 1] )
        
        if number_of_sameday > 0 : sum_havethesameday = sum_havethesameday + 1
        sum_thesameday = number_of_sameday + sum_thesameday
    
    p[number_of_people] = sum_havethesameday / number_of_trial
    d[number_of_people] = sum_thesameday / number_of_trial

plt.figure(1)
plt.title("Birthday") 
plt.xlabel("number of people") 
plt.ylabel("p") 
plt.plot(np.arange(0,max_number_of_people),p)


plt.figure(2)
plt.title("Birthday") 
plt.xlabel("number of people") 
plt.ylabel("d") 
plt.plot(np.arange(0,max_number_of_people),d)

plt.figure(3)
plt.title("Birthday") 
plt.xlabel("p") 
plt.ylabel("d") 
plt.plot(d,p)

# plt.figure(1)
# plt.title("Random walk") 
# plt.xlabel("x axis caption") 
# plt.ylabel("y axis caption") 
# plt.plot(np.arange(0,expsize),xrandomwalk)

# plt.figure(2)
# plt.title("CLT") 
# plt.xlabel("x axis caption") 
# plt.ylabel("y axis caption") 
# plot2 = plt.hist(xbar, bins='auto')


toc = time.perf_counter()   
print('time: ',toc-tic)
