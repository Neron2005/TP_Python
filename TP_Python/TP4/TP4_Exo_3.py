
vmax = 3
v1 = []
v2 = []
c = 1
d = 1
m = 0
while True:
    a = int(input("Entrez la taille des vecteurs : "))
    if a < 1 or a >vmax:
        print("La taille doit être comprise entre 1 et 3")
    print("Saisie du premier vecteur ")
    for i in range(3):
        x = int(input(f"Donnes la composante {c} du vecteur 1 : "))
        c += 1
        v1.append(x)
    print("Saisie du deuxième vecteur ")
    for a in range(3):
        y = int(input(f"Donnes la composante {d} du vecteur 2 : "))
        d += 1
        v2.append(y)
    for z in range(3):    
        p = v1[0]
        d = v2[0]
        m += p*d
        del v1[0]
        del v2[0]
    print(f"Le produit scalaire de v1 par v2 est égale à {m}")
    break