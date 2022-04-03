'''4. Verificaţi dacă un cuvânt este palindrom. Un cuvânt este palindrom dacă scris de la dreapta la
stanga, este tot acel cuvânt.(folositi assert pt verificare)
am gasit cateva metode nici una cu "assert" pe https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/
'''
#asa am inceput eu
#a = str(input('Intruduceti un palindrom '))
#reversed(a)
#print(a)

def reverse(string):
    string = "".join(reversed(string))
    return string


s = str(input('Intruduceti un palindrom '))

print("The original string  is : ", end="")
print(s)

print("The reversed string(using reversed) is : ", end="")
print(reverse(s))

if s : reverse(s) print('avem un paindrom')
else print('nu avem un palindrom')

