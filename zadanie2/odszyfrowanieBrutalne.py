def odszyfrowanieBrutalne(tekst):
    dlugoscTekstu=range(len(tekst))
    odkodowany=""
    doSprawdzenia=""
    
    for klucz in range(1,26):
        print(klucz)
        for i in dlugoscTekstu:
            if tekst[i].isupper():
                odkodowany+=chr((ord(tekst[i])-65+klucz)%26+65)
            else:
                odkodowany+=tekst[i]
        doSprawdzenia=odkodowany.replace(" ","")
        for i in range(len(polskie)):
            znalezono=doSprawdzenia.find(polskie[i])
            if znalezono==True:
                zapisPliku(odkodowany,"polskie")
        for i in range(len(angielskie)):
            znalezono=doSprawdzenia.find(angielskie[i])
            if znalezono==True:
                zapisPliku(odkodowany,"odszyfrowane")
        zapisPliku(odkodowany,"gotowe\\"+str(klucz))
        odkodowany=""
    return odkodowany
def wczytajPlik(nazwaPliku):
    try:
        Plik=open(nazwaPliku+".txt","r", encoding="utf-8")
        tekst=Plik.read()
        Plik.close()
        return tekst
    except:
        print("Nie istnieje plik, podaj poprawna nazwe.")
polskie=["byc","na","do", "ze","jak","ale","juz","jeszcze",
         "moze", "kiedy", "pan"]
angielskie=["the","be","have","about","after","all","also",
            "and", "ask","back", "because", "become", "begin",
            "between", "but", "come"]
def zapisPliku(tekst,nazwa):
    plik=open(nazwa+".txt",'w', encoding="utf-8")
    plik.write(tekst)
    plik.close()
def Main():
    tekst=wczytajPlik("zaszyfrowane\\2")
    odszyfrowanieBrutalne(tekst)
    print("koniec")
Main()
