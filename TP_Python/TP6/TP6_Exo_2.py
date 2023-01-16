def ajouter_elt(lst, elt):  
    lst.append(elt)  
    return lst

l1 = [0,1,2]
l2 = ajouter_elt(l1,10)

print(l1,type(l1),id(l1))
print(l2,type(l2),id(l2))

# On remarque que les deux listes possèdent le même ID