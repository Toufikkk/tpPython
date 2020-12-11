class Personne:
	global sexe
	sexe = ["M", "F"]
	
	#Constructeur
	def __init__(self,nom, sexe):
		self._nom = nom
		self._sexe = sexe
		self._adresses = []
	

	@property
     	def _get_nom(self):
        
        	print("On accède à l'attribut nom !")
        	return self._nom
	
	@property
     	def _get_sexe(self):
        
        	print("On accède à l'attribut sexe !")
        	return self._sexe


	@nom.setter
    	def _set_nom(self, n):

       		self._nom = n

	@sexe.setter
    	def _set_sexe(self, s):

       		self._sexe = s

	#Methodes de gestion de la liste des adresses
	def get_adresses(self):
		return self._adresses

	def add_adresses(self,a):
		if a not in self._adresses:
			self._adresses.append(a)

	def remove_adresses(self,a):
		if a in self._adresses:
			self._adresses.remove(a)


	def find_by_nom(self,nom):
        if nom in self._nom:
        	return self._adresse
        else:
            return 'NULL'