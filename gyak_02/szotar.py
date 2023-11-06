""" FELADAT:
Készíts egy programot, ami egy beírt szót lefordít angolról magyarra vagy magyarról angolra!
Írja ki a program, ha a megadott szó nem található meg egyik szótárban sem,
egyébként a lefordított szót írja ki. A szavak legyenek előre eltárolva egy-egy tíz elemű listában!
"""

# Szótárak
angol_szavak = [
    "apple", "break", "chair", "tree", "respect", "water", "table", "error", "snake", "animal",
]
magyar_szavak = [
    "alma", "szünet", "szék", "fa", "tisztelet", "víz", "asztal", "hiba", "kígyó", "állat",
]

szo = input("Kérek egy magyar vagy angol szót! ")

if szo in angol_szavak:
    i = angol_szavak.index(szo)
    print(magyar_szavak[i])
elif szo in magyar_szavak:
    i = magyar_szavak.index(szo)
    print(angol_szavak[i])
else:
    print(f"A(z) {szo} egyik szótárban sem található meg!")
