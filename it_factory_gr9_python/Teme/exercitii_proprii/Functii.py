"""
Magyar Youtube csatornarol
"""

nevek1 = ['Xena', 'Bozsi', 'Vica', 'Eni', 'Ildi', 'Zsizsi', 'Evi', 10, True]
nevek2 = ['Pityu', 'Ati', 'Peti', 'Bence', 'Feri']


def nev_printer(nev_lista):
    for nev in nev_lista:
        if isinstance(nev, str):
            print(nev.upper())
        else:
            print('Nem string tipus, hanem:' + str(type(nev)) )

nev_printer(nevek1)
nev_printer(nevek2)
