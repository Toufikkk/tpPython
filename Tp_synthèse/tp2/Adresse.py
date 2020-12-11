class Adresse:

	#Constructeur
	def __init__(self,rue,ville,codePostal):
		self._rue = rue
		self._ville = ville
		self._codePostal = codePostal

	@property
     	def _get_rue(self):
        
        	print("On accède à l'attribut rue !")
        	return self._rue
	
	@property
     	def _get_ville(self):
        
        	print("On accède à l'attribut ville !")
        	return self._ville

	@property
     	def _get_codePostal(self):
        
        	print("On accède à l'attribut codePostal !")
        	return self._codePostal

	@rue.setter
    	def _set_rue(self, r):

       		self._rue = r

	@ville.setter
    	def _set_ville(self, v):

       		self._ville = v

	@codePostal.setter
    	def _set_codePostal(self, cp):

       		self._codePostal = cp