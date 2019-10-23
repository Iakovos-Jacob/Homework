#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Program that implements the Fizz Buzz dilemma
for x in range(1,101):
    if (x % 3 == 0) and (x % 5 == 0):
        print('FizzBuzz')
    elif  (x % 3 == 0) and (not(x % 5 == 0)):
        print('Fizz')
    elif (not(x % 3 == 0)) and (x % 5 == 0):
        print('Buzz')
    else:
        print(x)


# In[43]:


#Debye's theory of solids that gives the heat capacity of a solid 
import numpy as np
from matplotlib import pyplot as plt
r = 6.022*10**(28)  #Solid Density of solid aluminium
th = 428            #Debye Temperature
kB = 1.3806*10**(-23) #Boltzmann's Constant
V= 0.001        #Volume in meters cubed
a = []
b = []
def cv(T):
    def f(x):
        return((x**4*np.e**x)/((np.e**x-1)**2))
    N = 1000
    a = 0.0 
    b = (th/T)
    h = (b-a)/N
    s = 0.5*f(b)
    for k in range (1,N):
        s+= f(a + k*h)
    return 9*V*r*kB*((T/th)**3) * (h*s)
for T in range (5,501):
    a.append(T)
    b.append(cv(T))
# Making a graph of heat capacity with respect to temperature
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(a,b,s=5,c='k',alpha=0.3)

# add the labels
ax.set_xlabel("${Temperature}$ $(Kelvin)$",size=20) # allows LaTeX style formating
ax.set_ylabel("${Heat_Capacity}$ $(J/K)$",size=20)      # allows LaTeX style formating

# increase the size of the numbers on the axes
ax.xaxis.set_tick_params(labelsize=20)
ax.yaxis.set_tick_params(labelsize=20)


# In[ ]:




