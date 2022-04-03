'''
16.
Ne imaginam o echipa de fotbal pt teren sintetic.
3 Schimbari maxime admise

Declara o Lista cu 5 jucatori
Schimbari_efectuate = va jucati voi cu valori diferite

Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
-	Efectuam schimbarea
-	Stergem jucatorul scos din lista
-	Adaugam jucatorul intrat
-	Afisam a intra x, a iesit y, mai aveti z schimbari
Daca jucatorul nu e in teren:
-	Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
-	Afisati ‘mai aveti z schimbari’

Testati codul cu diferite valori

Google search hint
“how to check if item is in list python”
'''

echipa = ['1.Hagi', '2.Petrescu', '3.Popescu','4.Munteanu', '5.Moldovan']
rezerva = ['6.Mutu', '7.Chivu', '8.Radoi']
nr_schimburi = 3
# print(echipa)
# print(rezerva)
decizia = input('Echipa care joaca este ' +  str(echipa) + '\niar pe banca de rezerva avem ' + str(rezerva) + '\nsi mai aveti ' + str(nr_schimburi) + ' schimburi' + '\nDoriti sa facem un schimb(DA sau NU)')
decizia = decizia.upper()
if decizia == 'DA':
    nr_echipa = int(input('Jucatorul care va fi schimbat se afla pe pozitia nr '))
    jucator_jos = echipa.pop(nr_echipa - 1)
    nr_rezerza = int(input('Jucatorul care va intra e afla pe pozitia nr '))
    jucator_sus = rezerva.pop(nr_rezerza - 1)
    print(jucator_jos)
    print(jucator_sus)
    if nr_schimburi > 0 and nr_echipa>0<=5 and nr_rezerza>0<=3 :
        nr_schimburi -= 1
        echipa.append(jucator_sus)
        print(echipa)
        rezerva.append(jucator_jos)
        print(rezerva)
    elifif nr_schimburi > 0 and nr_echipa > 0 <= 5 and nr_rezerza > 0 <= 3:

    else
        print('S-au facut maximul de 2 schimbari')
else:
    print('Echipa a ramas nemodifica')
