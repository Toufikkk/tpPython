#coding:utf8
prenom = str(input("Quel est votre prenom?"))
nom= str(input("Quel est votre nom?"))
age = int(input("Quel est votre age?"))

#Affichage des informations saisies.
print("Tu t'appelles {} {} et tu as {} ans".format(prenom,nom,age))

#Calcul l'age dans 10 ans
age10 = age + 10
print("Tu auras {} dans 10 ans".format(age10))