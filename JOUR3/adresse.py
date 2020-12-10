# Ma classe
class Adresse:
	def __init__(self,rue, numero,code_postal,ville):
		assert len(rue) > 3 and len(rue) < 25, "la rue doit contenir entre 3 et 25 caractères"
		self.rue = rue
		self.numero = numero
		self.code_postal = code_postal
		self.ville = ville
	#redefinition de la méthode d'affichage
	def __str__(self):
		return "{} \n{}\n{}\n{}".format(self.rue,self.numero,self.code_postal,self.ville)
#Mère
class Personne:
	#constructeur
	def __init__(self,nom,prenom,age):
		self.nom = nom
		self.prenom = prenom
		self.age = age
	#redefinition de la méthode d'affichage
	def __str__(self):
		return "{} \n{}\n{}\n{}".format(self.nom,self.prenom,self.age)
	# definition des autres autres methodes
	def se_nourrir(self):
		print("Je mange ...")

#Classe Fille
class Etudiant(Personne):
	def __init__(self,nom,prenom,age,moyenne):
		Personne.__init__(self,nom,prenom,age)
		self.moyenne = moyenne 
	def se_nourrir(self):
		print("Je mange au fast food...")

#Classe Fille
class Professeur(Personne):
	def __init__(self,nom,prenom,age,matiere_enseigne):
		Personne.__init__(self,nom,prenom,age)
		self.matiere = matiere_enseigne
	def se_nourrir(self):
		print("Je mange au restaurant...")

# Heritage multiple
class Doctorant(Etudiant, Professeur):
	pass
#Classe Voiture : getter / setter
class Voiture:

	nb_voitures =0
	def __init__(self):
		self._roues = 4

	#getter
	@property
	def roues(self):
		print("Récuperation du nombre des roues")
		return self._roues
	#setter
	@roues.setter
	def roues(self, r):
		print("changement du nombre de roues")
		self._roues = r	

def change_nb_voitures(cls, nouveau_nombre):
	nb_voitures = nouveau_nombre


change_nb_voitures = classmethod(change_nb_voitures)	

# Programme principal
a1 = Adresse("rue de paris","5","75000","Paris")
print(a1)
p1 = Personne("zec","union",40)
et1 = Etudiant("toto","tata",25,26)
prof1 = Professeur("eddy","CHRISTIAN",35,"C#")
# connaître le type d'un objet
print(type(p1))
print(type(et1))
print(type(prof1))
# Appel des méthodes
p1.se_nourrir()
et1.se_nourrir()
prof1.se_nourrir()
#appel de voiture
ma_voiture = Voiture()
print(ma_voiture.roues)
ma_voiture.roues = 5
print(ma_voiture.roues)
#fonction dir pour avoir l'aperçu des methodes de l'objet
print(dir(ma_voiture))
#attribut __dict__ donne les valeurs des attributs
print(ma_voiture.__dict__)
#appel de method de classe
print("nombre de voitures = ".format(Voiture.change_nb_voitures))