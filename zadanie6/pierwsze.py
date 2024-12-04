#Stworzyć funkcje:
#1. do potęgowania liczb z użyciem modulo potega_m(a,b,n),
#2. generującą k liczb pierwszych z zakresu [x, y],

import math


def pierwsza(a):
    if a <= 1:
        return 0
    p = 1  
    while p == 1:  
        for i in range(2, math.floor(math.sqrt(a)) + 1):
            if a % i == 0:  
                p = 0 
                break  
        break  

    if p == 1:  
        #print('liczba pierwsza')
        return p 
    elif p == 0:
        #print('liczba nie jest pierwsza')
        return p



#pierwsza(1)

def liczby_pierwsze(k,x,y):
    #k - ilość liczb pierwszych, jeżeli k=0 wyświetla wszystkie
    #x - początek zakresu
    #y - koniec zakresu
    k = int(k)
    x = int(x)
    y = int(y)
    if y < x:
        x, y = y, x #zamiana x i y
    licznik=0
    l=[]
    for i in range(x,y+1):
        if pierwsza(i)==1:
            l.append(i)
            licznik+=1
            if licznik == k:
                break
    print(l)
    return l
        
#liczby_pierwsze(0, 100, 50)

def potega_m(a,b,n):
    #a - podstawa potęgi
    #b - wykładnik potęgi
    #n - dzielenie modulo 
    a = int(a)
    b = int(b)
    n = int(n)
    if n == 0:
        raise ValueError("Argument 'n' nie może być równy 0!")
    a = a % n
    wynik = 1
    while b>0:
        if b % 2 == 1:
            wynik = (wynik*a) % n
        a = a*a % n
        b=b//2
    #print(wynik)
    return wynik


potega_m(25,152,41)
potega_m(25,152.5,6)
