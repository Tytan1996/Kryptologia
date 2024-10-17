# -*- coding: utf-8 -*-

import regex as re
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

#%%

def wczytajPlik(nazwaPliku):
    try:
        Plik=open(nazwaPliku+".txt","r", encoding="utf-8")
        tekst=Plik.read()
        Plik.close()
        return tekst
    except:
        print("Nie istnieje plik, podaj poprawna nazwe.")
        


def letterFreq(tekst, top):
    litery=list(filter(lambda x: x.isalpha(), list(tekst.lower())))
    return pd.Series(litery).value_counts()[0:top]


polski=['a', 'e', 'o','i', 'z', 'n', 's', 'r', 'w',  # z w
        'c', 't', 'l', 'y', 'k', 'd', 'p', 'm', 'u',
        'j', 'b','g', 'h', 'f', 'q', 'v', 'x'] 

angielski=['e', 't', 'a', 'o', 'n', 'i', 's', 'h','r', # t h
           'd', 'l', 'f', 'c', 'm', 'u', 'g', 'y', 'p',
           'w', 'b', 'v', 'k', 'j', 'x', 'z', 'q']



def stat(tekst,  alfabet, top=7):
    lista=alfabet[:top]
    
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
 




def wczytajPlik(nazwaPliku):   #funkcja Maćka
    try:
        Plik=open(nazwaPliku+".txt","r", encoding="utf-8")
        tekst=Plik.read()
        Plik.close()
        return tekst
    except:
        print("Nie istnieje plik, podaj poprawna nazwe.")
        
        
        
        
def odkodowanie(tekst, klucz):
    alfabet_maly="abcdefghijklmnopqrstuvwxyz"
    alfabet_duzy="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    znakiPlMale="ąćęłńóśżź"
    znakiPlDuze="ĄĆĘŁŃÓŚŻŹ"
    znakiDeMale="äüöß"
    znakiDeDuze="ÄÜÖ"
    odkodowany_tekst=""



    for i in tekst:
        if i in alfabet_maly:
            odkodowany_tekst+=alfabet_maly[(alfabet_maly.index(i)-klucz)%len(alfabet_maly)]
        elif i in alfabet_duzy:
            odkodowany_tekst+=alfabet_duzy[(alfabet_duzy.index(i)-klucz)%len(alfabet_duzy)]
        elif i in znakiPlMale:
            odkodowany_tekst+=znakiPlMale[(znakiPlMale.index(i)-klucz)%len(znakiPlMale)]
        elif i in znakiPlDuze:
            odkodowany_tekst+=znakiPlDuze[(znakiPlDuze.index(i)-klucz)%len(znakiPlDuze)]
        elif i in znakiDeMale:
            odkodowany_tekst+=znakiDeMale[(znakiDeMale.index(i)-klucz)%len(znakiDeMale)]
        elif i in znakiDeDuze:
            odkodowany_tekst+=znakiDeDuze[(znakiDeDuze.index(i)-klucz)%len(znakiDeDuze)]
        elif i.isdigit():
            odkodowany_tekst += str((int(i) - klucz) % 10)

            
        else:
            odkodowany_tekst+=i
        
    return odkodowany_tekst



        
        
p1=wczytajPlik('zaszyfrowane\\6')

klucz1= stat(p1,angielski, 1)
klucz2 =stat(p1,polski, 1)


print(odkodowanie(p1, klucz1)[:50])
print()
print(odkodowanie(p1, klucz2)[:50])

