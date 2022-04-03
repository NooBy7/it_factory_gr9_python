# Ne imaginam o echipa de fotbal pt teren sintetic.
# 3 Schimbari maxime admise
#
# Declara o Lista cu 5 jucatori
# Schimbari_efectuate = va jucati voi cu valori diferite
#
# Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
# Efectuam schimbarea
# Stergem jucatorul scos din lista
# Adaugam jucatorul intrat
# Afisam a intra x, a iesit y, mai aveti z schimbari
# Daca jucatorul nu e in teren:
# Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren'
# Afisati 'mai aveti z schimbari'
#
# Testati codul cu diferite valori

SCHIMBARI_MAXIME = 3
schimbari_efectuate = 0
schimbari_ramase = SCHIMBARI_MAXIME - schimbari_efectuate
echipa = {'j1','j2','j3','j4','j5'}
jucator_in = 'j6'
jucator_out = 'j1'
if jucator_out in echipa and schimbari_efectuate <SCHIMBARI_MAXIME:
    if jucator_in in echipa:
        print("Nu putem face schimbarea deoarece jucatorul introdus este deja in teren")
    else:
        echipa.remove(jucator_out)
        echipa.add(jucator_in)
        schimbari_ramase -= 1
        print(f"A intrat {jucator_in} si a iesit {jucator_out}. Mai aveti {schimbari_ramase} schimbari disponibile")
        print(f"Actuala echipa este {echipa}")
else:
    if schimbari_ramase<=0:
        print("Nu mai ai schimbari disponibile")
    print(f"Nu se poate efectua schimbarea deoarece jucatorul {jucator_in} nu este in teren")