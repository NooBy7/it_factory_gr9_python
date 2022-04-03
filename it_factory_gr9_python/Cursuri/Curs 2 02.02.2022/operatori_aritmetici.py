#operatori aritmetici
print(10%3)# restul impertirii 10 la 3
print(2**3) # ridicare la putere
print(9//2)
x =9
print(x**(1/2)) # radical de baza 1_din_26.01.2022
print(16//2)

print('-----------------')
#operatori de comparatie
x = 5
y = 3
print(x==y) # operator de comparartie
x = y
x=5
print(x==y)
print(x!=y)# verifica daca valorile variabilelor sunt diferite
print(x<y)
print(x<=y)
print(x>=y)
print(x>y)
print('-----------------')
#Operatori logici
'''
Operatori logici sunt : and , or , not
intotdeanu operatorul and are prioritate in fata operatorului or
'''
print(x<2 and x<y) # ambele conditii trbuie sa fie true pentru a avea conditii
print(x>2 and x<y)
print(x>2 and x<y or y>2)
print(x>2 or x<y and y>2)
print(x>2 and (x<y or y>2))
print('-----------------')
pasaport = (input('introduceti validarea pasaportului , alegeti da sau nu : '))
ambii_pariti = input('are ambii parinti , alegeti da sau nu: ')
permisiune = input('Are permisiunea? DA/NU/NA: ')
if pasaport == 'DA' and (ambii_pariti == 'DA' or permisiune == 'DA'):
    print('Permite calatoria')
else:
    print('Nu permite calatoria')


