from CBC import *
from krypto import *

def szyfrowanie(tekst, klucz):
    tekstWBitach = zamianaNaBity(tekst)
    bloki = dzielenieNaBloki(tekstWBitach)
    IV = "1101011100111011001100100101110011001011110011100101011101111000"
    perm = 9
    zaszyfrowaneBloki = CBC(bloki, klucz, IV, perm, mode="szyfr") 
    zaszyfrowanyTekstWBitach = połaczenieBloków(zaszyfrowaneBloki)
    #zaszyfrowanyTekst = zamianaNaTekst(zaszyfrowanyTekstWBitach)
    zapisPliku(zaszyfrowanyTekstWBitach, klucz, "zaszyfrowany_plik")
    return zaszyfrowanyTekstWBitach

def deszyfrowanie(tekst, klucz):
    zaszyfrowanyTekst, klucz = wczytajPlik("zaszyfrowany_plik.txt")
    print('zaszyfrowany tekst:', zaszyfrowanyTekst)
    #zaszyfrowaneBity = zamianaNaBity(zaszyfrowanyTekst)
    blokiZaszyfrowane = dzielenieNaBloki(zaszyfrowanyTekst)
    ##print("Bloki zaszyfrowane: ", blokiZaszyfrowane)
    odszyfrowaneBloki = []
    IV = "1101011100111011001100100101110011001011110011100101011101111000"  
    perm = 9
    odszyfrowaneBloki_str = ''.join(CBC(blokiZaszyfrowane, klucz, IV, perm, mode="deszyfr"))
    odszyfrowaneBloki.append(odszyfrowaneBloki_str)
    odszyfrowaneBity = połaczenieBloków(odszyfrowaneBloki)
    odszyfrowanyTekst = zamianaNaTekst(odszyfrowaneBity)
    zapisPliku(odszyfrowanyTekst, klucz, "odszyfrowany_plik")
    return odszyfrowanyTekst



szyfrowanie()
deszyfrowanie()


def zapisPliku(tekstSzyfrowany, klucz, nazwa):
    with open(f"{nazwa}.txt", 'w', encoding="utf-8") as plik:
        # Zapisz klucz w pierwszej linii
        #plik.write(f"klucz {klucz}\n")
        # Zapisz zaszyfrowany tekst poniżej
        plik.write(tekstSzyfrowany)