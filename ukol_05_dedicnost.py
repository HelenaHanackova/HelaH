"""
https://github.com/andywaltlova/python-1-podzim-2022/blob/master/ukoly/ukol-05.md
"""
class Nemoc:

    def __init__(self, jmeno, inkubacni_doba, pocet_obeti, sireni):
        self.jmeno = jmeno
        self.inkubacni_doba = inkubacni_doba
        self.pocet_obeti = pocet_obeti
        self.sireni = sireni

    def __str__(self):
        return f'Nazev: {self.jmeno}'

    def zmen_pocet_obeti(self, pocet_obeti):
        self.pocet_obeti = pocet_obeti

class Koronavirus(Nemoc):

    def __init__(self,jmeno, inkubacni_doba = 7, pocet_obeti = 125, sireni = 'vzduchem',):
        super().__init__(jmeno, inkubacni_doba, pocet_obeti, sireni)
        self.varianty = []
     
    def pridej_variantu(self, varianta):
        self.varianty.append(varianta)
        
    def __str__(self): 
        if len(self.varianty)==0:
            return f"{super().__str__()}\nZadne nalezene varianty"
        else:       
            return f"{super().__str__()}\nVarianty: {', '.join(self.varianty)}"


omikron = Koronavirus('Coronavirus', ['omikron'])
print(omikron)

corona = Koronavirus('Coronavirus')
print(corona)
corona.pridej_variantu('omikron')
print(corona)
print(corona.pocet_obeti)
corona.zmen_pocet_obeti(1563)
print(corona.pocet_obeti)
corona.pridej_variantu('delta')
corona.pridej_variantu('alpha')
print(corona)








