"""
FELADAT:
While ciklussal add össze azokat a számokat, amelyek a 10000 és 35000
zárt intervallumba esnek és oszthatók 7-tel!
"""

# Kezdőértékek megadása
osszeg = 0  # Összeg tárolása
szam = 10000  # Intervallum alsó határa

# Ciklus
while szam <= 35000:  # Amíg a szám el nem éri az intervallum felső határát
    if szam % 7 == 0:  # Ha a szám osztható 7-tel
        osszeg += szam  # Hozzáadjuk a számot az összeghez
    szam += 1  # Következő szám

# Összeg kiírása
print(f"Az összeg: {osszeg}")
