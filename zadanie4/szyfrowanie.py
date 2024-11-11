#kod szyfrujący tekst kodem  Vigenère'a
#wymaganie:  otwieranie tekstu i klucza z plików, zapisywanie wyników do pliku. +  szyfrowanie alfabetu 26-znakowego, pozostałe znaki są usuwane
import time
import re

def wczytajPlik(nazwa_pliku):
    with open(nazwa_pliku, "r", encoding="utf-8") as plik:
        tekst = plik.read()
        #print(tekst)
        
    wiersze = tekst.splitlines()

    if wiersze and wiersze[0].startswith("klucz "):
        klucz = wiersze[0].split()[1]
        wiersze.pop(0)
        tekst = "\n".join(wiersze)  # Połącz pozostałe wiersze
        return tekst, klucz
    else:
        print("Nie znaleziono danych do kodowania tekstu lub są źle napisane.")
        return tekst

    
    
def usunZnaki(tekst):
    symbole = " .,'!:;/@#$%^&(*)-_+=[{]}|?\n\"0123456789"
    b=range(len(symbole))
    for i in b:
        tekst=tekst.replace(symbole[i],"")
    return tekst

def usunPolskieZnaki(tekst):
    znakiPl="ąęółżźśćńĄĘÓŁŻŹŚĆŃ"
    znaki="aeolzzscnAEOLZZSCN"
    for i in range(len(znaki)):
        tekst=tekst.replace(znakiPl[i],znaki[i])
    return tekst

def zapisPliku(tekstSzyfrowany):
    plik=open("zakodowane.txt",'w', encoding="utf-8")
    plik.write(tekstSzyfrowany)
    plik.close()


def vigenere_cipher(tekst):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    wynik = ""
    do_zakodowania, klucz = wczytajPlik(tekst)

    do_zakodowania = usunZnaki(do_zakodowania)
    do_zakodowania = usunPolskieZnaki(do_zakodowania)
    print(do_zakodowania)
    klucz = usunPolskieZnaki(klucz.lower())

    for i in range(len(do_zakodowania)):
        litera_idx = alfabet.index(do_zakodowania[i].lower())
        #print(litera_idx)
        #indeks_klucza= alfabet.index(len(do_zakodowania[:i])%len(klucz))
        indeks_klucza = alfabet.index(klucz[i % len(klucz)])
        #print(indeks_klucza)
        nowa_litera_idx = (litera_idx + indeks_klucza) % 26
        nowa_litera = alfabet[nowa_litera_idx]
        wynik += nowa_litera

    zapisPliku(wynik)



vigenere_cipher("dozakodowania.txt")

