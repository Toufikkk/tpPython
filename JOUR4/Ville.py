#coding:utf8
class ville:
	def __init__(self, nomVille):  
        self.nomVile = nomVille 
        self.batiments = []
       
    def __del__(self):  
        print("le nom de la ville est {}".format(self.nomVille))  
  
class Batiment:  
    def __init__(self, nomBat):  
        self.nomBat = nomBat 
  
    def __del__(self):  
        print("le nom du batiment est {}".format(self.nomBat))  
  
class Entreprise:  
    def __init__(self, nomEntr):  
        self.nom = nom  
        self.batiments = [] 
        self.employes = []  
  
    def __del__(self):  
        print("nombre de batiments d'une Entreprise {}".format(self.nom))  
  
    def recrute(self, employe):  
        self.employes.append(employe)  
 
    def nombreDeBatiments(self):  
        print("l'Entreprise{} possède {} bâtiment(s)".format(self.nom,  
		len(self.batiments)))  
  
class Employe:  
    def __init__(self, nom,prenom):  
        self.nom = nom  
  		self.prenom = prenom
    def __del__(self):  
        print(" {}".format(self.nom))  