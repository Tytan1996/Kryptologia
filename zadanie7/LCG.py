# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import LFSR
from datetime import datetime

def LCG(a,b,mod,seed):
    x=(a*seed+b)%mod
    return x

random= datetime.now()
random=random.microsecond
#print(random)
seed = LCG(687 ,28411 ,134456 ,random)

#print (seed)

for i in range (9):
    seed = LCG (8121 ,28411 ,134456 , seed )
    #print (seed)

#testy dla różnych parametrów
p=[]
p1Time=datetime.now()
p1Time=p1Time.microsecond
def generatorSeed(p1Time):
    p.append(p1Time)
    for i in range (1,10):
        if i%2==0:
            x=p[i-1]*(i*2)
        else:
            x=p[i-1]/(i*2)
        x=round(x)
        p.append(x)
    return p

seed = generatorSeed(p1Time)
LCGLista=[]
print("parametry:")
print("8121 ,28411 ,134456")
for i in range(len(seed)):
    x=LCG(8121 ,28411 ,134456 , seed[i] )
    LCGLista.append(x)
    print(f"dla seed: {seed[i]} wychodzi wynik: {LCGLista[i]}")

LCGLista.clear()
print("parametry:")
print("3215 ,451 ,100")
for i in range(len(seed)):
    x=LCG(3215 ,451 ,100 , seed[i] )
    LCGLista.append(x)
    print(f"dla seed: {seed[i]} wychodzi wynik: {LCGLista[i]}")

LCGLista.clear()
print("parametry:")
print("4567 ,4567 ,4567")
for i in range(len(seed)):
    x=LCG(4567 ,4567 ,4567 , seed[i] )
    LCGLista.append(x)
    print(f"dla seed: {seed[i]} wychodzi wynik: {LCGLista[i]}")

LCGLista.clear()
print("parametry:")
print("254 ,4567 ,100")
for i in range(len(seed)):
    x=LCG(254 ,4567 ,100, seed[i] )
    LCGLista.append(x)
    print(f"dla seed: {seed[i]} wychodzi wynik: {LCGLista[i]}")

LCGLista.clear()
print("parametry:")
print("64 ,12 ,100")
for i in range(len(seed)):
    x=LCG(64 ,12 ,100, seed[i] )
    LCGLista.append(x)
    print(f"dla seed: {seed[i]} wychodzi wynik: {LCGLista[i]}")
#próba wygenrowania pseudoliczby 
LCGLista.clear()
print("próby wygenrowania najdluzego ciagu:")
print("LCG:")
liczb1= LCG(99999999545645654645654546546464563535999999999999999999999999999999999999999999999
            ,1 ,
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999,
            999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
print(liczb1)
print("LFSR:")
liczb2=LFSR.LFSR2([1,1,0],[0,0,1],9999)
print(liczb2)
print("LFSR (dziesietne):")
liczb3=LFSR.dziesietny(liczb2)
print(liczb3)
