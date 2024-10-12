# coding: utf-8
import re
import inspect

def czyBedaLiczby():
    czyLiczba= input("Czy usunac liczby w teksie syfrowanym? [t/n]\nOdpowiedz: ")
    if czyLiczba=='t':
        return True
    elif czyLiczba=='n':
        return False
    else:
        print("Prowadz poprawna odpowiedz")
        return czyBedaLiczby()
def czyDuzeLitery():
    czyLiczba= input("Czy zakodowac w malych literach? [t/n]\nOdpowiedz: ")
    if czyLiczba=='t':
        return True
    elif czyLiczba=='n':
        return False
    else:
        print("Prowadz poprawna odpowiedz")
        return czyDuzeLitery()
def wyborJezyka():
    try:
        jezyk=int(input("Wybierz jezyk:\n1 - Polski,\n2 - Niemiecki,\n3 - Angielski,\n4 - Korerański\nTwoja opcja: "))
        if jezyk in range(1,4):
            return jezyk
        else:
            print("prowadz poprawny wybor")
            return wyborJezyka()
    except ValueError:
        print("Wporwadz liczbe, a nie tekst")
        return wyborJezyka()
def czyUsunacPolskieZnaki():
    czyBedaPolskieZnaki= input("Czy usunac polskie/niemieckie litery? [t/n]\nTwoja odpowiedz: ")
    if czyBedaPolskieZnaki == 't':
       return True
    elif czyBedaPolskieZnaki =='n':
        return False
    else:
        print ("Porwadz poprawna odpowiedz")
        return czyUsunacPolskieZnaki();
def wczytajPlik():
    nazwaPliku=input("Wprowadz nazwe pliku, bez .txt\nNazwa pliku: ")
    try:
        Plik=open(nazwaPliku+".txt","r", encoding="utf-8")
        tekst=Plik.read()
        Plik.close()
        # Definiowanie wzorca do wyszukiwania
        wzorzec = r'Jezyk:\s*(\w+),\s*Polskie/Niemieckie\s*litery:\s*(True|False),\s*liczby:\s*(True|False),\s*małe\s*litery:\s*(True|False)'
        # Wyszukiwanie w tekście
        if re.search(wzorzec, tekst):
            wynik=re.search(wzorzec, tekst)
            if wynik:
                jezyk = wynik.group(1)  # Wartość języka
                polskie_niemieckie = wynik.group(2)  # Polskie/Niemieckie litery
                liczby = wynik.group(3)  # Liczby
                male_litery = wynik.group(4)  # Małe litery
                wiersze = tekst.splitlines()  # Podziel tekst na wiersze
                wiersze.pop(0)  # Usuń pierwszy wiersz
                tekst = "\n".join(wiersze)  # Połącz pozostałe wiersze
            return tekst,jezyk,polskie_niemieckie,liczby,male_litery
        else:
            print("Nie znaleziono danych do kodowanaia tekstu lub je zle napisano.")
        return tekst
    except:
        print("Nie istnieje plik, podaj poprawna nazwe.")
        return wczytajPlik()
def usunCyfry(tekst):
    cyfry="0123456789"
    b=range(len(cyfry))
    for i in b:
        tekst=tekst.replace(cyfry[i],"")
    return tekst
def usunZnaki(tekst):
    symbole=" .,'!:;/@#$%^&(*)-_+=[{]}|?\n\""
    b=range(len(symbole))
    for i in b:
        tekst=tekst.replace(symbole[i],"")
    return tekst
def usunPolskieZnaki(tekst,jezyk):
    znakiPl="ąęółżźćńĄĘÓŁŻŹĆŃ"
    znaki="aeolzzcnAEOLZZCN"
    znakiDe="äöüßÄÖÜ"
    znaki2="aouBAOU"
    if jezyk==1:
        for i in range(len(znaki)):
            tekst=tekst.replace(znakiPl[i],znaki[i])
    elif jezyk==2:
        for i in range(len(znaki2)):
            tekst=tekst.replace(znakiDe[i],znaki[i])
    return tekst

def przeksztalcenie(tekst,tekst2):
    dlugoscTekstu=range(len(tekst))
    table=""
    k=0
    for i in dlugoscTekstu:
        if i%5==0 and i!=0 and i%35 !=0:
            k+=1
            tekst2=tekst2+" "
        if i%35==0 and i!=0:
            k+=1
            tekst2=tekst2+'\n'
        tekst2=tekst2+tekst[i]
    return tekst2
