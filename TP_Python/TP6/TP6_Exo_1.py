
L1 = [0]*3
L1[1] += 1
print( L1,"|",type(L1),"|",id(L1))

print(L1[0],"|",id(L1[0]))
print(L1[1],"|",id(L1[1]))
print(L1[2],"|",id(L1[2]))

# B) On remarque que les id de chaque valeurs de la liste sont identiques et ne change pas à chaque éxécution.
# C) Cependant quand des valeurs sont différentes, on remarque l'id est modifier.
# D) C'est bien un nouvel objet qui à été crée, on peut donc conlcure que les éléments d'une liste ont tous le même id si ils sont égaux, sinon leurs id diffèrent.