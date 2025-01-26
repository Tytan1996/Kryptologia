import cv2 as cv


tekst = "Ala ma kota, kot ma Ale"
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

img=cv.imread('pobrane.jpeg')


wiadomosc="Zaczyname akcje jutro rano!"

def zakodowanieWiadomosciWObrazu(bitowaWiadomosc):
    data_index = 0
    for row in img:
        for pixel in row:
            for color in range(3):  # R, G, B
                if data_index < len(bitowaWiadomosc):
                    if int(bitowaWiadomosc[data_index]) == 1:
                        # Ustaw wartość na najbliższą nieparzystą liczbę
                        pixel[color] = pixel[color] | 1
                    else:
                        # Ustaw wartość na najbliższą parzystą liczbę
                        pixel[color] = pixel[color] & ~1
                    data_index += 1
                else:
                    # Zakończ pętlę, jeśli wiadomość została zakodowana
                    break
            if data_index >= len(bitowaWiadomosc):
                break
        if data_index >= len(bitowaWiadomosc):
            break

    # Zapisz zakodowany obraz do pliku
    cv.imwrite("UkrytaWiadomosc.jpeg", img)
    print("Wiadomosc zostala zapisana")
                    
bity=zamianaNaBity(wiadomosc)
zakodowanieWiadomosciWObrazu(bity) 