#kod szyfrujący tekst kodem  Vigenère'a
#wymaganie:  otwieranie tekstu i klucza z plików, zapisywanie wyników do pliku. +  szyfrowanie alfabetu 26-znakowego, pozostałe znaki są usuwane
import time
import re

def wczytajPlik(nazwa_pliku):
    with open(nazwa_pliku + '.txt', "r", encoding="utf-8") as plik:
        tekst = plik.read()
        #print(tekst)
        return tekst


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


def vigenere_decipher(plik, klucz):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    wynik = ""
    tekst=wczytajPlik(plik)
    
    klucz = usunPolskieZnaki(klucz.lower())

    for i in range(len(tekst)):
        litera_idx = alfabet.index(tekst[i])
        klucz_idx = alfabet.index(klucz[i % len(klucz)])
        #print(indeks_klucza)
        litera = alfabet[(litera_idx - klucz_idx) % len(alfabet)]
        wynik += litera
        if (i%10==0):
            print(tekst[i], litera_idx, klucz_idx, litera)

    return(wynik)
    



wynik=vigenere_decipher("zakodowane", 'tajnehaslo')
zapisPliku(wynik, 'odkodowane')
