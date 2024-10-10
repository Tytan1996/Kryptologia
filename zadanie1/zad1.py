# coding: utf-8


def czyBedaLiczby():
    czyLiczba= input("Czy usunac liczby w teksie syfrowanym? [t/n]\nOdpowiedz: ")
    if czyLiczba=='t':
        return True
    elif czyLiczba=='n':
        return False
    else:
        print("Prowadz poprawna odpowiedz")
        return czyBedaLiczby()

def wyborJezyka():
    try:
        jezyk=int(input("1 - Polski, 2 - Angieslski....\nTwoja opcja: "))
        if jezyk in [1,2]:
            return jezyk
        else:
            print("prowadz poprawny wybor")
            return wyborJezyka()
    except ValueError:
        print("Wporwadz liczbe, a nie tekst")
        return wyborJezyka()
def czyUsunacPolskieZnaki():
    czyBedaPolskieZnaki= input("Czy usunac polskie znaki? [t/n]\nTwoja odpowiedz: ")
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
        return tekst
    except:
        print("Nie istnieje plik, podaj poprawna nazwe.")
        return wczytajPlik()
def wczytanieInstrukcji():
    try:
        Plik=open("instrukcja.txt","r")
        tekst=Plik.read()
        Plik.close()
        print(tekst)
        return tekst
    except:
        print("Nie ma pliku instrukcja.txt")
        return wczytanieInstrukcji()
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
def usunPolskieZnaki(tekst):
    znakiPl="ąęółżźćń"
    znaki="aeolzzcn"
    b=range(len(znaki))
    for i in b:
        tekst=tekst.replace(znakiPl[i],znaki[i]) 
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
def szyfrowanie(tekst):
    klucz=5
    dlugoscTekstu=range(len(tekst))
    szyfr=""
    for i in dlugoscTekstu:
        if tekst[i].isalpha():
            szyfr+=chr((ord(tekst[i])-97+klucz)%26+97)
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
    instrukcja=wczytanieInstrukcji()
    tekstSzyfrowany=""
    #jezyk=wyborJezyka()
    tekst=wczytajPlik()
    tekst=tekst.lower() # zamienia na male literki
    tekst=usunZnaki(tekst)
    if(czyBedaLiczby()==True):
        tekst=usunCyfry(tekst)
    if(czyUsunacPolskieZnaki()==True):
        tekst=usunPolskieZnaki(tekst)
    tekstPrzeksztalcony=przeksztalcenie(tekst,tekstPrzeksztalcony)
    tekstSzyfrowany=szyfrowanie(tekstPrzeksztalcony)
    zapisPliku(tekstSzyfrowany)
    print("udalo sie.\nKoncze dzialanie programu!")


Menu()

       



    
