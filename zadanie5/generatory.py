#ZADANIA:
#1. napisanie i przetestowanie działania funkcji generator(g, p) sprawdzająca, czy g jest generatorem w pierścieniu Zp*,
#2. napisanie i przetestowanie działania funkcji generatory(g, p) wypisująca generatory g w Pierścieniu Z∗p(zapis do pliku).


def generator(g, p):
    #czy g jest generatorem w Zp*
    if p < 2:
        raise ValueError(f'{p} nie jest liczbą pierwszą')
    for i in range(2, p//2 + 1):
        if (p % i) == 0:
            raise ValueError(f'{p} nie jest liczbą pierwszą')
    l = [i for i in range(1, p)] #elementy Zp
    #print(l)
    gl = []
    for k in range(1, p):
        g_k = g**k % p
        gl.append(g_k)
    gl.sort()
    #print(gl)
    if l == gl:
        print(f'liczba {g} jest generatorem w pierścieniu Z_{p}*.')
        return True
    else:
        print(f'liczba {g} nie jest generatorem w pierścieniu Z_{p}*.')
        return False



def generatory(p):
    #wypisuje wszystkie generatory g w pierscieniu Zp i zapisuje je do pliku
    gen = []
    for i in range(1,p):
        if generator(i,p) == True:
            gen.append(i)
    with open("generatory.txt", 'w', encoding="utf-8") as plik:
        plik.write(f"Generatory w pierścieniu Z_{p}*:\n")
        plik.write(", ".join(map(str, gen)))
    
    print(f"Generatory w pierścieniu Z_{p}*: {gen}")
    
    
    




generator(4,17)
#generatory(17)