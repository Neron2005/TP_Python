e = int(input("Nombres d'étudiants durant l'examen ? : "))
moyenne = 0.00
notes = []
compteur = 1
somme = 0
t = 0
while t != e:
    for i in range(e):
        n = int(input(f"Qu'elle est la note du {compteur} élève ? :  "))
        if n < 0 or n >20:
            print("erreur")
            break
        compteur += 1
        notes.append(n)
        somme += n
    break
    
moyenne = somme/e
print(f"Moyenne de classe : {moyenne}\n")
print("N° | Notes | écart à la moyenne")

for a in range(1,e+1):
    a = notes[0]
    print(f"{a}  | {notes[0]}     | {a-moyenne} ")
    del notes[0]
    