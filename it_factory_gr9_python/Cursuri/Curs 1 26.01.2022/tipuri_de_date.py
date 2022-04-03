import math
marca = 'Dacia' # string - sir de caractere
an_fabricatie = 1987 # int - nr intreg
pret = 2300.500 # float
itp = True
print(type(itp))
#imprtam librarie (cod) externa


a = 3.7
# sintaxa care limitaza nr de zecimale
print('{:.2f}'.format(a))# se va lista a doar cu 1_din_26.01.2022 zecimale
print(round(a))
print(math.floor(a)) # fortam rotunjire in jos
print(math.ceil(a)) # fortam rotunjire in sus

# cum aflam tipuri

nume = 'Norbi'
print(type(nume)) # => <class 'str'>

#type casting - schimbam tipul de date
cifra = '3'
# cifra= int(cifra) # schimbam tipul de date / type casting
cifra2 = int(cifra)
print(cifra)
print(type(cifra))
print(cifra2)
print(type(cifra2))