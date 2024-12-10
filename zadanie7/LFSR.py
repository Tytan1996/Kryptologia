# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 16:49:55 2024

@author: 48513
"""


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

print(LFSR([1,1,0], [0,0,1]))


def dziesietny(seed):
    l=0
    for i in range(len(seed)):
        l+=int(seed[i])*2**i
        #l+=int(seed[i])*2**(len(seed)-1-i)
    return l

print(dziesietny([0,0,1,0,1,0]))