
'''------------FOR------------'''
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for i in masini:
#     print(f'Masina mea preferata este {i} ')
'''----------FOR-EACH----------'''
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for marca in masini:
#     print(f'Masina mea preferata este {marca}')
# Aici ai facut de doua ori for each, dar niciodata for
# For-ul ar fi asa:
# for i in range(len(masini)):
#      print(f’Masina mea preferata este {masini[i]}’)
"""-----------------------------------------------------------"""
# i = 0
# while i < len(masini):
#     for marca in masini:
#        print(f'Masina mea preferata este {marca}')
#     i += 1
# Aici nu e nevoie si de for pentru ca iti va printa toate masinile de 8 ori
# Corect ar fi asa:
# i = 0
# while i < len(masini):
#     print(f'Masina mea preferata este {marca}')
#     i += 1
"""-----------------------------------------------------------"""
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for maj in masini[1:-1]:
#      print(f'Acestea le-am scris cu majuscule uite asa= ', maj.upper())
# else:
#      print(f'Acestea nu le-am modificat = ', masini[0], ' si ', masini[-1])
# Aici alta varianta ar fi:
# #2.Aceeasi lista Folositi un for else; Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimu
# # for i in range(len(masini)):
# #    if not(i==1 or i==len(masini)-1):
# #       print(masini[i].upper())
"""-----------------------------------------------------------"""
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for client_vrea in masini:
#      if client_vrea == 'Mercedes':
#          print(f'Clientul si-a gasit masina dorita adica un',client_vrea)
#          break
# Aici e ok dar nu ai pus si else-ul.
# Corect ar fi asa:
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for client_vrea in masini:
#      if client_vrea == 'Mercedes':
#          print(f'Clientul si-a gasit masina dorita adica un',client_vrea)
#          break
#      else:
#          print(f"Am gasit masina {client_vrea}. Mai cautam")
"""-----------------------------------------------------------"""
# # masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# # masini_vechi = []
# # nr = 0
# # for prezentare in masini:
# #     if prezentare == 'Lastun':
# #         nr = masini.index('Lastun')
# #         masini_vechi.append(prezentare)
# #         masini.remove('Lastun')
# #         masini.insert((nr), 'Tesla')
# #     elif prezentare == 'Trabant':
# #         nr = masini.index('Trabant')
# #         masini_vechi.append(prezentare)
# #         masini.remove('Trabant')
# #         masini.insert((nr), 'Tesla')
# #     else:
# #         pass
# # print(masini_vechi)
# # print(masini)
# Aici e partial corect.
# Te-ai complicat mult
# Exercitiul cerea sa suprascrii elementele, nu sa le stergi. Deci corect ar fi fost asa:
# masini_vechi = []
# for i in range(len(masini)):
#     if masini[i] == 'Lastun' or masini[i]=='Trabant':
#         masini_vechi.append(masini[i])
#         masini[i]='Tesla'
# print(masini)
# print(masini_vechi)
"""-----------------------------------------------------------"""
# # masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# # for prezentare in masini:
# #     if prezentare == 'Lastun':
# #         continue
# #     elif prezentare == 'Trabant':
# #         continue
# #     print(f's-ar putea sa va placa masina', prezentare)
# Aici e ok, dar varianta mai simpla ar fi fost:
# # masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# # for prezentare in masini:
# #     if prezentare == 'Lastun' or prezentare == 'Trabant':
# #         continue
# #     print(f's-ar putea sa va placa masina', prezentare)
"""-----------------------------------------------------------"""
# pret_masini = {
#      'Dacia': 6800,
#      'Lastun': 500,
#      'Opel': 1100,
#      'Audi': 19000,
#      'BMW': 23000 }
# buget = 15000
# for oferta in pret_masini.items():
#      if oferta[1] <= buget:
#          print(f'Pentru un buget de sub 15000 euro puteti alege masina', oferta[0])
# Aici e corect.
# Alta varianta ar fi fost:
# buget = 15000
#
#
# for masina in pret_masini.keys():
#      if pret_masini[masina] <= buget:
#         print(f'Pentru un buget de sub 15000 euro, puteti alege masina {masina}')
"""-----------------------------------------------------------"""
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# nr_max = None
# for nr in numere:
#      if (nr_max is None or nr > nr_max):
#          nr_max = nr
# print(f'Cel mai mare numar este:' , nr_max)
# Aici e ok, dar poti sa initializezi nr_max direct cu 0, si atunci nu ai mai avea nevoie de conditia nr_max is None in if
"""-----------------------------------------------------------"""
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# for nr in alte_numere:
#      if nr < 0:
#          numere_negative.append(nr)
#          if (nr % 2) == 0:
#              numere_pare.append(nr)
#          else:
#              numere_impare.append(nr)
#      else:
#          numere_pozitive.append(nr)
#          if (nr % 2) == 0:
#              numere_pare.append(nr)
#          else:
#              numere_impare.append(nr)
# Aici e ok. doar ca te-ai complicat.
# Mai usor ar fi asa:
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# for nr in alte_numere:
#     if nr%2==0:
#         numere_pare.append(nr)
#         if nr < 0:
#             numere_negative.append(nr)
#         else:
#             numere_pozitive.append(nr)
#     else:
#              numere_impare.append(nr)

"""-----------------------------------------------------------"""
# La asta nu afiseaza ce trebuie.
# Corect ar fi asa:
# x = int(input('Introduceti un numar care da inaltimea si baza piramidei:\n'))
# for i in range(1, x+1) :
#     print(f'{i}' * i)

"""-----------------------------------------------------------"""