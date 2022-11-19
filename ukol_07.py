"""
https://github.com/andywaltlova/python-1-podzim-2022/blob/master/ukoly/ukol-07.md
"""

from datetime import datetime

datum_navstevy_str = input("Kdy chcete letni kino navstivit?")
# pocet_osob = int(input("Kolik vstupenek chcete?"))


datum_navstevy = datetime.strptime(datum_navstevy_str, "%d.%m.%Y")
# print(datum_navstevy)

otevreno_od_1 = datetime(2021, 7, 1)
otevreno_do_1 = datetime(2021, 8, 10)
otevreno_od_2 = datetime(2021, 8, 11)
otevreno_do_2 = datetime(2021, 8, 31)

cena_vstupenky_1 = 250
cena_vstupenky_2 = 180

if (datum_navstevy >= otevreno_od_1) and (datum_navstevy <= otevreno_do_1):
   pocet_osob = int(input("Kolik vstupenek chcete?"))
   celkova_cena_1 = pocet_osob*cena_vstupenky_1
   print(f'Celkova cena bude {celkova_cena_1}.')
elif (datum_navstevy >= otevreno_od_2) and (datum_navstevy <= otevreno_do_2):
    pocet_osob = int(input("Kolik vstupenek chcete?"))
    celkova_cena_2 = pocet_osob*cena_vstupenky_2
    print(f'Celkova cena bude {celkova_cena_2}.')
else:
    print("Letni kino je zavrene.")
