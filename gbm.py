# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pylab as p
import numpy as np

#Define Parameters#

mu=0.1; sigma=0.26; S0=39;
n_path=1000; n=1000; time=3;

#Generate Brownian Motion#

t=p.linspace(0,3,n+1)
dB=p.randn(n_path,n+1)/p.sqrt(n/time); dB[:,0]=0
B=dB.cumsum(axis=1)

#Calculate Stock Price#

nu=(mu-sigma*sigma/2.0)
S = p.zeros_like(B); S[:,0]=S0
S[:,1:]=S0*p.exp(nu*t[1:]+sigma*B[:,1:])

#Plot GBM using 5 realizations points#
S_sample=S[0:5]
p.plot(t,S_sample.transpose())
label='Time, $T$'; p.xlabel(label)
label= 'Stock Price, $St$'; p.ylabel(label)
p.title('GBM of ' + label + '\n with $\mu$ = ' + str(mu) + ' and $\sigma$ = ' + str(sigma))
p.show();

#Calculate E[S(3)] & Var[S(3)]#

S3=p.array(S[:,-1])
E_S3=np.mean(S3)
Var_S3=np.var(S3)
print('E(S3)='+str(E_S3),'\nVar(S3)='+str(Var_S3))

#Calculate P[S(3)> 39] & E[S(3)|S(3)>39]#

mask = S3 > 39
P_S3 = sum(mask) / len(mask)
S3_39 = S3 * mask 
E_S3_39 = sum(S3_39) / sum(mask)
print('P(S3 > 39) = ' + str(P_S3) , '\nE(S3 | S3 > 39) = ' + str(E_S3_39))

#Using Formula to findE[S( 3)] & Var[S(3)]#
print('\nTheoritical expectation and variance:')
E = S0 * p.exp(mu*time)
Var = (S0**2)*(np.exp(2*mu*time))*(np.exp(sigma*sigma*time)-1)
print('E('+ str(time) + ') = ' + str(E) , '\nVar('+str(time) + ') = ' + str(Var))
