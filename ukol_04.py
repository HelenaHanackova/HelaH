"""
Kuchařka a recepty
https://github.com/andywaltlova/python-1-podzim-2022/blob/master/ukoly/ukol-04.md
"""

class Recept:
    
    def __init__(self, nazev, narocnost, url_adresa):
        self.nazev = nazev
        self.narocnost = narocnost
        self.url_adresa = url_adresa
        self.vyzkouseno = False
    
    def zmen_narocnost(self, nova_hodnota):
        self.narocnost = nova_hodnota

    def zkusit (self):
        self.vyzkouseno = True

    def __str__(self):
        if self.vyzkouseno:
            vypis = "Recept vyzkousen: ano."
        else:
            vypis = "Recept vyzkousen: ne."
        return f" Recept {self.nazev} má narocnost {self.narocnost}. Odkaz: {self.url_adresa}. {vypis}"

class Kucharka:

    def __init__(self, nazev, autor):
        self.nazev = nazev
        self.autor = autor
        self.recepty = []
                                                      
    def pocet_receptu(self):
        return len(self.recepty)              

    def pridej_recept(self, recept):
        self.recepty.append(recept)          

    def __str__(self):
        return f"{self.nazev} od {self.autor} - {self.pocet_receptu()} receptu."

babovka = Recept('Babovka', 3, 'www.babovka.cz')
palacinky = Recept('Palacinky', 1, 'www.palacinky.cz')
dort = Recept('Dort',5,"www.dort.sk")
print(babovka)
babovka.zkusit()
palacinky.zkusit()
print(babovka)
print(palacinky)
print(dort)
palacinky.zmen_narocnost(3)
print(palacinky)
    
moje_kucharka = Kucharka ("Sladke", "Eliska")
print(moje_kucharka)
moje_kucharka.pridej_recept(babovka)
moje_kucharka.pridej_recept(palacinky)
moje_kucharka.pridej_recept(dort)

print(moje_kucharka)
print(moje_kucharka.pocet_receptu())

