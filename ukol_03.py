"""
ukol-03: SMS brána
Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:

1.Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
2. Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.

Tvůj program bude obsahovat dvě funkce:

1.První funkce ověří délku telefonního čísla. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). Nemusíte kontrolovat, zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme v kurzu zatím neřešili. Pokud je číslo platné, funkce vrátí hodnotu True, jinak vrátí hodnotu False.
2.Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.

Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou vypíše uživateli.
"""

import math

cislo_uzivatele = input("Jake je vase cislo?")

def platnost_cisla(cislo_uzivatele):
    return (len(cislo_uzivatele) == 9) or ("+420" in cislo_uzivatele and len(cislo_uzivatele) == 13)
  
def cena_zpravy(cena, pocet):
   celkova_cena = cena * pocet       
   return celkova_cena 

if platnost_cisla(cislo_uzivatele):
    text_zpravy = input("Napiste text zpravy:")
    cena_180z = 3
    pocet_segmentu = math.ceil(len(text_zpravy)/180) 

    print("Cena zpravy je", cena_zpravy(cena_180z, pocet_segmentu), "Kc.")
else:
    print("Toto neni telefonni cislo.")     




        

        
   

