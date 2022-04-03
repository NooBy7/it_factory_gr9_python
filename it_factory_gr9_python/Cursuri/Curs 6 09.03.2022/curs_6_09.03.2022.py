"""
FUNCTII SIMPLE
"""
# def say_hi():
#     print('Hi')
#
# say_hi()
"""
FUNCTII CU PARAMETRII
"""
# def say_hi_1(user, varsta, ocupatie):
#     print(f'Buna {user}, ai {varsta} ani, si esti {ocupatie} ')
#
# nume = input('Introdu userul')
# ani = input('Introdu varsta')
# job = input('Introdu ocupatia ta')
# say_hi_1(nume , ani , job)
print('----------------')

nume_input = {'Marian':{35:'manager'} , 'Norbi':{30,'vanzator'}, 'Alexandra':{20:'marketing'}, 'Roxy':{18,'elon musk'}}
for k,v in nume_input.items():
    say_hi_1(nume_input[k]), nume_input[k]
print('----------------')
# def say_hi_v2(user):
#     print(f'Hi {user}')
# nume_input = ['Alex', 'Roxy', 'Norbi']
# for nume in nume_input:
#     say_hi_v2(nume)
print('----------------')

# def calculeaza_impozit(valoare_salariu):
#     if valoare_salariu <4000:
#         tax = 0
#     elif valoare_salariu >= 4000 and valoare_salariu < 5000 :
#         tax = 0.10
#     elif valoare_salariu >= 5000 and valoare_salariu< 33500 :
#         tax = 0.22
#     else:
#         tax = 0.4
#     salariu_impozat = valoare_salariu-valoare_salariu*tax
#     impozit = valoare_salariu*tax
#     return f'taxa aplicata a fost de {tax} iar salariul dupa impozit {salariu_impozat} impozitu este de {impozit}'
# valoare_salariu = int(input('introduceti salariul: '))
# taxa=calculeaza_impozit(valoare_salariu)
# # print(taxa)
# print(calculeaza_impozit(valoare_salariu))



#exercitiu cu bilete de avion:
#bilet avion <10 ani = 0 ; 10-18 = -50% ; 18-65 = 100% ; >65=0.

# def calculeaza_pret_bilet(varsta, pret_bilet):
#     while varsta<0:
#         varsta = int(input('Varsta incorecta. Va rog sa introduceti inca o data'))
#     if varsta < 10 or varsta>65:
#         pret_bilet=0
#         print('Pret zero')
#     elif varsta>=10 and varsta<18:
#         pret_bilet = pret_bilet-pret_bilet*0.5
#         print('pret 1')
#     elif varsta>=18 and  varsta<65:
#         pret_bilet=pret_bilet
#         print('pret 2')
#     else:
#         print('Varsta incorecta. Va rugam incercati din nou: ')
#     # return pret_bilet
#     return f'Aveti varsta de {varsta}, pretul biletului este de {pret_bilet} lei'
#
# varsta = -1
# pret_bilet = 100
#
# pret_final=calculeaza_pret_bilet(varsta, pret_bilet)
# print(pret_final)





















