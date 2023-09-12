#exercice 4:

nombre_de_chiffres_pairs = 0
nombre_de_chiffre_impairs = 0
for something in range(1,10):
    #modulo pour déterminer si le chiffre est pair
    if (chiffre%2) == 0:
        print("%d est pair."%chiffre)
        nombre_de_chiffre_pairs +=1

    else:
        print("%d est impair."%chiffre)
        nombre_de_chiffre_impairs +=1

print("Il y a "+str(nombre_de_chiffre_pairs)+ "chiffres pairs et "+str(nombre_de_chiffre_impairs)+" chiffres impairs")
