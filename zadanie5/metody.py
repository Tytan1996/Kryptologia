# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 10:38:14 2024

@author: 48513
"""
import datetime

def euklid(g,p):
    tablica=[[p,1,0],
             [g,0,1,-(p//g)]]
    for i in range(len(tablica)):
        t=[]
        t.append(tablica[-2][0]%tablica[-1][0])
        t.append(tablica[-1][1]*tablica[-1][-1]+tablica[-2][1])
        t.append(tablica[-1][2]*tablica[-1][-1]+tablica[-2][2])
        
        #print(tablica)
        if t[0]==1:
            return t[-1]
            break
        t.append(-(tablica[-1][0]//t[0]))
        tablica.append(t)      

def potega(a,b,p):
    wynik=a
    for i in range(1, b):
        wynik=(wynik*a)%p
    return wynik


def metodaBrutalna(g,p,h):
    start = datetime.datetime.now()
    for a in range(p):
        if potega(g,a,p)==h:
            end = datetime.datetime.now()
            czas=(end-start).microseconds
            #print(f"{g}^a (mod {p})={h} dla a={a}")
            return a,czas
        
print(euklid(5, 17))