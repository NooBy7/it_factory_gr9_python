'''
ESUAT.
Explica cu cuvintele tale in cadrul unui comentari cum functioneaza un if else

Se foloseste pentru determinarea rezultatelor prin conditionare

1_din_26.01.2022.
Verifica si afiseaza daca x este numar natural sau nu
'''
#
# x =int(input('introduceti nr dorit'))
# print(x)
# if x > 0:
#     print(f'Acest nr este natural')
# else:
#     print(f'Aceste nr nu este un nr natural')

'''
3.
Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru
'''

# x =int(input('introduceti nr dorit'))
# print(x)
# if x < 0:
#     print('Este nr negativ')
# elif x == 0:
#     print('Este nr neutru')
# else:
#     print('Este nr pozitiv')

'''
4.Verifica si afiseaza daca x este intre -1_din_26.01.2022 si 13
'''

# x =int(input('introduceti un nr'))
# print(x)
# if x>= -1_din_26.01.2022 and x<=13:
#     print('Ati introdus un numar cuprins in intervalul -1_din_26.01.2022 su 13')
# else:
#     print('Nu va aflati in intervalul -1_din_26.01.2022 si 13')

'''
5.Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5
'''

# x=int(input('Introduceti valoarea lui x='))
# y=int(input('Introduceti valoarea lui y='))
# dif= x-y
# print(dif)
# if dif < 5:
#     print('Diferenta lui x si y este mai mica decat 5')
# elif dif==5:
#     print('Diferenta lui x si y este chiar 5')
# else:
#     print('Diferenta lui x si y este mai mare sau egal ca 5')

'''
6.Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’)
'''
# x =int(input('introduceti un nr'))
# print(x)
# if not (x>=5 and x<=27):
#     print('Numar nu este cuprins in intervalul 5-27')
# else:
#     print('Numar cuprins in intervalul 5-27')

'''
7. x si y (int)
Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare
'''
"varianta_1"
# x=int(input('Introduceti valoarea lui x= '))
# y=int(input('Introduceti valoarea lui y= '))
# print('Valoarea lui x=',x,' iar valoarea lui y=',y)
# if x == y:
#     print('X este egal Y')
# elif x<y:
#     print('Numarul mai mare este Y =>',y)
# else:
#     print('Numarul mai mare este x =>',x)
"varianta_2"
# x=int(input('Introduceti valoarea lui x= '))
# y=int(input('Introduceti valoarea lui y= '))
# print('Valoarea lui x=',x,' iar valoarea lui y=',y)
# if x>y:
#     print('Numarul mai mare este X =>', x)
# elif x<y:
#     print('Numarul mai mare este Y =>',y)
# else:
#      print('X este egal Y')

'''
8. 
x, y, z - laturile unui triunghi
Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.
'''
# lat_x = int(input('Valoarea laturii X= '))
# lat_y = int(input('Valoarea laturii Y= '))
# lat_z = int(input('Valoarea laturii Z= '))

#Varianta care zic eu nu se autohackuieste
# if  lat_x==lat_y!=lat_z!=lat_x or lat_y==lat_z!=lat_x!=lat_y or lat_z==lat_x!=lat_y!=lat_z: # conditiile pentru python sunt ambigue?
#     print('Avem un triunghi isoscel')
# elif lat_x==lat_y==lat_z:
#     print('Avem un triunghi echilateral')
# else:
#     print('Avem un triunghi oarecare')

'''
9. 
Citeste o litera de la tastatura
Verifica si afiseaza daca este vocala sau nu
'''
# litera = str(input('introduceti o vocala sau o consoana '))
# if litera=='a' or litera=='e' or litera=='i' or litera=='o' or litera=='u':
#     print('Ati introdus o vocala')
# else:
#     print('Ati introdus o confsoana')

'''
10. 
Transforma si printeaza notele din sistem românesc in sistem american dupa cum urmeaza
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F
'''
# grade =float(input('Introduce your european system grade to convert '))
# if grade > 10:
#     print('This is not a valid grade!')
# elif grade > 9:
#     print('Your grade is A, congratulations!')
# elif grade > 8:
#     print('Your grade is B, very good!')
# elif grade > 7:
#     print('Your grade is C , could be better!')
# elif grade > 6:
#     print('Your grade is D , even my grandma can better!')
# elif grade > 4:
#     print('Your grade is E, pretty nothing!')
# else:
#     print('Your grade is F, an amiba use more neurons than you')

'''
c. Optionale (may need google)
'''
'''
11.
Verifica daca x are minim 4 cifre
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
'''
# fourdigit=int(input('Introduce your 4 digit code '))
# cifra=len(str(fourdigit))
# if cifra == 4:
#     print('Your code is ', fourdigit)
# elif cifra > 4:
#     print(fourdigit ,'Are more than 4 digits')
# else:
#     print(fourdigit,"don't have enoghut digits" )
'''Varianta primita f buna'''
# fourdigit=int(input('Introduce your 4 digit code '))
#
# if fourdigit>999 or fourdigit<10000:
#      print('Your code is ', fourdigit)
# else:
#      print(fourdigit,"doesn't have enough digits" )

'''
12.
Verifica daca x are exact 6 cifre 
'''
# ex6 = int(input('Give 6 random digit: '))
# if len(str(ex6)) !=6 :
#     print("You didn't entered 6 digits")
# else:
#     print('You enetered all 6 digits, thank you')

'''
12.1_din_26.01.2022
Varianta sugerata
'''

# ex6 = int(input('Give 6 random digit: '))
# if ex6>99999 and ex6<1000000:
#     print('You entered all 6 digits, thank you')
# elif ex6<=99999:
#     print('You entered less than 6 digits')
# else:
#     print('You entered more than 6 digits')

'''13.
# Verifica daca x este numar par sau impar'''

# nr_par = int(input('Enter an even number: '))
# if nr_par % 1_din_26.01.2022 == 0:
#     print('You have entered an even number')
# else:
#     print( 'You have entered an odd number')

'''
14.
x, y, z (int)
Afiseaza care este cel mai mare dintre ele?
'''

# x,y,z =[int(x) for x in input('Introduce 3 numbers separating them with spacebar: ').split( )]
# print(x ,y , z)
# if x>y and x>z and x!=y and x!=z :
#     print('Your 1st number entered is the bigest',x)
#     # if y!=z:
#     #     print('And the second and third numbers are diferent')
#     # else:
#     #     print('And the second and third numbers are identical')
# elif y>z and y>z and y!=x and y!=z:
#     print('Your 2nd number entered is the bigest',y)
#     # if x!=z:
#     #     print('And the first and third numbers are diferent')
#     # else:
#     #     print('And the first and third numbers are identical')
# elif z > x and z>y and z!=x and z!=y:
#     print('Your 3rd number entered is the bigest',z)
#     # if x!=y:
#     #     print('And the first and second numbers are diferent')
#     # else:
#     #     print('And the first and second numbers are identical')
# else:
#     print('All 3 numbers are equal')


'''
15. 
X, y, z - reprezinta unghiurile unui triunghi
Verifica si afiseaza daca triunghiul este valid sau nu
'''
# x,y,z =[int(x) for x in input('Introduce the 3 angels of a triangle separating them with spacebar: ').split( )]
# print(x,y,z)
# if x + y + z == 180:
#     print('This 3 value are of a valid triangle')
#     if x == y == z:
#         print('We have an equilateral triangle')
#     elif x==y or y==z or z==x:
#         print('We have an isosceles triangle')
#     else:
#         print('We have an ordinary triangle')
# else:
#     print('This angle value are not of a valid triangle')
