"""
FELADAT:
Írj egy programot, amely véletlenszerűen generálja egy derékszögű háromszög
befogóit (1-20) és kiszámolja az átfogót és a háromszög területét, majd
kírja az oldalakat és a területet!
"""

# Modulok importálása
from random import randint
from math import sqrt

# Befogók generálása
a = randint(1, 20)  # A oldal
b = randint(1, 20)  # B oldal

# Átfogó kiszámítása
c = sqrt(a ** 2 + b ** 2)  # C oldal

# Terület kiszámítása
t = a * b / 2

# Változók kiírása
print(f"A = {a}\nB = {b}\nC = {c:.2f}\nT = {t:.1f}")
