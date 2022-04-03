# nume = input('Alege un nume')# default - string
# varsta = int(input('alege varsta'))

#input
a = 3
b = int(input('alege numar'))
print(a + b)

#input
a = 3
b = int(input('alege numar, by default el este str'))
print(a + b)

# uitati de asta dar merge
b = int(round(float(input('alege un nr'))))

name, age, gender = input('Enter Name|Age|Gender (separated by | sign):').split(' ')
print(name)
print(age)
print(gender)
# default la split e sa delimiteze dupa spatiu
