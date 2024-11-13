# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 21:30:40 2024

@author: maria
"""
from szyfrowanie import vigenere_cipher2, wczytajPlik
from odszyfrowanie import vigenere_decipher, zapisPliku

def interfejs():
    nazwa_pliku= input("Podaj nazwę pliku (.txt) do wczytania: ")
    if nazwa_pliku[-4:]!='.txt':
        nazwa_pliku+='.txt'
        
    dane=wczytajPlik(nazwa_pliku)
    if len(dane)!=2:
        while True:
            opcja=input("By zaszyfrować tekst wprowadź: 1,\nBy odszyfrować wprowadź: 2\n")
            if opcja in ['1', '2']:
                break
            else:
                print('Wybrano złą opcję, spróbuj jeszcze raz.')
        klucz=input("Podaj klucz: ")
        tekst=dane
    else:
        tekst, klucz = dane
        opcja='1'
      
    print("Wybierz, co uwzględnić:\n1. polskie litery,\n2. spacje,\n3. cyfry\n\nnp. by wybrać wszystkie opcje wpisz: 123")
    kod=['0']*3
    try:
        opcje=input()
        for i in range(len(opcje)):
            kod[int(opcje[i])-1]='1'
        
    except:
        print('Wprowadzono złe wartosci, szyfrowanie bez dodatkowych opcji')
    if opcja=='1':
        wynik=vigenere_cipher2(tekst, klucz, int(kod[0]), int(kod[1]), int(kod[2]))
        
    elif opcja=='2':
        kod=''.join(kod)
        wynik=vigenere_decipher(tekst, klucz, kod)
    
    nazwa = input('Podaj nazwę pliku do zapisu: ')
    zapisPliku(wynik, nazwa)
    
    print('Zapisano')
    
interfejs()