# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 14:24:01 2024

@author: 48513
"""
import regex as re
import numpy as np
import pandas as pd
from zadanie1odkodowanie import wczytajPlik, odkodowanie

def letterFreq(tekst, top):
    litery=list(filter(lambda x: x.isalpha(), list(tekst.lower())))
    return pd.Series(litery).value_counts()[0:top]



def angielski(tekst, top=7):
    lista=['e', 't', 'a', 'o', 'n', 'i', 's', 'h','r',
          'd', 'l', 'f', 'c', 'm', 'u', 'g', 'y', 'p',
          'w', 'b', 'v', 'k', 'j', 'x', 'z', 'q'][0:top]
    
    freq=letterFreq(tekst, top)
    
    
    shift=(ord(freq.index[0])-ord(lista[0]))%26
    for i in range(0,top):
        if shift!= (ord(freq.index[i])-ord(lista[i]))%26:
            shift=None
            break
        
    if shift!=None:
        return shift
    
    lista=sorted(lista)
    
    lista2=sorted(freq.index)*2
    
    
    j=0
    for i in range(0, len(lista)-1):
        if (ord(lista[i])-ord(lista[i+1]))%26!=(ord(lista2[i+j])-ord(lista2[i+j+1]))%26:
            j+=1
        if 
    if 
    lista2=lista2[j:j+top]
    
    shift=(ord(lista2[0])-ord(lista[0]))%26
        
    return shift
 
#%%   
    
tekst= wczytajPlik() 

#%%
klucz=angielski(tekst)
print(klucz)

#%%

for i in range(50,len(tekst),50):
    klucz=angielski(tekst[0:i])
    print(i, klucz)


