#import numpy as np
import pandas as pd
import regex as re
#import os
import random

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
    freq=pd.Series(litery).value_counts()/len(tekst)*100
    
    return freq


polski=['a', 'e', 'o','i', 'z', 'n', 's', 'r', 'w',  # z w
        'c', 't', 'l', 'y', 'k', 'd', 'p', 'm', 'u',
        'j', 'b','g', 'h', 'f', 'q', 'v', 'x'] 

angielski=['e', 't', 'a', 'o', 'n', 'i', 's', 'h','r', # t h
           'd', 'l', 'f', 'c', 'm', 'u', 'g', 'y', 'p',
           'w', 'b', 'v', 'k', 'j', 'x', 'z', 'q']



tekst= wczytajPlik("tekst2")
freq=letterFreq(tekst,1000)

print(freq)

for i in range(len(angielski)):
    print(freq.keys()[i], angielski[i], round(freq[i],3))

litery=list(freq.keys())



def zbitki(tekst):

    reg= re.compile(r"(.)\1\1")
    match = re.findall(reg, tekst)
    
    # if match:
    #     if match.group(1) not in dl:
    #         dl[match.group(1)] =1
    #         print(match.group)
            
    #     else:
    #         dl[match.group(1)]+=1
            
    print(pd.Series(match).value_counts())
    
zbitki(tekst)


def trigraphs(tekst):
    trigraphs={}
    for i in range(len(tekst)-2):
        tri=tekst[i]+tekst[i+1]+tekst[i+2]
        if tri in trigraphs:
            trigraphs[tri]+=1
        else:
            trigraphs[tri]=1
    return {k: v for k, v in sorted(trigraphs.items(), key=lambda item: item[1], reverse=True) if v>300}


def quadgraphs(tekst):
    q={}
    for i in range(len(tekst)-3):
        d=tekst[i]+tekst[i+1]+tekst[i+2]+tekst[i+3]
        if d in q:
            q[d]+=1
        else:
            q[d]=1
    return {k: v for k, v in sorted(q.items(), key=lambda item: item[1], reverse=True) if v>300}


print(trigraphs(tekst))
print(quadgraphs(tekst))

def podmien(tekst, jezyk, litery):
    odszyfrowny=''
    lista=list(tekst)
    for znak in lista:
        if znak.isalpha():
            odszyfrowny+=jezyk[litery.index(znak.lower())]
        else:
            odszyfrowny+=znak
    return odszyfrowny


sure={'a':'e', 'm':'t', 'd':'h', 'y':'r', 'x':'o'}
guess={ 'o':'n', 'h':'s', 'q':"b", 'i':'c', 'w':'i', 'v':'a', 'g':'p', 'n':'l', 'e':'u', 
       'j':'v', 'p':'x', 'u':'g', 'f':'y', 'b':'w', 'c':'d', 's':'f', 'k':'m', 'z':'k', 't':'q','r':'j'}

#u ->s   'f':'m', , 'b':'s', 'h':'y'

a={'n':'s', 'l':'z', 'f':'b', 'g':'d',
      'r':'q', 't':'x', 'z':'j','p':'k', 'h':'n',  'j':'v',
      'v':'i', 'o':'l', 'c':'u', 'w':'a', 'b':'y','e':'c',
     'i':'f', 'k':'g', 's':'m', 'u':'p', 'q':'w' }

keys=[i for i in list(a.keys()) if i not in guess.keys()]
random.shuffle(keys)
values=[i for i in list(a.values()) if i not in guess.values()]
random.shuffle(values)

losowo=dict(map(lambda i,j : (i,j) , keys,values))

lista=sure|guess|losowo

odszyfrowny=''


for l in tekst:
    if l.lower() in lista.keys():
        odszyfrowny+=lista[l.lower()]
    else:
        odszyfrowny+=l
    
print(odszyfrowny[0:1000])

def zapisPliku(tekst,nazwa, klucz):
    plik=open(nazwa+"_odszyfrowany.txt",'w', encoding="utf-8")
    plik.write(tekst)
    plik.close()
    plik2=open(nazwa+'_klucz.txt', 'w', encoding="utf-8")
    plik2.write(str(klucz))
    plik2.close()
    
zapisPliku(odszyfrowny, 'tekst2', lista) 

#print(podmien(tekst,angielski,litery))


# the other root