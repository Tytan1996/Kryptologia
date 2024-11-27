import math
import datetime
import metody

def metodaShanksa(p,g,h):
    pier=round(math.sqrt(p))
    lista=[]
    j=0
    licznik=-1
    petla = True
    start = datetime.datetime.now()
    for i in range(pier-1):
        lista.append((g**i)%p)
    while petla:
        licznik+=1
        hg=(h*(p-186)**(pier*licznik))%p
        for i in range(len(lista)):
            if hg==lista[i]:
                j=i
                petla=False
        
    a=licznik*round(math.sqrt(p))+j
    end = datetime.datetime.now()
    czas=(end-start).microseconds
    return a,czas

wynikiKonczoweShanksa=metodaShanksa(1117,6,527)
#wynikiKonczoweBrutalna=metody.metodaBrutalna(6, 1117, 527)

print("Czas metody Shanksa: ")
print(wynikiKonczoweShanksa[0])
print("Czas metody brutalnej: ")
#print(wynikiKonczoweBrutalna[0])

print("Wynik metody Shanksa: ")
print(wynikiKonczoweShanksa[1])
print("Wynik metody brutalnej: ")
#print(wynikiKonczoweBrutalna[1])