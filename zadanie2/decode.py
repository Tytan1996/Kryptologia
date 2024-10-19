# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import re
import os

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
 




def wczytajPlik(nazwaPliku):   # funkcja Maćka
    try:
        Plik = open(nazwaPliku + ".txt", "r", encoding="utf-8")
        tekst = Plik.read()
        Plik.close()
        return tekst
    except FileNotFoundError:
        print(f"Nie istnieje plik: {nazwaPliku}, podaj poprawną nazwę.")
        return None 


def zapisPliku(tekst,nazwa):
    plik=open(nazwa+".txt",'w', encoding="utf-8")
    plik.write(tekst)
    plik.close()
        
        
def odkodowanie(tekst, klucz):
    tekst=tekst.lower()
    alfabet_maly="abcdefghijklmnopqrstuvwxyz"
    odkodowany_tekst=""

    for i in tekst:
        if i in alfabet_maly:
            odkodowany_tekst+=alfabet_maly[(alfabet_maly.index(i)-klucz)%len(alfabet_maly)]
        
        elif i.isdigit():
            odkodowany_tekst += str((int(i) - klucz) % 10)
     
    return odkodowany_tekst



def dekodowanie():
    nazwapliku = input("Podaj nazwę pliku dla którego chcesz odgadnąć klucz: ")
    sciezka = os.path.join('zaszyfrowane', nazwapliku)
    tekst = wczytajPlik(sciezka)
    for i in range(1,8):
        klucz1= stat(tekst,angielski, i)
        print(klucz1)
        klucz2 =stat(tekst,polski, i)
        print(klucz2)
        ang=''.join(odkodowanie(tekst, klucz1).split())
        print(ang[:50])
        pl=''.join(odkodowanie(tekst, klucz2).split())
        print(pl[:50])
        #dla angielskiego sprawdzamy 'the'
        #dla polskiego sprawdzamy 'prz'
        zliczenie_ang = len(re.findall('the', ang))
        print("zliczenie ang")
        print(zliczenie_ang)
        zliczenie_pl = len(re.findall('prz', pl))
        print("zliczenie pl")
        print(zliczenie_pl)
        if zliczenie_ang > zliczenie_pl:
            print("Treść tekstu jest w języku angielskim")
            zapisPliku(ang, nazwapliku+"decoded.txt")
            print(ang[:100])
            break
        elif zliczenie_pl > zliczenie_ang:
            print("Treść tekstu jest w języku polskim")
            zapisPliku(pl, nazwapliku+"decoded.txt")
            print(pl[:100])
            break
        elif zliczenie_pl == zliczenie_ang:
            zliczenie_pl2 = len(re.findall('szcz', pl))
            if zliczenie_ang > zliczenie_pl:
                print("Treść tekstu jest w języku angielskim")
                zapisPliku(ang, nazwapliku+"decoded.txt")
                print(ang[:100])
                break
            elif zliczenie_pl > zliczenie_ang:
                print("Treść tekstu jest w języku polskim")
                zapisPliku(pl, nazwapliku +"decoded.txt")
                print(pl[:100])
                break
        elif zliczenie_pl == 0  and zliczenie_ang == 0:
            i+=1
    
dekodowanie()

#p1=wczytajPlik('zaszyfrowane\\5')

#klucz1= stat(p1,angielski, 1)
#print("klucz1")
#print(klucz1)
#klucz2 =stat(p1,polski, 1)
#print("klucz2")
#print(klucz2)

#ang=''.join(odkodowanie(p1, klucz1).split())

#pl=''.join(odkodowanie(p1, klucz2).split())

#print('the', len(re.findall('the', ang)))
#print('prz', len(re.findall('prz', pl)))
#print('szcz', len(re.findall('szcz', pl)))


