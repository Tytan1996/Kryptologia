# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 14:24:01 2024

@author: 48513
"""
import regex as re
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

#%%

def wczytajPlik(nazwaPliku):   #funkcja Maćka
    try:
        Plik=open(nazwaPliku+".txt","r", encoding="utf-8")
        tekst=Plik.read()
        Plik.close()
        return tekst
    except:
        print("Nie istnieje plik, podaj poprawna nazwe.")
        
de=wczytajPlik('sprawdzam_de')

def letterFreq(tekst, top):
    litery=list(filter(lambda x: x.isalpha(), list(tekst.lower())))
    return pd.Series(litery).value_counts()[0:top]

print(letterFreq(de, 12))

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
        
    
    lista2=lista2[j:j+top]
    
    shift=(ord(lista2[0])-ord(lista[0]))%26
        
    return shift
 
    
def polski(tekst, top=7):
    lista=['a', 'i', 'o', 'e', 'z', 'n', 'r',
           'w', 's', 't', 'c', 'y', 'k', 'd',
           'p', 'm', 'u', 'j', 'l', 'ł', 'b',
           'g', 'ę', 'h', 'ą', 'ó', 'ż', 'ś',
           'ć', 'f', 'ń', 'q', 'ź', 'v', 'x'][0:top]
    
    freq=letterFreq(tekst, top)
    
    
    shift=(ord(freq.index[0])-ord(lista[0]))%len(lista)
    for i in range(0,top):
        if shift!= (ord(freq.index[i])-ord(lista[i]))%len(lista):
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
        
    
    lista2=lista2[j:j+top]
    
    shift=(ord(lista2[0])-ord(lista[0]))%26
        
    return shift 
    

def polski(tekst, top=7):
    lista=['a', 'i', 'o', 'e', 'z', 'n', 'r',
           'w', 's', 't', 'c', 'y', 'k', 'd',
           'p', 'm', 'u', 'j', 'l', 'ł', 'b',
           'g', 'ę', 'h', 'ą', 'ó', 'ż', 'ś',
           'ć', 'f', 'ń', 'q', 'ź', 'v', 'x'][0:top]
    
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
        
    
    lista2=lista2[j:j+top]
    
    shift=(ord(lista2[0])-ord(lista[0]))%26
        
    return shift 


def niemiecki(tekst, top=2):
    lista=['e', 'n', 'i', 's', 'r', 'a', 't',
           'd', 'h', 'u', 'l', 'c', 'g', 'm',
           'o', 'b', 'w', 'f', 'k', 'z', 'v',
           'ü', 'p', 'ä', 'ß', 'j', 'ö', 'y',
           'q', 'x'][0:top]
    
    freq=letterFreq(tekst, top)
    
    
    shift=(ord(freq.index[0])-ord(lista[0]))%len(lista)
    for i in range(0,top):
        if shift!= (ord(freq.index[i])-ord(lista[i]))%len(lista):
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
        
    
    lista2=lista2[j:j+top]
    
    shift=(ord(lista2[0])-ord(lista[0]))%26
        
    return shift 

#%%   
    
ang= wczytajPlik('prologueEn_szyfr') 
ang2 = wczytajPlik('koniec_ang')
pl = wczytajPlik('koniec_pl')

de=wczytajPlik('koniec_de')


#%%

x=[]
k_Ang=[]
for i in range(50,len(ang),50):
    klucz=angielski(ang[0:i])
    x.append(i)
    k_Ang.append(klucz)

fig, ax = plt.subplots(layout='constrained')
fig.suptitle('Angielski (klucz = 7)')
ax.axhline(7, ls='--', c='red', lw=1 ,label='klucz')
ax.plot(x,k_Ang)
plt.show()


x=[]
k_Ang=[]
k_Ang2=[]
for i in range(50,len(ang2),50):
    klucz=angielski(ang2[0:i])
    klucz2=angielski(ang2[0:i], top=1)
    x.append(i)
    k_Ang.append(klucz)
    k_Ang2.append(klucz2)

fig, ax = plt.subplots(layout='constrained')
fig.suptitle('Angielski (klucz = 15)')
ax.axhline(15, ls='--', c='red', lw=1, label='klucz' )
ax.plot(x,k_Ang, c='b', lw=2, label='top=7')
ax.plot(x,k_Ang2, c='g', lw=1.5, label='top=1')

ax.legend(fontsize='small')
plt.show()


x=[]
k_Pl=[]
k_Pl2=[]
for i in range(50,len(pl),50):
    klucz2=polski(pl[0:i],top=4)
    klucz=polski(pl[0:i])
    x.append(i)
    k_Pl.append(klucz)
    k_Pl2.append(klucz2)

fig, ax = plt.subplots(layout='constrained')
fig.suptitle('Polski (klucz = 15)')
ax.axhline(15, ls='--', c='red', lw=1, label='klucz' )
ax.plot(x,k_Pl, c='b', lw=2, label='top=7')
ax.plot(x,k_Pl2, c='g', lw=1.5, label='top=4')
ax.legend(fontsize='small')

plt.show()


x=[]
k_De=[]
k_De2=[]
for i in range(50,len(de),50):
    klucz2=niemiecki(de[0:i],top=10)
    klucz=niemiecki(de[0:i], top=8)
    x.append(i)
    k_De.append(klucz)
    k_De2.append(klucz2)



fig, ax = plt.subplots(layout='constrained')
fig.suptitle('Niemiecki (klucz = 10)')
ax.axhline(10, ls='--', c='red', lw=1, label='klucz' )
ax.plot(x,k_De, c='b', lw=2, label='top=8')
ax.plot(x,k_De2, c='g', lw=1.5, label='top=10')
ax.legend(fontsize='small')

plt.show()


