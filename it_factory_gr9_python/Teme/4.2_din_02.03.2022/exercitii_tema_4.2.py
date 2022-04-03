"""
1.Print First 10 natural numbers using while loop
"""
# i = 1
# while i < 11:
#     print(i)
#     i += 1
print("-------1----------")
"""
2.Write a program to print something like the following number pattern using a loop.
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
"""
# row = int(input('care sa fie numarul sirului de  numere:\n'))
# for i in range(1, row+1, 1):
#     for j in range(1, i+1):
#         print(j, end=' ')
#     print('')
print("----------2-----------")
"""
3.For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)
Varianta mea
"""

# suma = 0
# for i in range(1,(int(input('Suma cifrelor de la unu pana la: '))+1), 1):
#     suma += i
# print(f'Suma cifrelor este:', suma)


"""
v.2
"""
# x = sum(range(1,(int(input('Suma cifrelor de la unu pana la: '))+1)))
# print(f'Suma cifrelor este:', x)
print("----------3-----------")

"""
4: Write a program to print multiplication table of a given number
"""

# for x in range(1,11):
#     n = x * 2
#     print(n)
print("----------4-----------")

"""
5.Display numbers from a list using loop
Write a program to display only those numbers from a list that satisfy the following conditions

The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop
"""

# numbers = [12, 75, 150, 180, 145, 525, 50]
# for i in numbers:
#     if i >= 500:
#         break
#     if i > 150:
#         continue
#     if i%5 == 0:
#         print(i)
print("----------5-----------")


"""
6. Count the total number of digits in a number
Write a program to count the total number of digits in a number using a while loop.

For example, the number is 75869, so the output should be 5.

Varianta mea
"""
# n = int(input('Introduceti un numar sa vedem din cate cifre este alcatuti: '))
# l = len(str(n))
# print(l)

"""
Varianta site
"""
# num = 75869
# count = 0
# while num != 0:
#     num = num // 10
#     count = count + 1
# print("Total digits are:", count)
print("----------6-----------")

"""
Exercise 7: Print the following pattern
Write a program to use for loop to print the following reverse number pattern

5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
"""

# n = 5
# k = 5
# for i in range(0,n+1):
#     for j in range(k-i,0,-1):
#         print(j,end=' ')
#     print()

print('-----------7----------')
print('---------teme_curs_4.1---------')

"""
Recapitulare tema curs 4

1.
Avand lista
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

Folositi un for ca sa iterati prin toata lista si sa afisati
‘Masina mea preferata este x’
Faceti acelasi lucru cu un for each
Faceti acelasi lucru cu un while
"""
"""
A iterare prin for
"""
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for i in masini:
#     print(f'Masina mea preferata este', i)

"""
A iterare prin for each
"""
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for masina in masini:
#     print(f'Masina mea preferata este', masina)

"""
A iterare prin while
"""
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# i=0
# while i < len(masini):
#     print(f'Masina mea preferata este', masini[i])
#     i +=1
print('---------teme_curs_4.2---------')
'''
2.
Aceeasi lista
Folositi un for else
In for
   Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul
In else 
   Printati lista
'''
""""V1"""
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for i in range(len(masini)):
#     if not(i==0 or i==len(masini)-1):
#         print(masini[i].upper())
#     else:
#         print(masini[i])

""""V2"""
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for i in range(len(masini)):
#     if (i==0 or i==len(masini)-1):
#         print(masini[i])
#     else:
#         print(masini[i].upper())

print('---------teme_curs_4.3---------')
'''
3. 
Aceeasi lista, 
Vine un cumparator care doreste sa cumpere un Mercedes
Iterati prin ea prin modalitatea aleasa de voi
Daca masina e mercedes 
   Printam ‘am gasit masina dorita de dvs’
   Iesim din ciclu folosind un cuvant cheie care face acest lucru
Altfel
   Printam Am gasit masina X. Mai cautam	
'''
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for masina in masini :
#     if masina == 'Mercedes':
#         print('Am gasit masina dorita de Dvs.')
#         break
#     else:
#         print(f'Am gasit masina {masina}. Mai cautam!')

print('---------teme_curs_4.4---------')
"""
4.
Aceasi lista
Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun
"""
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for masina in masini:
#     if masina == 'Trabant' or masina == 'Lastun':
#         continue
#     else:
#         print(f'Avem sa va prezentam: {masina}')

print('---------teme_curs_4.5---------')

"""
5. 
Modernizati parcul de masini
Creati o lista goala, masini_vechi
Iterati prin masini
Cand gasiti Lastun sau Trabant:
-	Salvati aceste masini in masini_vechi
-	Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
Printati Modele vechi: x
Modele noi: x
"""
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# masini_vechi = []
# for i in range(len(masini)):
#     if masini[i] == 'Trabant' or masini[i] == 'Lastun':
#         masini_vechi.append(masini[i])
#         masini[i]='Telsa'
# print(masini)
# print(masini_vechi)

print('---------teme_curs_4.6---------')

"""
6. 
Avand dict
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000 }
Vine un client cu un buget de 15000 euro
Prezentati doar masinile care se incadreaza in acest buget
Iterati prin dict.items() si accesati masina si pretul
Printati Pentru un buget de sub 15000 euro puteti alege masina x

"""

# pret_masini = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000 }
# budget = 15000
# for pret in pret_masini.items():
#     if pret[1] <= budget:
#         print(f'Pentru un buget de sub 15000 euro puteti alege masina ',pret[0])

print('---------teme_curs_4.7---------')









































