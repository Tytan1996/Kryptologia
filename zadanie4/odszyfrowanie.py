#kod szyfrujący tekst kodem  Vigenère'a
#wymaganie:  otwieranie tekstu i klucza z plików, zapisywanie wyników do pliku. +  szyfrowanie alfabetu 26-znakowego, pozostałe znaki są usuwane
import time
import re

def wczytajPlik(nazwa_pliku):
    try:
        with open(nazwa_pliku + '.txt', "r", encoding="utf-8") as plik:
            tekst = plik.read()
            #print(tekst)
            return tekst
    except FileNotFoundError:
        print("Nie istnieje plik, podaj poprawną nazwę.")

def zapisPliku(tekstSzyfrowany, nazwa):
    plik=open(nazwa+".txt",'w', encoding="utf-8")
    plik.write(tekstSzyfrowany)
    plik.close()
    
    

def usunPolskieZnaki(tekst):
    znakiPl="ąęółżźśćńĄĘÓŁŻŹŚĆŃ"
    znaki="aeolzzscnAEOLZZSCN"
    for i in range(len(znaki)):
        tekst=tekst.replace(znakiPl[i],znaki[i])
    return tekst


def vigenere_decipher(tekst, klucz, kod=None):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    znakiPl="ąćęłńóśżź"
    wynik = ""
    klucz=klucz.lower()
    if not kod:
        kod=''
        for i in [any((True for x in znakiPl if x in tekst)), ' ' in tekst, any(x.isdigit() for x in tekst)]:
            if i:
                kod+='1'
            else:
                kod+='0'
     
    lista=[znakiPl, ' ', '0123456789']
    kod=str(kod).rjust(3,'0')
    for i in range(3):
        if int(kod[i]):
            alfabet+=lista[i]
    
    if not int(kod[i]):
        klucz=usunPolskieZnaki(klucz)
    for i in range(len(tekst)):
        litera_idx = alfabet.index(tekst[i])
        klucz_idx = alfabet.index(klucz[i % len(klucz)])
        #print(indeks_klucza)
        litera = alfabet[(litera_idx - klucz_idx) % len(alfabet)]
        wynik += litera

    return(wynik)
    



# wynik=vigenere_decipher("zakodowane2", 'tajnehaslo',11)
# print(wynik)
# zapisPliku(wynik, 'odkodowane2')
