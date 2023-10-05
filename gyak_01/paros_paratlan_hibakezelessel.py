"""
FELADAT:
A program kérjen be egy számot és írja ki, hogy a szám páros vagy páratlan!
A program írjon hibaüzenetet, ha a beolvasott érték nem egész szám!
"""

# Szám bekérése STDIN-ről
szam_beolvas = input("Adj meg egy egész számot: ")

# Hibakezelés
try:
    szam = int(szam_beolvas)  # Átalakítás egész számmá
except ValueError:  # Értékhiba esetén
    print("Nem egész számot adtál meg!")  # Hiba kiírása
else:
    # Páros vagy páratlan szám
    if szam % 2 == 0:
        tulajdonsag = "páros"
    else:
        tulajdonsag = "páratlan"

    # Eredmény kiírása
    print(f"A szám {tulajdonsag}.")
