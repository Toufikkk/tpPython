#coding:utf8

def add(a, b):
	return a + b

def sous(a, b):
	return a - b
	
def mult(a, b):
	return a * b 
	
def div(a, b):
	return a/b
	
#PROGRAMME PRINCIPAL
print("Veuillez saisir les informations de la calcul")

x=int(input("saisir le premier chiffre:"))
y=int(input("saisir le deuxiem chiffre"))

print("resultat addition:{}".format(add(x,y)))
print("resultat soustraction:{}".format(sous(x,y)))
print("resultat multiplication:{}".format(mult(x,y)))
print("resultat division:{}".format(div(x,y)))