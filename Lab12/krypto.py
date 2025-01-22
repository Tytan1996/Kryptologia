
def wczytajPlik(nazwa_pliku):
    try:
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
    except FileNotFoundError:
        print("Nie istnieje plik, podaj poprawną nazwę.")
        raise FileNotFoundError()

slowo="Ala ma kota, ale kot nie ma Ali"
def zamianaNaBity(tekst):
    tablicaBitow=[]
    for i in range(len(tekst)):
        Asci=ord(tekst[i])
        Bin=bin(Asci)[2:]
        pom=Bin.zfill(7)
        if pom.count('1')%2:
            tablicaBitow.append(pom+'0')
        else:
            tablicaBitow.append(pom+'1')
    #polaczenieBitow
    tekstWBitach =""

    for i in range(len(tablicaBitow)):
        tekstWBitach+=tablicaBitow[i]
    return tekstWBitach


def dzielenieNaBloki(tekstWBitach):
    bloki=[]
    for i in range(0,len(tekstWBitach),64):
        bloki.append(tekstWBitach[i:i+64])
    if len(bloki[-1])<64:
        bloki[-1]+='1'*(64 - len(bloki[-1]))
    
    return bloki;


def połaczenieBloków(Bloki):
    tekst=""
    for i in range(len(Bloki)):
        tekst+=Bloki[i]
        
    return tekst
def zamianaNaTekst(tekst):
    znaki = []
    
    # Podział na 8-bitowe segmenty
    for i in range(0, len(tekst), 8):
        segment = tekst[i:i+8]
        
        # Usuń bit parzystości (ostatni bit)
        if len(segment) == 8:
            segment_bez_parzystości = segment[:-1]  # Usuń ostatni bit
            
            # Zamiana na znak ASCII
            znak = chr(int(segment_bez_parzystości, 2))
            znaki.append(znak)
    
    # Połączenie znaków w tekst
    tekst = ''.join(znaki)
    return tekst
'''
def zapisPliku(tekstSzyfrowany, nazwa):
    plik=open(f"{nazwa}.txt",'w', encoding="utf-8")
    plik.write(tekstSzyfrowany)
    plik.close()
'''
def zapisPliku(tekstSzyfrowany, klucz, nazwa):
    with open(f"{nazwa}.txt", 'w', encoding="utf-8") as plik:
        # Zapisz klucz w pierwszej linii
        plik.write(f"klucz {klucz}\n")
        # Zapisz zaszyfrowany tekst poniżej
        plik.write(tekstSzyfrowany)
tekst=zamianaNaBity(slowo)
bloki=dzielenieNaBloki(tekst)
calyTekst=połaczenieBloków(bloki)
calyTekst1=zamianaNaTekst(calyTekst)
#print(calyTekst1)


