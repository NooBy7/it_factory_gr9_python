# pasaport = (input('introduceti validarea pasaportului , alegeti da sau nu : '))
# ambii_pariti = input('are ambii parinti , alegeti da sau nu: ')
# permisiune = input('Are permisiunea? DA/NU/NA: ')
# if pasaport == 'DA' and (ambii_pariti == 'DA' or permisiune == 'DA'):
#     print('Permite calatoria')
# else:
#     print('Nu permite calatoria')

print('--------------------')

NOTA_DE_TRECERE = 5 # o constanta se scrie cu litere mari si se dpreeste sa mi se schimbe
NOTA_DE_TRECERE_PURTARE = 7
nota_exament = int(input('Introdu nota de la examen'))
nota_purtare = int(input('Introdu nota de la purtare'))
if nota_exament >= NOTA_DE_TRECERE and nota_purtare >= NOTA_DE_TRECERE_PURTARE:
    print('Bravo ai trcut')
    if nota_exament == 10 and nota_purtare == 10 : # acest if se executa doar daca conditia anteriare este evaluata ca adevarata
        print('Felicitari esti premiant')
else :
    print('Nu ai trcut calsa! ')
