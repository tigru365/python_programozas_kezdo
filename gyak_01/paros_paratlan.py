""" FELADAT:
A program kérjen be egy számot és írja ki, hogy a szám páros vagy páratlan!
"""

# Szám bekérése STDIN-ről és egész számmá alakítása
szam = int(input("Adj meg egy egész számot: "))

# Páros vagy páratlan szám
if szam % 2 == 0:
    tulajdonsag = "páros"
else:
    tulajdonsag = "páratlan"

# Eredmény kiírása
print(f"A szám {tulajdonsag}.")
