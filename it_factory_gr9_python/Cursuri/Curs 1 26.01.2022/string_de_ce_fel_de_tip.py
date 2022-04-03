# string
prop = 'Norbi este prescurtat de la Norbert'
print(len(prop))
print(prop[0:3])
print(prop[::-1])
print(prop.upper())

#string index
print(prop[3])

#string slicing
# https://stackoverflow.com/questions/509211/understanding-slice-notation
# my_string[de unde incepem : pana unde mergem : din cat in cat]

myStr = 'Azi e miercuri'
#vreay sa il parcurg pana la penultimul
#aflu ultimul index
last_index = len(myStr)-1
print(last_index)
print(myStr[last_index])
print(myStr[13])
#hai sa parcurgem
print(myStr[0:last_index-1])
print(myStr[0:last_index:2])# de unde incepem : pana unde mergem : din cat in cat
# hai sa parcurgem
print(myStr[::-1])
#parcurgere inversa
print(myStr[:1:-1]) # coada : inceput : -ESUAT