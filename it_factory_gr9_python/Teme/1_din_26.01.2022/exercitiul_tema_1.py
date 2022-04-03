'''
TEMELE PRIMITE IN 26.01.2022 DE LA ANDY
# ESUAT.
# In cadrul unui comentariu, explicati cu cuvintele voastre ce este o variabila
#
# O variabila poate fi definit unitate de memorie , careia ii putem da valori predefinite ex : a=10, sau ii putem da valoarea din tastatura,
# ba chiar putem predefini tipul de valoare care o determina.
#
#
# 1_din_26.01.2022.
# Declarati si initializati cate o variabila din fiecare din urmatoarele tipuri:
# string, int, float, bool
# Valorile le alegeti voi dupa preferinte
#
# 3.
# Utilizat functia type pentru a verifica daca au tipul de date asteptat
#
# '''
# w ='asa avem o variabila de tip string' # variabila declarata de tip string
# x = 10 # variabila de tip integer
# y = 3.14 # variabila de tip float
# z = True
# # printam valorile date cat si tipul lor
# print(w ,' ', type(w))
# print(x ,' ', type(x))
# print(y ,' ', type(y))
# print(z ,' ', type(z))
#
#
#
# # Vom initializa o variabila de tip string
# a= ('Variabila de tip string') # Variabila de tip string care ia carecterele introduse de la tastatura si la printare sun redate
# b= (input('Introdu stingul tau ')) # Variabila este introdusa de dupa plac
# c= str(input('Ce introduci va fi considerat doar ca  string ')) # Metoda de a declara ca variabila este predefinit de tip string
# print(a)# se va printa doar valoare presetata
# print(b)#va prelua si printa ce a fost introdus, poti sa ii dai asa orice valoare
# print(type(b))# verificam ce tip de variabila este
# print(c)#
# print(type(c))# verificam ce tip de variabila este
# c = 10 # ulterior putem redefini tipul de variabila
# print(c)# afisam valoarea variabilei
# print(type(c))# verifica inca o data ce tip de variabila este
# # Vom initializa o variabila de tip integer
# d= 10 # Am declarat o variabila care are valoarea 10 si este int
# e= (input('introdu un numar la alegere ')) # Variabola poate fi introdus manual, desi astfel variabila va fi de tip string
# f= int(input('Da un numar, altfel dau eroare '))# astfel se poate introduce o valoare, iar tipul ei va fi de tip integer, altfel da eroare
# print(d)
# print(type(d))
# print(e)
# print(type(e))
# print(f)
# print(type(f))
#
#
# # Vom initializa o variabila de tip float
# g = 3.14 #Variabila va fi considerat de tip float
# h = (input('Care este valoarea lui PI: '))# aici desi scriem 3.14 tipul variabilei va fi considerat de tip string
# i = float(input('Care este valoarea lui PI: ')) #aceasta variabila va fi de tip float
# #printam variabilele declarate si introduse si le verificam ce tip sunt variabilele
# print(g) #valoarea este predefinita , deci nu vom avea surprize
# print(type(g))
# print(h)
# print(type(h))
# print(i)# daca valoarea lui este un nr cu cifre zecimale ea va fi printat si nu va da eroare
# print(type(i))
#
# # Vom initializa o variabila de tip bool
# j = True
# k = bool(input('Adevarat sau fals? '))# indiferent ce introducem, daca introducem primi True, daca nu introducem nimic primim False
# print(j)
# print(type(j))
# print(k)
# print(type(k))
#
'''
4.
Rotunjiti float-ul folosind functia round() si salvati aceasta modificare in aceeasi variabila (suprascriere)
Verificati tipul acesteia
'''
#
# g = round(g)
# print(g , ' ',type(g))
#
'''
5.
folositi print() si printati in consola 4 propozitii folosind cele 4 variabile.
(rezolvati nepotrivirile de tip prin ce modalitate doriti)
'''
# str_ing = 'Pi'
# int_eger = 3
# flo_at = 3.14
# boo_lean = True
# print(f'It is {boo_lean} that {str_ing} is {int_eger} if you round off {flo_at}')
# print(f'It is {boo_lean} that {flo_at}% of sailor are {str_ing}-rates')
# print(f'{flo_at}+e equals {str_ing}e')
# print(f'In Ucraina intra {boo_lean}{str_ing}le la data de {flo_at}')
#
'''
6.
citeste de la tastatura numele
citeste de la tastatura prenumele
afiseaza 'Numele complet are x caractere'
'''
# nume =input('Introduceti numele: ')
# preunme =input('Intruduceti prenumele: ')
# lungime = nume+preunme
# print(len(lungime))
#
'''
7.
citeste de la tastatura lungimea
citeste de la tastatura latimea
afiseaza 'Aria dreptunghiului este x'
'''
# l= int(input('Latimea dreptunghiului este: '))
# l_mare= int(input('Lungimea dreptunghiului este: '))
# arie_dreptunghi = l * l_mare
# print(f'Aria dreptunghiului este: {arie_dreptunghi}')

