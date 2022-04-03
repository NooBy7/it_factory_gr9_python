
'''

LISTE

'''

# lista1 = []  # lista este creeata
# lista1.append(10)  # se adauga in lista
# lista1.append(11)  # de fiecare data succesiv
# lista1.append(12)  # una dupa alta
# lista1.append(14)  # de fiecare data pe indexul urmator
# print(lista1)
# lista1.append(int(input('valoare: ')))  # introducere de la tasatatuira succesiv un integer , NU SE POATE INDEXA POZITIA UNDE VA FI INTRODUS,
# print(lista1)
# lista1.insert(3, 15)  # se adauga la pozitia ceruta elementul, restul fiind impins mai incolo
# lista1.insert(10, int(input('inca o valoare: ')))
# print(lista1)
# retinere = lista1.pop(-1)
# print(lista1)
# retinere = lista1.pop()  # fara indexi sterge ultimul element din lista SI TINE "MINTE" CE A STERS deoarece nu se stia doar pozitia nu si valoare ce se va sterge
# print(lista1)
# print(retinere)
# retinere2 = lista1.remove(15)  # nu tine minte ce a sters , deoarece aici sa sters cunoscand valoarea ce se doarea a fi sters
# print(lista1)
# print(retinere2)
'''
In Python la un IF daca o variabila are lungime (len 0) sau continutul este Zero sau 0.0 este considerat
ca si expimare boolean ,cel mai PYTHONIC mod de a verifica daca o lista este goala sau nu
'''

# lista_1 = [3, 1, 0, 2]
# print(lista_1)
# lista_2 = [6, 5, 4]
# print(lista_2)
# lista_3 = lista_1 + lista_2
# lista_3.sort()
# if lista_3:
#     print('The list is not empty ',lista_3)
# else:
#     print('The list is empty')
# lista_2.clear()
# if lista_2:
#     print('The list is not empty ',lista_2)
# else:
#     print('The list is empty',lista_2)
# lista_1.clear()
# if not lista_1:
#     print('The list is empty',lista_1)
# else:
#     print('The list is not empty ', lista_1)

'''
metoda BOOL si LEN
Este asemanatoare modul de functionare doar trebiue verificat cum se pune intrebarea pentru IF
'''
# print('--------------------')
# l1 = ["Hire", "the", "top", "1%", "freelancers"]
#
# l2 = []
#
# if bool(l2):
#     print("list is empty")
# else:
#     print("list is not empty")
#
# # Output: "list is empty"
# print('--------------------')
# l1 = ["Hire", "the", "top", "1%", "freelancers"]
#
# l2 = []
#
# if len(l2):
#     print("list is not empty")
# else:
#     print("list is empty")
#
# # Output: "list is empty"
# print('--------------------')
# l1 = ["Hire", "the", "top", "1%", "freelancers"]
#
# l2 = []
#
# if len(l2) == 0:
#     print("list is empty")
# else:
#     print("list is not empty")
#
# # Output: "list is empty"
# print('--------------------')