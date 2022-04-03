"""
explicati urmatoarele chestii:
    -Ce este un for, cand se foloseste si cum se foloseste:
Este un mod prin care se programeaza repetarea unei secvente de operatiuni,
    -Ce este un for each, cand se foloseste si cum se foloseste
-Este o soliutie de iterare a unei secvente de operatiuni cu numar finit de executie atribuindu-se unei variabile
temporare o valoare
 in functie de  parametri altei variabile

    -Care e diferenta intre for si foreach
    -Ce este un while, cand se foloseste si cum se foloseste.
Este creearea unei bucle

"""
"""Clasa Cerc

Atribute: raza, culoare

Constructor pt ambele atribute

Metode:
descrie_cerc() - va PRINTA culoarea si raza
aria() - va RETURNA aria 
diametru() 
circumferinta()
"""


class Cerc:  # definim clasa cerc cu litera mare
    # aici trecem atrubutele(fields)
    raza = 0
    culoare = None

    # definim constructorul
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    # aici facem metodele
    def descrie_cerc(self):
        culoare = self.culoare
        raza = self.raza
        return f'Cercul nostru are culoarea {culoare} si are o raza de {raza}'

    def aria(self, ):
        aria = (self.raza ** 2) * 3.14
        return aria

    def diametru(self, ):
        diametru = 2 * self.raza
        return diametru

    def circunferinta(self):
        circumferinta = 2 * self.raza * 3.14
        return circumferinta


print('------Cerc2--------')
cerc1 = Cerc(8, 'Galben')
print(cerc1.descrie_cerc())
print(f'Aria cercului este: {cerc1.aria()}')
print(f'Diametrul ceruclui este: {cerc1.diametru()}')
print(f'Circumferinta cerecului este: {cerc1.circunferinta()}')
print(f'Am creat Cercul1 despre care putem spune :\n{cerc1.descrie_cerc()}\n-are culoarea {cerc1.culoare}'
      f'\n-raza sa este de {cerc1.raza} fapt careia ii datoram urmatoarele:'
      f'\nAria: {cerc1.aria()}  Diametrul este: {cerc1.diametru()}  Circumferinta:{cerc1.circunferinta()} ')
print('------Cerc2--------')
cerc2 = Cerc(12, 'Bleumarin')
print(cerc2.descrie_cerc())
cerc2.raza = 8
print(f'Aria cercului este: {cerc2.aria()}')
print(f'Diametrul ceruclui este: {cerc2.diametru()}')
print(f'Circumferinta cerecului este: {cerc2.circunferinta()}')
print(f'Am creat Cercul1 despre care putem spune :\n{cerc2.descrie_cerc()}\n-are culoarea {cerc2.culoare}'
      f'\n-raza sa este de {cerc2.raza} fapt careia ii datoram urmatoarele:'
      f'\nAria: {cerc2.aria()}  Diametrul este: {cerc2.diametru()}  Circumferinta:{cerc2.circunferinta()} ')




