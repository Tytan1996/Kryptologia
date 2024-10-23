# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import re
import os
import time
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
    litery=list(filter(lambda x: x.isalpha(), list(str(tekst).lower())))
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
    
    try:
        shift=(ord(freq.index[0])-ord(lista[0]))%26
        for i in range(1,top):
            if shift!= (ord(freq.index[i])-ord(lista[i]))%26:
                shift=None
                break
    except IndexError:
        shift=None
        raise IndexError("Brak liter w tekście lub tekst jest za krótki. Nie można odnaleźć klucza")

    else:
        if shift!=None:
            return shift
    
        lista=sorted(lista)
    
        lista2=sorted(freq.index)*2
    
        try:
            j=0
            for i in range(0, len(lista)-1):
                if (ord(lista[i])-ord(lista[i+1]))%26!=(ord(lista2[i+j])-ord(lista2[i+j+1]))%26:
                    j+=1
        except IndexError:
            shift = None
            raise IndexError("Tekst jest za krótki. Nie można odnaleźć klucza")
        else:
            lista2=lista2[j:j+top]
        
            shift=(ord(lista2[0])-ord(lista[0]))%26
        
    return shift
 




def zapisPliku(tekst,nazwa):
    plik=open(nazwa+".txt",'w', encoding="utf-8")
    plik.write(tekst)
    plik.close()
        
        
def odkodowanie(tekst, klucz):
    try:
        klucz=int(klucz)
    except (ValueError, TypeError) as e:
        raise ValueError('Klucz powinien być liczbą całkowitą!')
        return
    else:
        tekst=str(tekst).lower()
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
    start = time.time()
    for i in range(5,10):
     try:
        klucz1= stat(tekst,angielski, i)
        klucz2 =stat(tekst,polski, i)
     except IndexError as e:
        print(e)
        return
     else:
        ang=''.join(odkodowanie(tekst, klucz1).split())
        pl=''.join(odkodowanie(tekst, klucz2).split())
        #dla angielskiego sprawdzamy 'the'
        #dla polskiego sprawdzamy 'prz'
        zliczenie_ang = len(re.findall('the', ang))
        zliczenie_pl = len(re.findall('prz', pl))
        if zliczenie_ang > zliczenie_pl:
            zapisPliku(ang, 'odszyfrowane/'+nazwapliku+"decoded.txt")
            end = time.time()
            return end - start, i
        elif zliczenie_pl > zliczenie_ang:
            zapisPliku(pl, 'odszyfrowane/'+nazwapliku+"decoded.txt")
            end = time.time()
            return end - start, i
        elif zliczenie_pl == zliczenie_ang:
            zliczenie_pl2 = len(re.findall('szcz', pl))
            if zliczenie_ang > zliczenie_pl2:
                zapisPliku(ang, 'odszyfrowane/'+nazwapliku+"decoded.txt")
                end = time.time()
                return end - start, i
            elif zliczenie_pl2 > zliczenie_ang:
                zapisPliku(pl, 'odszyfrowane/'+nazwapliku +"decoded.txt")
                end = time.time()
                return end - start, i
        elif zliczenie_pl == 0  and zliczenie_ang == 0:
            i+=1
 


    
dekodowanie()

def sredni_czas_iteracja(liczbaiteracji):
    czas=[]
    iteracja=[]
    nazwapliku = input("Podaj nazwę pliku: ")

    for i in range(liczbaiteracji):
        c,it = dekodowanie(nazwapliku)
        #print(c)
        #print(it)
        if c is not None and it is not None:

            czas.append(c)
            iteracja.append(it)

    sredni_czas = sum(czas)/liczbaiteracji
    srednia_iteracja = sum(iteracja)/liczbaiteracji

    #return sredni_czas, srednia_iteracja
    print("sredni czas:", sredni_czas)
    print("srednia iteracja:", srednia_iteracja)


#sredni_czas_iteracja(50)


czas=[0.02971471309661865, 0.0503673791885376, 0.10554842948913574, 0.014775562286376952, 0.09075160026550293, 0.035639681816101075, 0.13189016819000243, 0.3842524814605713]
ilosc_liter=[5, 5, 6, 5, 5, 5, 5, 6]
teksty=[1,2,3,4,5,6,7,8]

"""
plt.plot(teksty, czas)
#tu fajnie byłoby dodać drugą linie z czasem dla atau brutelnego dla każdego pliku
plt.title('Średni czas odszyfrowania plików \n (średnia z 50 prób)')
plt.xlabel('dany tekst')
plt.ylabel('czas')
plt.show()
"""
'''
#czy taki wykres jest ok?
plt.bar(teksty, ilosc_liter, color='skyblue')
plt.title("Ilość potrzebnych liter do porównania do odszyfrowania tekstu")
plt.xlabel('Dany tekst')
plt.ylabel('Ilość liter')
plt.xticks(teksty)
plt.show()
'''






