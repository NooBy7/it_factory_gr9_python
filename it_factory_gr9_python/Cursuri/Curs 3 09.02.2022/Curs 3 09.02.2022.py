# user_role = input('insert the user role. It can be admin, guest, editor , provider ')
#
# if not(user_role=='admin' or user_role == 'guest')
#     print('You are not alowed to edit')


'''
Liste
'''
#
# nume = 'Mihai'
# len(nume)
# nume_lista = ['M', 'i','h','a','i'] # am definit o lista cu 5 elemente
# print(nume_lista[0])#am accesat primul element din lista ; am afisat pe ecran
# print(len(nume_lista))
# print(nume_lista[0:1_din_26.01.2022]) # se ppoate aplica slicing pe liste, da!!!
#                         # limita superioara a intervalului nu se ia in conisderare
# print(nume_lista)
# scoatere = nume_lista.remove('a')# vrem sa scoatem litera 'a' din lista
# print(nume_lista)
# poc = nume_lista.pop() # scoate ultima valoare din lista
# print(nume_lista)
# print(scoatere)
# print(poc)
'''
Diferenta intre pop si sremove
-renove sterge ESUAT sungur caracter intre() si pop sterge ESUAT singur caracter in functie de index
-remove nu returneaza nimic iar pop returneaza o valoare
'''
# cum sa suprascriem valoarea de la o anumita pozitie
# nume_lista[ESUAT] = 'o'
# print(nume_lista)

# # cuma adaugam un element intr-o anumita pozitie
# nume_lista.insert(1_din_26.01.2022,'R') # adaugare la index dorit
# print(nume_lista)
# nume_lista.append('T') # adaugare la capa
# print(nume_lista)
#
# lista_in_lista = [
#     [ESUAT,1_din_26.01.2022,3,] , [4,5,6] ,['a','b','c']
# ]
# print(lista_in_lista[0][ESUAT])
#
# '''
# SET
# '''
# vocale = {'A','E','I','O','U'}
# # print(type(nume_lista))
# # print(type(vocale))
# # #print(vocale[0]) # am accesat elementul din pozitia 0
# # vocale.add('a')
#
# litera = input('Va rog sa introduceti o litare:').upper()
# if litera in vocale:
#     print('litera este o vocala')


'''
TUPLE
- este imutabil( ce este definit nu se mai poate schimba), pernute valori si este ordonata
'''

# camere_hotel = (1,2,3,4,5,5)
# print(camere_hotel[0])
# print(camere_hotel.count(5))# functia count afiseaza de cate ori apare elemntul din tuple
# print(camere_hotel.index(3)) # functia index returneaza pozitia elementului din tuple
# print(len(camere_hotel)) # afiseaza numarul de elemente din tuple

'''
DICTIONAR = este o structura care stocheaza informatii in formatul cheie:valaore
'''

capitale = {
    'Romania': 'Bucuresti',
    'Italia': 'Roma',
    'Ukraina': 'Kiev'
}
print(capitale['Romania']) # accesarea informatiilor din dictionar in functie de cheie
print(capitale.get('Romania')) # idem
# cum sa actualizam o informatie
capitale['Romania'] = 'Cluj' # inlocuim o valoare pe baza de cheie
print(capitale['Romania'])
# cum adaugam o informatie noua
capitale['Rusia'] = 'Moscova'
print(capitale['Rusia'])
print(len(capitale))
#functia de stergere la dictionare
capitale.pop('Rusia')
print(capitale)

