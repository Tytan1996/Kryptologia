#
#%% Imports
import sys
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.widgets import CheckButtons
from PyQt5.QtCore import Qt, QStandardPaths
from PyQt5.QtWidgets import QMainWindow,  QMenuBar, QMessageBox,  QApplication,  QVBoxLayout, QGroupBox, QHBoxLayout, QFormLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QAction, QFileDialog, QComboBox, QWidget, QLabel, QMenu, QInputDialog
import pandas as pd
import numpy as np
from pathlib import Path
from CBC import *
from krypto import *



APP_NAME='Plot RfG 0.2'
    
#%% App Windows      
 

class DES:
    def __init__(self, tekst, klucz, mode):
        self.klucz=klucz
        self.mode=mode
        if mode:
            self.tekst=tekst
            self.szyfr=self.szyfrowanie()
        else:
            self.szyfr=tekst
            self.tekst=self.deszyfrowanie()
        
        
    
    def get_params(self):
        IV, klucz =self.klucz[:64], self.klucz[64:]
        perm=self.dziesietny(klucz[:2]+IV[:1]+klucz[-1])
        return klucz,IV,perm
        
    def dziesietny(self, seed):
        l=0
        for i in range(len(seed)):
            l+=int(seed[i])*2**i
            #l+=int(seed[i])*2**(len(seed)-1-i)
        return l
    
    def szyfrowanie(self):
        klucz, IV , perm = self.get_params()
        tekstWBitach = zamianaNaBity(self.tekst)
        bloki = dzielenieNaBloki(tekstWBitach)
        zaszyfrowaneBloki = CBC(bloki, klucz, IV, perm, mode="szyfr") 
        zaszyfrowanyTekstWBitach = połaczenieBloków(zaszyfrowaneBloki)
        #zaszyfrowanyTekst = zamianaNaTekst(zaszyfrowanyTekstWBitach)
        zapisPliku(zaszyfrowanyTekstWBitach, klucz, "zaszyfrowany_plik")
        #print(zaszyfrowanyTekstWBitach)
        return zaszyfrowanyTekstWBitach
    
    def deszyfrowanie(self):
        klucz, IV , perm = self.get_parms()
        #zaszyfrowaneBity = zamianaNaBity(zaszyfrowanyTekst)
        blokiZaszyfrowane = dzielenieNaBloki(self.szyfr)
        ##print("Bloki zaszyfrowane: ", blokiZaszyfrowane)
        odszyfrowaneBloki = []
        odszyfrowaneBloki_str = ''.join(CBC(blokiZaszyfrowane, klucz, IV, perm, mode="deszyfr"))
        odszyfrowaneBloki.append(odszyfrowaneBloki_str)
        odszyfrowaneBity = połaczenieBloków(odszyfrowaneBloki)
        odszyfrowanyTekst = zamianaNaTekst(odszyfrowaneBity)
        return odszyfrowanyTekst

    def zapisPliku(self, nazwa):
        if mode:
            tekst=self.szyfr
        else:
            tekst=self.tekst
        with open(f"{nazwa}.txt", 'w', encoding="utf-8") as plik:
            # Zapisz klucz w pierwszej linii
            #plik.write(f"klucz {klucz}\n")
            # Zapisz zaszyfrowany tekst poniżej
            plik.write(tekst)
       

