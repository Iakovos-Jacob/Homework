#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Problem 1 for Homework #7
from math import pi, cos,log
from numpy import random
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

the_great_list = []
def gausian(z0, σ):
    m = random.rand()
    θ = 2*pi*random.rand()
    r = (-2*(σ)**2*log(1-m))**(1/2)
    x = r*cos(θ)
    return  x + z0
for j in range (100001):
    i = gausian(-1,2)
    the_great_list.append(i)
plt.hist(the_great_list, 350, facecolor='c', alpha=0.5)


# In[10]:


#Problem 2 on Homework #7
from random import random
from numpy import arange 
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

NBi = 10000   # # of Bismuth Atoms 
NPb = 0      # # of Lead Atoms 
NTh = 0      # # of Thalium Atoms
NBi209 = 0   # # of Bismuth 209 Atoms 
tau = 46*60  # Half-Life of Bi in sec
tau1 = 2.2*60 # Half-Life of Ti in sec 
tau2 = 3.3*60 # Half-Life of Pb in sec 
h = 1.0      # Size of the time step (s)
p = 1 - 2**(-h/tau)  # Probability of Bi decaying 
z = 1 - 2**(-h/tau1) # Probability of Ti decaying 
f = 1 - 2**(-h/tau2) # Probability of Pb decaying
tmax = 20000
#create lists of atoms
tpoints = arange(0.0,tmax,h)
BIpoints = []
Thpoints = []
PBpoints = []
BI209points = []
for t in tpoints: 
    BIpoints.append(NBi)
    Thpoints.append(NTi)
    PBpoints.append(NPb)
    BI209points.append(NBi209)
    
    # calculate the number of atoms that decay for each element
    decay = 0
    decayTh = 0
    decayPb = 0 
    decayBi = 0
    for i in range(NPb):
        if (random() < f):
            decayBi += 1
    NPb -= decayBi
    NBi209 += decayBi
    for j in range(NTh):
        if (random() < z):
            decayTh += 1
    NTh -= decayTh
    NPb += decayPb
    for k in range(NBi):
        if (random() < p):
            decay +=1
            if (random() < 0.9791):
                decayPb += 1
            else:
                decayTh += 1
    NBi -= decay
    NTh += decayTh
    NPb += decayPb
    
fig = plt.figure()
ax =fig.add_subplot(111)
ax.scatter(tpoints,BIpoints, s=5, c='b', alpha=0.3)
ax.scatter(tpoints,Thpoints, s=5, c='r', alpha=0.3)
ax.scatter(tpoints,PBpoints, s=5, c='c', alpha=0.3)
ax.scatter(tpoints,BI209points, s=5, c='y', alpha=0.3)
ax.set_xlabel("$Time$ $s$", size=20)
ax.set_ylabel("# of Atoms", size=20)
ax.xaxis.set_tick_params(labelsize=20)
ax.yaxis.set_tick_params(labelsize=20)


# In[ ]:




