"""
Úkol č.1 - Balíky

Níže máš slovník, který obsahuje kódy balíků s informací, zda již byl balík předán kurýrovi k doručení. Pokud byl předán, má hodnotu True, v opačném případě má hodnotu False.

Napiš program pro operátora společnosti, který poskytuje informaci, zda byl balík předán kurýrovi. Nejprve se uživatele zeptej na kód balíku. Následně podle hodnoty ve slovníku vypiš větu Balík byl předán kurýrovi nebo Balík zatím nebyl předán kurýrovi.

baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}
"""

baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

cislo_baliku = input("Zadej cislo baliku:")

if cislo_baliku in baliky:
    na_sklade = baliky[cislo_baliku]
    if na_sklade:
        print("Balik byl predan kuryrovi.")
    else:
        print("Balik zatim nebyl predan kuryrovi.")
else:
    print("Tento balik nemame v preprave.")
