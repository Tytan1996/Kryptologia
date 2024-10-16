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
    
def zapisPliku(tekstSzyfrowany, nazwaPliku): #funkcja Maćka
    #nazwaPliku=input("Podaj nazwe pliku do zapisu (bez .txt): \nNazwa pliku: ")
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

def sprawdzenie_zgodnosci_tekstu(nazwa):
    print("podaj teraz plik orginalny aby sprawdzić zgodność")
    org = wczytajPlik()
    plik=open(nazwa+".txt","r", encoding="utf-8")  
    odkodowany=plik.read()
    plik.close()
    org = usunZnaki(org)
    odkodowany = usunZnaki(odkodowany)
    #print(org)
    #print(odkodowany)
    ilosc_znakow = len (org)
    zgodne_znaki = 0
    for i in range(ilosc_znakow):
        if org[i]==odkodowany[i]:
            zgodne_znaki+=1
        else:
            continue
    print(f"ilość znaków które się zgadzają: {zgodne_znaki} / {ilosc_znakow}")


def odkodowanie():
    alfabet_maly="abcdefghijklmnopqrstuvwxyz"
    alfabet_duzy="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    znakiPlMale="ąćęłńóśżź"
    znakiPlDuze="ĄĆĘŁŃÓŚŻŹ"
    znakiDeMale="äüöß"
    znakiDeDuze="ÄÜÖ"
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
        elif i.isdigit():
            odkodowany_tekst += str((int(i) - klucz) % 10)
            
        elif '가' <= i <= '힣':
            odkodowany_tekst+=chr(ord('가')+(ord(i) - ord('가') -klucz) % (ord('힣') - ord('가') + 1))
        elif 'ㄱ' <= i <= 'ㅣ':
            odkodowany_tekst+=chr(ord('ㄱ')+(ord(i) - ord('ㄱ') - klucz) % (ord('ㅣ') - ord('ㄱ') + 1))

            
        else:
            odkodowany_tekst+=i
    nazwaPliku=input("Podaj nazwe pliku do zapisu (bez .txt): \nNazwa pliku: ")
    zapisPliku(odkodowany_tekst, nazwaPliku)
    sprawdzenie_zgodnosci_tekstu(nazwaPliku)



odkodowanie()
