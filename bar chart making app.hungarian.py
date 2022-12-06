# -*- coding: utf-8 -*-
"""
Created on Mon May 10 15:17:08 2021

@author: József
"""
import signal
import sys, os
import matplotlib.pyplot as plt






print("Szia! Én egy diagramkészítő alkalmazás vagyok. A nevem Grafikonka! \t Az adatok megadása során az X tengelyé csak string, az Y tengelyé pedig csak integer lehet. Jó munkát!")
telegram = [int(input("Add meg az Y tengely elemeit: ")) for i in range(int(input("Hány elem legyen az Y tengelyen? ")))]
plt.bar([int(input("Add meg az Y tengely elemeit: ")) for i in range(int(input("Hány elem legyen az Y tengelyen? ")))], color = input("Add meg az oszlopok színét a diagramon angolul: "))
plt.title(input("Mi legyen a diagram címe? "))
plt.xlabel(input("X tengely neve: "))
plt.ylabel(input("Y tengely neve: "))
data = input("Szeretnéd menteni a kész diagramot? [igen/nem] ")
if "igen" in data:
    plt.savefig(input('Milyen néven szeretnéd menteni a fájlt? ')+'.png', dpi=400, bbox_inches='tight')
    

plt.show()







