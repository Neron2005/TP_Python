def ajouter_elt(lst=[0,1,2], elt=3):
    lst.append(elt)  
    return lst

def ajouter_carac(ch=["abc"],elt="d"):
    ch.append(elt)
    return ch

print(ajouter_elt(),id(ajouter_elt))
print(ajouter_carac(),id(ajouter_carac))

# A) [0,1,2,3]
# B) On remarque que la valeur 3 c'est ajouter à la liste
# D) ["abc","d"]
# C) On remarque que l'ID de la liste change à chaque éxécution