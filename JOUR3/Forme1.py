#TP geometrie
class Form:
	def __init__(self, x,y):
		self.x = x
		self.y = y

	def calculer_distance(self):
		print('je calcule la distance')

	def calculer_perimetre(self):
		print('je calcule le calculer_perimetre')		

	def afficher(self):
		print('je calcule le perimètre')

class Rectangle(Form):
	def __init__(self,x,y):
		Form.__init__(self,x,y)					

	def calculer_perimetre(self):
		perimetre = self.x * self.y
		return 'le perimetre est {}'.format(perimetre)	

	def __str__(self):
		print('les coordonnées du rectangle sont {} {}'.format(self.x, self.y))	