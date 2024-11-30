# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 15:23:03 2024

@author: 48513
"""
from random import randrange
import seaborn as sns
import matplotlib.pyplot as plt


def RandomNumbers_test(test, zakres, ilosc):
    liczby=[]
    for i in range(ilosc):
        liczby.append(randrange(zakres[0], zakres[1], 1))
    #Jesli pierwsze bedzie zawierać wszystkie liczby z zakresu
    pierwsze=[]
    pierwsze=set(pierwsze).intersection(set(liczby))
    
    confusion_matrix={"TP":0, "FP":0, "FN":0, "TN": 0}
    t=0
    for l in liczby:
        wynik, czas=test(l)
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
    pierwsze=[]
    
    confusion_matrix={"TP":0, "FP":0, "FN":0, "TN": 0}
    t=0
    for l in liczby:
        wynik, czas=test(l)
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
    
    
