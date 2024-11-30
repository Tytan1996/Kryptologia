# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import datetime
import math

def ur(a):
    u=0
    r=a-1
    while r%2==0:
        r=r/2
        u=u+1
        return u, r

def pirewszaMR(a,s):
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
                z=pow(t,r)%a
                if z!=1:
                    j=0
                    while z!=a-1:
                        z=(z**2)%a
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

def priewsza(a):
    start = datetime.datetime.now()
    p=True
    if a==1:
        p=False
    elif (a==2) or (a== 3):
        p=True
    elif a%2==0:
        p=False
    else:
        while p==1:
            for i in range(2,int(math.sqrt(a))):
                if (a%i)==0:
                    p=False
                    break
            break
    end = datetime.datetime.now()
    czas=(end-start).microseconds
    return p, czas

def priewszaF(a,s):
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
                if math.pow(t, (a-1))%a!=1:
                    p=False
                    break
    end = datetime.datetime.now()
    czas=(end-start).microseconds
    return p, czas

a=101
s=9
wartosci=priewsza(a)
print(wartosci[0])
wartosci1=priewszaF(a,s)
print(wartosci1[0])
wartosci2=pirewszaMR(a,s)
print(wartosci2[0])