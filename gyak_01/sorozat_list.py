"""
FELADAT:
Írj egy programot, amely előállít egy 110 elemű sorozatot 1-gyel kezdve úgy,
hogy a sorozat elemei között 12 a különbség!
- A program írja ki a sorozat 1. és 10. elemét egymás mellé!
- A program írja ki a sorozat 100. elemét!
- A program számolja ki a sorozat 1. és 10. elemének összegét, majd írja ki!
"""

# List-ben tároljuk a sorozatot
sorozat = []

# Kezdőértékek
i = 0  # Cíklusváltozó
a = 1  # Sorozat első eleme

# Sorozat előállítása
while i < 110:
    sorozat.append(a)  # Új elem hozzáadása a list-hez
    a += 12
    i += 1

# 1. és 10. elem
print(f"A sorozat 1. eleme: {sorozat[0]}, 10. eleme: {sorozat[9]}")

# 100. elem
print(f"A sorozat 100. eleme: {sorozat[99]}")

# 1. és 10. elem összege
print(f"A sorozat 1. és 10. elemének összege: {sorozat[0] + sorozat[9]}")
