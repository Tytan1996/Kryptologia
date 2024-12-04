# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import datetime
import math
import pierwsze

def ur(a):
    u=0
    r=a-1
    while r%2==0:
        r=r/2
        u=u+1
        return u, r

def pierwszaMR(a,s):
    start = datetime.datetime.now()
    p=True
    if a==1:
        p=False
    elif (a==2) or (a== 3):
        p=True
    elif a%2==0:
        p=False
    else:
        (u, r) = ur(a)
        for i in range(s):
            for t in range(2,a-2):
                z=pierwsze.potega_m(t,r,a)
                #z=pow(t,r)%a
                if z!=1:
                    j=0
                    while z!=a-1:
                        z=pierwsze.potega_m(z,2,a)
                        j=j+1
                        if(z==1) or (j==u):
                            p=False
                            break
                        break
                    break
                break
    end = datetime.datetime.now()
    czas=(end-start).microseconds
    return p,czas

def pierwsza(a):
    start = datetime.datetime.now()
    p=True
    print(math.sqrt(a))
    if a==1:
        p=False
    elif (a==2) or (a== 3):
        p=True
    elif a%2==0:
        p=False
    else:
        while p==1:
            for i in range(2,int(math.sqrt(a))+1):
                print(i)
                if (a%i)==0:
                    p=False
                    break
            break
    end = datetime.datetime.now()
    czas=(end-start).microseconds
    return p, czas

def pierwszaF(a,s):
    start = datetime.datetime.now()
    p=True
    if a==1:
        p=False
    elif (a==2) or (a== 3):
        p=True
    elif a%2==0:
        p=False
    else:
        for i in range(1,s):
            for t in range(2,a-2):
                if pierwsze.potega_m(t,a-1,a)!=1:
                #if math.pow(t, (a-1))%a!=1:
                    p=False
                    end = datetime.datetime.now()
                    czas=(end-start).microseconds
                    return p, czas
                    break
    end = datetime.datetime.now()
    czas=(end-start).microseconds
    return p, czas

a=6
s=9
    
wartosci=pierwsza(a)
print(wartosci[0])
wartosci1=pierwszaF(a,s)
print(wartosci1[0])
wartosci2=pierwszaMR(a,s)
print(wartosci2[0])
