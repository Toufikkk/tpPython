#coding:utf8
"""
DEFINITION DES FONCTIONS
"""
def ma_fonction1():
	print("Ma première fonction")

def ma_fonction2(a,b):
	print("Les valeurs des paramètres sont :{} et {}".format(a,b))	

def ma_fonction3(a,b=12,c=3):	
	print("Les valeurs des paramètres sont :{} , {} et {}".format(a,b,c))
def ma_fonction4(a,b):
	return a+b
def ma_fonction5(*params):
	print("paramètres",params)

def get_player_position():
	posX = 150
	posY = 86
	return (posX,posY)

"""
PROGRAMME PRINCIPAL
"""
#appel normal
ma_fonction1()
ma_fonction2(15, 75)
ma_fonction3(15,75,100)
#valeur par defaut
ma_fonction3(15,75)
ma_fonction3(15)
#Etiquettes
ma_fonction3(c=5, b=4, a=3)
#ma_fonction3()
#appel d'une fonction avec valeur de retour
resultat = ma_fonction4(4,5)
print(resultat)
#appel d'une fonction à parametres variables
ma_fonction5(2)
ma_fonction5(2, 'titi')
ma_fonction5(2, 'test',5,6)

#appel d'une fonction qui retourne un tuple
print(get_player_position())