from CBC import *
from krypto import *

def szyfrowanie():
    tekst, klucz = wczytajPlik("tekst_do_zaszyfrowania.txt")
    print('tekst do szyfru: ', tekst)
    tekstWBitach = zamianaNaBity(tekst)
    bloki = dzielenieNaBloki(tekstWBitach)
    print('telst w bitach', bloki)
    IV = "1101011100111011001100100101110011001011110011100101011101111000"
    perm = 9
    zaszyfrowaneBloki = CBC(bloki, klucz, IV, perm, mode="szyfr") 
    print("Zaszyfrowane bloki: ", zaszyfrowaneBloki)
    zaszyfrowanyTekstWBitach = połaczenieBloków(zaszyfrowaneBloki)
    zaszyfrowanyTekst = zamianaNaTekst(zaszyfrowanyTekstWBitach)
    print('zaszyfrowanyTekst', zaszyfrowanyTekst)
    zapisPliku(zaszyfrowanyTekst, klucz, "zaszyfrowany_plik")

def deszyfrowanie():
    zaszyfrowanyTekst, klucz = wczytajPlik("zaszyfrowany_plik.txt")
    print('zaszyfrowany tekst:', zaszyfrowanyTekst)
    zaszyfrowaneBity = zamianaNaBity(zaszyfrowanyTekst)
    blokiZaszyfrowane = dzielenieNaBloki(zaszyfrowaneBity)
    print("Bloki zaszyfrowane: ", blokiZaszyfrowane)
    odszyfrowaneBloki = []
    IV = "1101011100111011001100100101110011001011110011100101011101111000"  
    perm = 9
    odszyfrowaneBloki_str = ''.join(CBC(blokiZaszyfrowane, klucz, IV, perm, mode="deszyfr"))
    odszyfrowaneBloki.append(odszyfrowaneBloki_str)
    print("Odszyfrowane bloki str: ", odszyfrowaneBloki)
    odszyfrowaneBity = połaczenieBloków(odszyfrowaneBloki)
    odszyfrowanyTekst = zamianaNaTekst(odszyfrowaneBity)
    print('odszyfrowany tekst:', odszyfrowanyTekst)
    zapisPliku(odszyfrowanyTekst, klucz, "odszyfrowany_plik")



szyfrowanie()
deszyfrowanie()