def szyfrowanie(tekst,jezyk):
    znakiPlMale=[]
    znakiPlMale += ['ą', 'ę', 'ó', 'ł', 'ż', 'ź', 'ć', 'ń']
    znakiPlDuze =[znak.upper() for znak in znakiPlMale]
    znakiDeMale = []
    znakiDeMale +=['ä', 'ö', 'ü', 'ß']
    znakiDeDuze = []
    znakiDeDuze +=['Ä', 'Ö', 'Ü']
    klucz=5
    dlugoscTekstu=range(len(tekst))
    znakiPl="ąęółżźćń"
    szyfr=""
    for i in dlugoscTekstu:
        if tekst[i].isalpha():
            if tekst[i].islower():
                if tekst[i] in znakiPlMale and jezyk==1:
                    numerPl=znakiPlMale.index(tekst[i])
                    szyfr+=znakiPlMale[(numerPl+klucz)%len(znakiPlMale)]
                elif tekst[i] in znakiDeMale and jezyk==2:
                    numerDe=znakiDeMale.index(tekst[i])
                    szyfr+=znakiDeMale[(numerDe+klucz)%len(znakiDeMale)]
                else:
                    szyfr+=chr((ord(tekst[i])-97+klucz)%26+97)
            elif tekst[i].isupper():
                if tekst[i] in znakiPlDuze and jezyk==1:
                    numerPl=znakiPlDuze.index(tekst[i])
                    szyfr+=znakiPlDuze[(numerPl+klucz)%len(znakiPlDuze)]
                elif tekst[i] in znakiDeMale and jezyk==2:
                    numerDe=znakiDeDuze.index(tekst[i])
                    szyfr+=znakiDeDuze[(numerDe+klucz)%len(znakiDeDuze)]
                else:
                    szyfr+=chr((ord(tekst[i])-65+klucz)%26+65)
        elif tekst[i].isdigit():
            szyfr+=str((int(tekst[i])+klucz)%10)
        else:
            szyfr+=tekst[i]
    return szyfr
def zapisPliku(tekstSzyfrowany):
    nazwaPliku=input("Podaj nazwe pliku do zapisu (bez .txt): \nNazwa pliku: ")
    plik=open(nazwaPliku+".txt",'w', encoding="utf-8")
    plik.write(tekstSzyfrowany)
    plik.close()
def Menu():
    tekst=""
    tekstPrzeksztalcony=""
    instrukcja=""
    liniaTekstu=""
    tekstSzyfrowany=""
    wyniki = wczytajPlik()
    if len(wyniki)==5:
        tekst=wyniki[0]
        jezyk=wyniki[1]
        polskie_niemieckie=wyniki[2]
        liczby=wyniki[3]
        maleLitery=wyniki[4]
        print(f"Język: {jezyk}")
        print(f"Polskie/Niemieckie litery: {polskie_niemieckie}")
        print(f"Liczby: {liczby}")
        print(f"Małe litery: {maleLitery}")
        if jezyk=="Pl":
            jezyk=1
        elif jezyk=="Ang":
            jezyk=3
        elif jezyk=="De":
            jezyk=2
        elif jezyk=="Ko":
            jezyk=4
        else:
            jezyk==None
    else:
        tekst=wyniki;
        jezyk=None
        polskie_niemieckie=None
        liczby=None
        maleLitery=None
    # Sprawdź, czy język jest None
    if jezyk is None:
        jezyk = wyborJezyka()

    # Usuń cyfry, jeśli jest to konieczne
    if (jezyk is None and czyBedaLiczby()) or (liczby is False):
        tekst = usunCyfry(tekst)

    # Usuń polskie znaki, jeśli jest to konieczne
    if (jezyk is None and czyUsunacPolskieZnaki()) or (polskie_niemieckie is False):
        tekst = usunPolskieZnaki(tekst, jezyk)

    # Zamień na małe litery, jeśli jest to konieczne
    if (jezyk is None and czyDuzeLitery()) or (maleLitery is False):
        tekst = tekst.lower()  
    
    tekst=usunZnaki(tekst)    
    tekstPrzeksztalcony=przeksztalcenie(tekst,tekstPrzeksztalcony)
    tekstSzyfrowany=szyfrowanie(tekstPrzeksztalcony,jezyk)
    zapisPliku(tekstSzyfrowany)
    print("udalo sie.\nKoncze dzialanie programu!")


Menu()

       



    
