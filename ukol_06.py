"""
https://github.com/andywaltlova/python-1-podzim-2022/blob/master/ukoly/ukol-06.md
"""

with open('semestr_znamky.txt', 'r', encoding = 'utf-8') as file:
    radky = file.readlines()

for radek in radky:
    print(radek)    

radky_testy = [radek.replace ("1", "1").replace("2",'2').replace ('3','3').replace ('4','4').replace('5','5') for radek in radky[0]]

radky_s_pismeny = [radek.replace ("1",'A').replace("2",'B').replace ('3','C').replace ('4','D').replace('5','E') for radek in radky[1:]]

print(radky_testy, radky_s_pismeny)

vsechny_radky = radky_testy + radky_s_pismeny

with open('semestr_znamky_nove.txt', 'w', encoding =  'utf-8') as file:
    file.writelines(vsechny_radky)

    

