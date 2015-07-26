# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 18:40:30 2015

@author: optimumlogistic
"""
import pylab as p
import numpy as np

#Define Parameters#

alpha = 1  
theta = 0.064 
sigma = 0.27 
R0 = 3
time = 1
n_path = 1000   
n = 1000     

#Generate Brownian motions#

dt = 1 / n
t = p.linspace(0,1,n+1)[:-1]   
dB = p.randn(n_path,n+1) * p.sqrt(dt) 
dB[:,0] = 0
B = dB.cumsum(axis=1)
R = p.zeros_like(B)
R[:,0] = R0

for col in range(n):
    R[:,col+1] = R[:,col] + (theta-R[:,col])*dt + sigma*R[:,col]*dB[:,col+1]

#Plot Mean Reversal Pocess with 5 realization points#

R_sample = R[0:5:,:-1]
p.plot(t,R_sample.transpose())
label = 'Time , $t$' ; p.xlabel(label)          
label = '$Rt$' ; p.ylabel(label)
para1 = '\n with $\\alpha$ = ' + str(alpha)
para2 = ', $\\theta$ = ' + str(theta)
para3 = ', and $\sigma$ = ' + str(sigma) + '\n'
p.title('Mean reversal process of 5 runs' + label + para1 + para2 + para3)
p.show()

#Calculate E[R(1)]#

R1 = p.array(R[:,-1])
E_R1 = np.mean(R1)
print('E(R1) = ' + str(E_R1))

#Calculate P(R(1)>2)#

mask = R[:,-1] > 2
P_R1 = sum(mask)/n_path
print('P(R1 > 2) = ' + str(P_R1))
