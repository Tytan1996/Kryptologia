import time

def odszyfrowanieBrutalne(tekst,numer):
    dlugoscTekstu=range(len(tekst))
    odkodowany=""
    doSprawdzenia=""
    tekst=tekst.lower()
    for klucz in range(1,26):
        for i in dlugoscTekstu:
            if tekst[i].islower():
                odkodowany+=chr((ord(tekst[i])-97-klucz)%26+97)
            else:
                odkodowany+=tekst[i]
        doSprawdzenia=odkodowany.replace(" ","")
        for i in range(len(polskie)):
            if polskie[i] in doSprawdzenia:
                zapisPliku(odkodowany,"odszyfrowane/odszyfrowanePL_klucz"+str(klucz)+"_tekst"+str(numer))
                return
        for i in range(len(angielskie)):
            if angielskie[i] in doSprawdzenia:
                zapisPliku(odkodowany,"odszyfrowane/odszyfrowaneENG_klucz"+str(klucz)+"_tekst"+str(numer))
                return
        odkodowany=""
    return odkodowany
def wczytajPlik(nazwaPliku):
    try:
        Plik=open(nazwaPliku+".txt","r", encoding="utf-8")
        tekst=Plik.read()
        Plik.close()
        return tekst
    except FileNotFoundError:
        raise FileNotFoundError(f"Nie istnieje plik {nazwaPliku}.txt, podaj poprawna nazwe.")
polskie=["jeszcze","kiedy","teraz","prawda"]
angielskie=["about","because", "become", "begin",
            "between"]
def zapisPliku(tekst,nazwa):
    plik=open(nazwa+".txt",'w', encoding="utf-8")
    plik.write(tekst)
    plik.close()
def Main():
    czasy=[]
    for i in range(1,9):
        try:
            tekst=wczytajPlik("zaszyfrowane\\"+str(i))
        except FileNotFoundError as e:
            print(e)
            return
        suma=0
        for j in range(0,50):
            poczatek = time.time()
            odszyfrowanieBrutalne(tekst,i)
            koniec = time.time()
            suma+=(koniec-poczatek)
        czas=suma/50
        czasy.append(czas)
        suma=0
    print("koniec")
    return czasy
Main()
