#napisać kod który będzie odszyfrowywał zaszyfrowane pliki znając klucz i będzie porównywał zgodność pliku zaszyfrowanego i rozszyfrowanego 

def wczytajPlik():   #funkcja Maćka
    nazwaPliku=input("Wprowadz nazwe pliku , bez .txt\nNazwa pliku: ")
    try:
        Plik=open(nazwaPliku+".txt","r", encoding="utf-8")
        tekst=Plik.read()
        Plik.close()
        return tekst
    except:
        print("Nie istnieje plik, podaj poprawna nazwe.")
        return wczytajPlik()
    
def zapisPliku(tekstSzyfrowany): #funkcja Maćka
    nazwaPliku=input("Podaj nazwe pliku do zapisu (bez .txt): \nNazwa pliku: ")
    plik=open(nazwaPliku+".txt",'w', encoding="utf-8")
    plik.write(tekstSzyfrowany)
    plik.close()

def usunCyfry(tekst): #funkcja Maćka
    cyfry="0123456789"
    b=range(len(cyfry))
    for i in b:
        tekst=tekst.replace(cyfry[i],"")
    return tekst

def usunZnaki(tekst): #funkcja Maćka
    symbole=" .,'!:;/@#$%^&(*)-_+=[{]}|?\n\""
    b=range(len(symbole))
    for i in b:
        tekst=tekst.replace(symbole[i],"")
    return tekst

def usunPolskieZnaki(tekst): #funkcja Maćka
    znakiPl="ąęółżźćń"
    znaki="aeolzzcn"
    b=range(len(znaki))
    for i in b:
        tekst=tekst.replace(znakiPl[i],znaki[i]) 
    return tekst

def sprawdzenie_zgodnosci_tekstu():
    print("podaj teraz plik orginalny aby sprawdzić zgodność")
    org = wczytajPlik()
    plik=open("odkodowane_pl.txt","r", encoding="utf-8")  #WAŻNE!!!!! TU ZMIENIAMY KTORY ODKODOWANY PLIK BIERZEMY 
    odkodowany=plik.read()
    plik.close()
    #org = org.lower()
    org = usunZnaki(org)
    org = usunCyfry(org)
    #org = usunPolskieZnaki(org)
    odkodowany = usunZnaki(odkodowany)
    print(org)
    print(odkodowany)
    ilosc_znakow = len (org)
    zgodne_znaki = 0
    for i in range(ilosc_znakow):
        if org[i]==odkodowany[i]:
            zgodne_znaki+=1
        else:
            continue
    print(f"ilość znaków które się zgadzają: {zgodne_znaki} / {ilosc_znakow}")

#sprawdzam_pl - tekst z polskimi znakami
#sprawdzam_bezpl - tekst bez polskich znaków

#koniec_pl - zakodowany tekst z polskimi znakami (kod Maćka)
#koniec_bezpl - zakodowany tekst bez polskich znaków

#odkodowane_pl - odkodowany tekst w którym NA POCZĄTKU BYŁY polskie znaki
#odkodowane_bezpl - odkodowany tekst w którym nie było polskich znaków :)

#WAŻNE!!!!! ODKODOWANY PLIK DO SPRAWDZENIA (CZY PL CZY BEZPL) NARAZIE TRZEBA ZMIENIC W FUNKCJI SPRAWDZANIE_ZGODNOSCI_TEKSTU


def odkodowanie():
    alfabet_maly="abcdefghijklmnopqrstuvwxyz"
    alfabet_duzy="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    znakiPlMale="ąęółżźćńś"
    znakiPlDuze="ĄĘÓŁŻŹĆŃŚ"
    znakiDeMale="äöüß"
    znakiDeDuze="ÄÖÜ"
    print("podaj nazwę pliku z zakodowanym tekstem ")
    tekst = wczytajPlik()
    odkodowany_tekst=""
    klucz = int(input("Podaj klucz szyfrowania: "))
    for i in tekst:
        if i in alfabet_maly:
            odkodowany_tekst+=alfabet_maly[(alfabet_maly.index(i)-klucz)%len(alfabet_maly)]
        elif i in alfabet_duzy:
            odkodowany_tekst+=alfabet_duzy[(alfabet_duzy.index(i)-klucz)%len(alfabet_duzy)]
        elif i in znakiPlMale:
            odkodowany_tekst+=znakiPlMale[(znakiPlMale.index(i)-klucz)%len(znakiPlMale)]
        elif i in znakiPlDuze:
            odkodowany_tekst+=znakiPlDuze[(znakiPlDuze.index(i)-klucz)%len(znakiPlDuze)]
        elif i in znakiDeMale:
            odkodowany_tekst+=znakiDeMale[(znakiDeMale.index(i)-klucz)%len(znakiDeMale)]
        elif i in znakiDeDuze:
            odkodowany_tekst+=znakiDeDuze[(znakiDeDuze.index(i)-klucz)%len(znakiDeDuze)]
        else:
            odkodowany_tekst+=i
    zapisPliku(odkodowany_tekst)
    sprawdzenie_zgodnosci_tekstu()

odkodowanie()












