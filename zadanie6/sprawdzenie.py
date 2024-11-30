# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 15:23:03 2024

@author: 48513
"""
from random import randrange
import seaborn as sns
import matplotlib.pyplot as plt
import pierwsze as prime



def RandomNumbers_test(test, zakres, ilosc):
    pierwsze= prime.liczby_pierwsze(ilosc//4, zakres[0], zakres[1])
    liczby=pierwsze.copy()
    while len(liczby)<ilosc:
        l=randrange(zakres[0], zakres[1]+1,1)
        if l not in liczby:
            liczby.append(l)
            if prime.pierwsza(l):
                pierwsze.append(l)
    
    confusion_matrix={"TP":0, "FP":0, "FN":0, "TN": 0}
    t=0
    for l in liczby:
        wynik, czas=test(l,s= 9)
        t+=czas
        if wynik and l not in pierwsze:
            confusion_matrix["FP"]+=1
        elif not wynik and l in pierwsze:
            confusion_matrix["FN"]+=1
        elif wynik and l in pierwsze:
            confusion_matrix["TP"]+=1
        elif not wynik and l not in pierwsze:
            confusion_matrix["TN"]+=1
            
    return confusion_matrix, t/ilosc

def NumberList_test(test, liczby):
    #sprawdzanie które są pierwsze
    pierwsze=[l for l in liczby if prime.pierwsza(l)]
    
    confusion_matrix={"TP":0, "FP":0, "FN":0, "TN": 0}
    t=0
    for l in liczby:
        wynik, czas=test(l, s=9)
        t+=czas
        if wynik and l not in pierwsze:
            confusion_matrix["FP"]+=1
        elif not wynik and l in pierwsze:
            confusion_matrix["FN"]+=1
        elif wynik and l in pierwsze:
            confusion_matrix["TP"]+=1
        elif not wynik and l not in pierwsze:
            confusion_matrix["TN"]+=1
            
    return confusion_matrix, t/len(liczby)



def plot_confusion_matrix(conf_matrix, test_name):
    plt.figure(figsize=(8,6))
    conf_matrix=[[conf_matrix['TP'], conf_matrix['FN']], [conf_matrix['FP'], conf_matrix['TN']]]
    sns.heatmap(conf_matrix, annot=True, fmt='d',
                cmap='plasma', cbar=False,
                xticklabels=['Positive', 'Negative'],
                yticklabels=['Positive', 'Negative'])
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title(f'Prime Numbers - {test_name}')
    plt.show()
    
    
