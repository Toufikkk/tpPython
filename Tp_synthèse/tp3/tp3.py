#coding:utf8
class Alphabet:
	def __init__(self, nom):
		self.lettre_nom = nom
	def info(self):
		print("Je suis une lettre de l'alphabet")
	def test1(self):
		print("Fonction test1() de la classe Alphabet")
	def test2(self):
		print("Fonction test2() de la classe Alphabet")		

class Mot:
	def info(self):
		print("Je suis un mot")
	def test1(self):
		print("Fonction test1() de la classe Mot")
	def test3(self):
		print("Fonction test3() de la classe Mot")

class Accent:
	def info(self):
		print("Je suis une lettre accentuée")
	def test2(self):
		print("Fonction test2() de la classe Accent")
	def test3(self):
		print("Fonction test3() de la classe Accent")

class A(Alphabet):
	def info(self):
		print("Je suis un A")
	def test1(self):
		print("Fonction test1() de la classe A")

class Abracadabra(Mot):
	def test1(self):
		print("Fonction test1() de la classe Abracadabra")

class AGrave(A, Accent, Abracadabra):
	lettreA = True
	lettreAccent = True 
	

aAccentGrave = AGrave("à")
aAccentGrave.lettre_nom
aAccentGrave.info()
aAccentGrave.test1()
aAccentGrave.test2()
aAccentGrave.test3()														