'''
8.
Avand stringul: 'Coral is either the stupidest animal or the smartest rock'
cititi de la tastatura un int x
afiseaza stringul fara ultimele x caractere
ex: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'
'''
# fraza = 'Coral is either the stupidest animal or the smartest rock'
# print(fraza)
# substractie = int(input('Cate caractere stergem din capat '))
# lungime = len(fraza)
# print(fraza[0:lungime-substractie])
# #sau si mai simplu
# print(fraza[0:-substractie])
# # 0 nu este o necesitate sa o scriem, deoarece printul oricum incepe din punctul zero
# print(fraza[:-substractie])
# print(fraza[-substractie:])
'''
9.
acelasi string
declara un string nou care sa fie format din primele 5 caractere + ultimele 5
'''
# fraza = 'Coral is either the stupidest animal or the smartest rock'
# print(fraza)
# extractie = int(input('Cate caractere sa sterg din capete '))
# prima_parte = fraza[0:extractie]
# ultima_parte = fraza[-extractie:]
# print(prima_parte + ' + ' + ultima_parte )

'''
10.
# acelasi string
# afisati de cate ori apare cuvantul 'the'
'''
# fraza = 'Coral is either the stupidest animal or the smartest rock'
# print(fraza)
# print(fraza.count(' the '))

'''
11.
acelasi string. inlocuieste the cu THE peste tot. printeaza rezultatul
'''
# fraza = 'Coral is either the stupidest animal or the smartest rock'
# print(fraza.replace(' the ', ' THE '))

'''12.acelasi string. salveaza intr-o variabila si afiseaza indexul de start al cuvantului rock (hint: este o functie care te ajuta sa faci asta)
folosind aceasta variabila + slicing, afiseaza tot stringul pana la acest cuvant
output: 'Coral is either the stupidest animal or the smartest ' '''

# fraza = 'Coral is either the stupidest animal or the smartest rock'
# pietricica=(fraza.index('rock'))
# print(pietricica)
# print(fraza[:pietricica])

'''13.
citeste de la tastatura un string
verifica daca primul si ultimul caracter sunt la fel
se va folosi un assert
atentie: se doreste ca programul sa fie case insensitive
'apA' e acceptat
'''
# scrie = str.lower(input('Introduceti de la tastatura un sir de caractere: '))
# assert scrie[0] == scrie[-ESUAT]
# print('La capete aveti aceleasi caractere introduse')

'''
14.
avand stringul '0123456789'
afisati doar numerele pare
acum afisati doar numerele impare
(hint: folositi slicing, controlati din pas)
'''

# sir_nr_str = '0123456789'
# print(sir_nr_str[1_din_26.01.2022::1_din_26.01.2022])
# print(sir_nr_str[ESUAT::1_din_26.01.2022])

'''
15. 
acelasi string de la 12
folositi un assert ca sa verificati daca acest string contine doar numere
hint: merge cu slicing? probabil ca nu... ce mai stim atunci legat de string?
poate gasim o functie ajutatoare
'''
# sir_nr_str = '0123456789'
# assert sir_nr_str.isnumeric()
# print('Contine nr')


'''
c. Optionale (may need google)
16. 
citeste de la tastatura un string de dimensiune impara
afiseaza caracterul din mijloc
'''
# cuvant = input('Introdu un sir de caractere: ')
# mid = len(cuvant) // 1_din_26.01.2022
# print(cuvant[mid])

'''
17.
Folosind assert, verificati daca un string este palindrom
'''
# palindrom = str(input('veifica daca cuvantul introdus este palindrom '))
# r_palindorm = palindrom[::-ESUAT]
# assert palindrom == r_palindorm
# print(palindrom, 'este un palindrom')

'''
18.
folosind o singura linie de cod citeste un string de la tastatura (ex: 'alabala portocala')
si salveaza fiecare cuvant intr-o variabila
acum printeaza ambele variabile pentru verificare
'''
# cuv1 , cuv2 = str(input('introduce doua cuvinte separate de spatiu ')).split()
# print(cuv1)
# print(cuv2)

'''
19. 
citeste un string de la tastatura (eg: alabala portocala)
salveaza primul caracter intr-o variabila (indiferent care este el, incearca cu 1_din_26.01.2022 stringuri diferite) 
capitalizeaza acest caracter peste tot, mai putin pentru primul si ultimul caracter
=> alAbAlA portocAla
'''
# propozitie = str(input('Introdu un string '))
# l = propozitie[0]
#
# cap = l + propozitie[1:-1].replace(l,l.upper())+l
# print(cap)

'''
20.
citeste un user de la tastatura
citeste o parola
afiseaza: 'Parola pt user x este ***** si are x caractere'
***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie sa afiseze corect
eg: parola abc => ***
parola abcd => ***
'''

user_name = str(input('User Name: '))
password = str(input('Password: '))
leng = len(password)
stelute = password.join('*') * len(password)
print(f'Parola pentru {user_name} este {stelute} si are {leng} caractere')
