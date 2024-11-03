import pandas as pd

def wczytajPlik(nazwaPliku):
    try:
        Plik=open(nazwaPliku+".txt","r", encoding="utf-8")
        tekst=Plik.read()
        Plik.close()
        return tekst
    except FileNotFoundError:
        raise FileNotFoundError(f"Nie istnieje plik {nazwaPliku}.txt, podaj poprawna nazwe.")
        

def letterFreq(tekst, top):
    litery=list(filter(lambda x: x.isalpha(), list(str(tekst).lower())))
    return pd.Series(litery).value_counts()[0:top]

def letterFreqPercentage(tekst):
    litery = list(filter(lambda x: x.isalpha(), list(str(tekst).lower())))
    freq_series = pd.Series(litery).value_counts(normalize=True) * 100
    return freq_series

polski=['a', 'e', 'o','i', 'z', 'n', 's', 'r', 'w',  # z w
        'c', 't', 'l', 'y', 'k', 'd', 'p', 'm', 'u',
        'j', 'b','g', 'h', 'f', 'q', 'v', 'x'] 

angielski=['e', 't', 'a', 'o', 'n', 'i', 's', 'h','r', # t h
           'd', 'l', 'f', 'c', 'm', 'u', 'g', 'y', 'p',
           'w', 'b', 'v', 'k', 'j', 'x', 'z', 'q']

# Częstotliwości procentowe dla polskiego i angielskiego
polski_freq_proc = {'a': 9.99, 'e': 9.05, 'o': 8.41, 'i': 8.29, 'z': 5.62}
angielski_freq_proc = {'e': 12.7, 't': 9.1, 'a': 8.2, 'o': 7.5, 'i': 7}

pl_trigrams = ['prz', 'nie', 'sie']
ang_trigrams = ['the', 'and', 'tha']

def odkodowanie():
    tekst = wczytajPlik("tekst2")

    freq_percentage = letterFreqPercentage(tekst)
    top_5 = freq_percentage.head(5)
    print(top_5)
    print(top_5[1])

    mniejsza_roznca_pl = 0
    mniejsza_roznca_ang = 0

    for i in range(5):
        p=['a', 'e', 'o', 'i', 'z']
        a=['e', 't', 'a', 'o', 'i']
        lp=p[i]
        la=a[i]
        roznica_pl = abs(top_5[i] - polski_freq_proc[lp])
        roznica_ang = abs(top_5[i] - angielski_freq_proc[la])
        if roznica_pl < roznica_ang:
            mniejsza_roznca_pl += 1
        else:
            mniejsza_roznca_ang += 1

    if mniejsza_roznca_ang>mniejsza_roznca_pl:
        print("prawdopodnie zakodowany tekst jest po angielsku")
        print(top_5)
        print(angielski_freq_proc)
    elif mniejsza_roznca_pl>mniejsza_roznca_ang:
        print("prawdopodobnie zakodowany tekst jest po polsku")
        print(top_5)
        print(polski_freq_proc)

    trigram_counts = {} #słownik ze znalezionymi trojznakami 
    for i in range(len(tekst) - 2):
        trigram = tekst[i:i+3]
        trigram_counts[trigram] = trigram_counts.get(trigram, 0) + 1
    
    repeated_trigrams = [(trigram, count) for trigram, count in trigram_counts.items() if count > 1]

    print(repeated_trigrams[:3])
    if mniejsza_roznca_ang>mniejsza_roznca_pl:
        print('trojki angielskie: ', ang_trigrams)
    elif mniejsza_roznca_pl>mniejsza_roznca_ang:
        print('trojki polskie: ', pl_trigrams)

odkodowanie()



    

    