class MainWindow(QMainWindow):
    def __init__(self,  DES, filepath=None):
        super().__init__()
        #self.main_app=main_app
        self.resize(1280, 900)
        self.setWindowTitle(APP_NAME)
        self.fig = plt.figure(layout='constrained', figsize=(15, 12))
        self.canvas = FigureCanvas(self.fig)
        self.fig.suptitle("DES")
        self.axes=self.fig.subplots(1,2)
        self.DES=DES
        self.path=filepath
        self.show_tekst=True
        self.show_text()
        
        
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Dodanie płótna
        layout.addWidget(self.canvas)

        self.setCentralWidget(central_widget)
        self.showMaximized()
        
    
        
    def show_text(self):
        
        for ax in self.axes:
            ax.clear()
            ax.set_xticks([])
            ax.set_yticks([])
            ax.set_navigate(False)
            
        self.axes[0].set_title("Tekst:")
        self.axes[0].text(0.05, 0.5, self.DES.tekst[:500] if self.show_tekst else "Wyświetlanie wyłączone",
                          wrap=True,
                          horizontalalignment="left", verticalalignment="center", fontsize=10)
    
        self.axes[1].set_title("Szyfr:")
        szyfr_blocks = "\n".join(dzielenieNaBloki(self.DES.szyfr)[:20])
        self.axes[1].text(0.05, 0.5, szyfr_blocks, wrap=True,
                          horizontalalignment="left", verticalalignment="center", fontsize=10)
    
        self.canvas.draw()
        
    
    def zapiszPlik(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Zapisz wykres", self.path,  "Figury (*.txt)")
        if filename:
            self.DES.zapisPliku(filename)
    
    
    
    




class MenuWindow(QWidget):
    def __init__(self, main_app, path=None):
        super().__init__()
        self.main_app = main_app
        self.setWindowTitle(APP_NAME+"-Menu")
        self.resize(450, 300)
        self.layout = QVBoxLayout()
        

        self.info=QLabel('')
        self.info.setFixedSize(400, 10)
        self.info.setVisible(False)
        self.info.setStyleSheet("""
            margin: -10px;  /* Brak zewnętrznych marginesów */
            padding: -10px; /* Brak wewnętrznych odstępów */
            color: red;          /* Kolor tekstu */
            font-size: 10px;      /* Wielkość czcionki */

        """)
        
        self.info.setContentsMargins(-10, -10, -10, -10)
        self.layout.addWidget(self.info)
        # Przycisk wczytywania figury
        self.file1_line = self.create_file_selector("Wczytaj plik", self.wczytaj_plik)
        self.layout.addLayout(self.file1_line)

        self.file2_line = self.create_file_selector("Wczytaj klucz", self.wczytaj_klucz)
        self.layout.addLayout(self.file2_line)



        if not path:
            self.default_path= QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
        else:
            self.default_path=path
            
        
        self.label = QLabel("Szyfrowanie / Odszyfrowywanie:", self)

        # Tworzymy przycisk
        self.toggle_button = QPushButton("Szyfrowanie", self)
        self.toggle_button.setCheckable(True)
        self.toggle_button.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; font-size: 15px; border-radius: 10px; }")
        
        # Ustawiamy początkowy stan
        self.toggle_button.setChecked(True)

        # Łączymy sygnał kliknięcia z funkcją zmiany tekstu
        self.toggle_button.toggled.connect(self.on_toggle)

        # Tworzymy układ horyzontalny (etkieta + przycisk)
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.label)
        h_layout.addWidget(self.toggle_button)


        # Tworzymy layout i dodajemy przycisk
        self.layout.addLayout(h_layout)

        # Przycisk zatwierdzania
        self.confirm_button = QPushButton("Zatwierdź wybór")
        self.confirm_button.clicked.connect(self.confirm_selection)
        self.layout.addWidget(self.confirm_button)
        
        self.setLayout(self.layout)
            


    def create_file_selector(self, button_text, func):
        layout = QHBoxLayout()
        line_edit = QLineEdit()
        line_edit.setReadOnly(True)
        line_edit.setPlaceholderText("...")
        browse_button = QPushButton(button_text)
        browse_button.clicked.connect(lambda: func(line_edit))
        layout.addWidget(line_edit)
        layout.addWidget(browse_button)
        return layout


    def wczytaj_plik(self, line_edit):
        try:
            file_path, _ = QFileDialog.getOpenFileName(None, "Wybierz plik z tekstem", self.default_path, "txt (*.txt)")
            if file_path:
                line_edit.setText(file_path)
                with open(file_path, "r", encoding="utf-8") as plik:
                    self.tekst = plik.read()
                
                self.default_path="/".join(file_path.split("/")[-1])
                
        except:
            self.info.setText(f'Wybrano nie odpowiedni plik')
            self.info.setVisible(True)
    
    def wczytaj_klucz(self, line_edit):
        try:
            file_path, _ = QFileDialog.getOpenFileName(None, "Wybierz plik z kluczem", self.default_path, "txt (*.txt)")
            if file_path:
                line_edit.setText(file_path)
                with open(file_path, "r", encoding="utf-8") as plik:
                    self.klucz = plik.read()
                
                self.default_path="/".join(file_path.split("/")[-1])
                #print(tekst)
        except:
            self.info.setText('Wybrano nie odpowiedni plik')
            self.info.setVisible(True)
    
    def on_toggle(self):
        if self.toggle_button.isChecked():
            self.toggle_button.setText("Szyfruj")
            self.toggle_button.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; font-size: 15px; border-radius: 10px; }")
        else:
            self.toggle_button.setText("Odszyfruj")
            self.toggle_button.setStyleSheet("QPushButton { background-color: #f44336; color: white; font-size: 15px; border-radius: 10px; }")


    def confirm_selection(self):
        des=DES(self.tekst, self.klucz, self.toggle_button.isChecked())
        self.main_app.open_Main(self.default_path, des)
        self.close()
            

        
class MainApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.data=None
        self.fig=None
    
    def run(self): 
        self.start_window = MenuWindow(self)
        self.start_window.show()
        sys.exit(self.app.exec_())
        
    def open_Main(self, path, DES):
        self.mainWindow=MainWindow(DES, path)
        self.mainWindow.show()



if __name__ == '__main__':
    #plt.rcParams['toolbar'] = 'toolmanager'
    app = MainApp()
    data=app.data
    app.run()
    fig=app.plot_window.getFig()


