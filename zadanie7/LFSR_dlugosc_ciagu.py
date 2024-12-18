# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 16:49:55 2024

@author: 48513
"""
import re

import math
def LFSR(p,seed):
    if len(seed)<len(p):
        raise IndexError("seed krótsze niż p!!")

    S=seed[-len(p):]
    seed.append(0)
    for i in range(len(p)):
        seed[-1]=(seed[-1]+S[i]*p[i])%2
    return seed



def LFSR2(p,seed, n):
    if len(seed)<len(p):
        raise IndexError("seed krótsze niż p!!")
    while len(seed)<n:
        S=seed[-len(p):]
        seed.append(0)
        for i in range(len(p)):
            seed[-1]=(seed[-1]+S[i]*p[i])%2
    return seed

print(LFSR2([1,1,0,1,1,0],[0,0,1,0,0,1],100))


def dziesietny(seed):
    l=0
    for i in range(len(seed)):
        #l+=int(seed[i])*2**i
        l+=int(seed[i])*2**(len(seed)-1-i)
    return l

#print(dziesietny([0,0,1,0,1,0]))




# sprawdzić długość generowanych ciągów pseudolosowych


def F(p, seed):
    for i in range(500):
        seed = LFSR(p,seed)
        c = len(seed)
        d = math.ceil(c/2)
        aa= ''.join(map(str, seed[:d]))
        b= ''.join(map(str, seed[d:]))
        if aa in b:
            print(f'Znaleziono powtarzający się ciąg {aa} w {seed}')
            return 
        
F([1,1,0,1,1,0],[0,0,1,0,0,1])




