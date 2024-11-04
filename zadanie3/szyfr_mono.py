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
ang_trigrams = ['the', 'and', 'tha', 'ent', 'ion', 'tio', 'for', 'nde']

#skoro podejrzewam, że to angielski to dodam jeszcze najpopularniejsze dwójki i powtórki 
ang_digraphs = ['th', 'er', 'on', 'an', 're', 'he', 'in', 'ed']
ang_doubles = ['ss', 'ee', 'tt', 'ff', 'll', 'mm', 'oo']

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

    sorted_trigrams = sorted(repeated_trigrams, key=lambda x: x[1], reverse=True)

    print('najczęsciej występujące trójki w tekscie: ', sorted_trigrams[:8])
    if mniejsza_roznca_ang>mniejsza_roznca_pl:
        print('trojki angielskie: ', ang_trigrams)
    elif mniejsza_roznca_pl>mniejsza_roznca_ang:
        print('trojki polskie: ', pl_trigrams)

    digram_counts = {} #słownik ze znalezionymi dwuznakami 
    for i in range(len(tekst) - 1):
        digram = tekst[i:i+2]
        digram_counts[digram] = digram_counts.get(digram, 0) + 1
    
    repeated_digrams = [(digram, count) for digram, count in digram_counts.items() if count > 1]

    sorted_digrams = sorted(repeated_digrams, key=lambda x: x[1], reverse=True)

    print('najczęściej wystęujące dwójki w tekscie: ', sorted_digrams[:8])
    print('angielskie dwójki: ',ang_digraphs)

    double_counts = {} #słownik ze znalezionymi dubletami 
   
    for i in range(len(tekst) - 1):
        if tekst[i] == tekst[i + 1]:  
            double = tekst[i] * 2
            double_counts[double] = double_counts.get(double, 0) + 1

    repeated_doubles = [(double, count) for double, count in double_counts.items() if count > 1]
    sorted_doubles = sorted(repeated_doubles, key=lambda x: x[1], reverse=True)

    print('najczęściej występujące powtórzone znaki w tekście:', sorted_doubles[:8])
    print('angielskie powtórzenia:', ang_doubles)

odkodowanie()

# szyfr - odkodowana litera
# A - e
# M - t
# W - a
# X - o - prawdopodobnie
# O - i - prawdopodobnie 
# D - h
#AY - podejrzewam ze to er bo jest tez YA co odpowiada re 
# Y - r
# jezeli y to r, to podejrzewam, że IEY to może byc 'for'
# wtedy:
# I - f
# E - o    
#po dubletach
# N - s
# H - l - prawdopodobnie

odkodowane_litery={'A': 'e', 'M': 't', 'W': 'a', 'X': 'o', 'O': 'i', 'D': 'h', 'Y': 'r', 'I': 'f', 'E': 'o', 'N': 's', 'H': 'l'} 

def zapisPliku(tekstOdkodowany):
    plik=open("tekst2_czesciowo_odkodowany.txt",'w', encoding="utf-8")
    plik.write(tekstOdkodowany)
    plik.close()


def czesciowe_odkodowanie():
    tekst = wczytajPlik("tekst2")
    odkodowany_tekst = ""
    for litera in tekst:
        if litera in odkodowane_litery:
            odkodowany_tekst += odkodowane_litery[litera]
        else:
            odkodowany_tekst += litera 
    zapisPliku(odkodowany_tekst)



#czesciowe_odkodowanie()

# tekscie jest dużo 'Je'