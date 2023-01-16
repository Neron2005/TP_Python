import random

def generer(nbr,vmin,vmax):
    for i in range(n):
        a = random.randint(vmin,vmax)
        tab.append(a)

def combienInferieur(table, vseuil):
    c = 0
    for a in range(len(tab)):
        for i in tab:
            c += 1
            i = tab[c]
            if i > s:
                total = c-1
            break
        break
        
n = int(input("Combien de valeurs souhaitez-vous générer ? : "))
y = int(input("Veuillez renseigner la valeur minimal de l'interval : "))
z = int(input("Veuillez renseigner la valeur maximal de l'interval : "))
tab = []
generer(n, y, z)
tab.sort()
print(tab)

while True:
    m = input("voulez préciser le seuil ? : ")
    if m in ["oui", "o"]:
        s = int(input("Entrez la valeur du seuil : "))
        break
    elif m in ["non", "n"]:
        print("Le seuil sera donc admis à 30")
        s = 30
        break
    else:
        print("réponse non valide, veuillez répondre par (oui | non) ou (o | n)")
                
total = 0
combienInferieur(tab,s)
print(f"Il y a {total} valeurs inférieurs à {s}")