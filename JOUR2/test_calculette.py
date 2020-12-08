#fichier de test unitaire
import unittest
"""
DEFINITION DES METHODES DE TEST DANS LA CLASSE DE TEST
"""
class TestCalculatrice(unittest.TestCase):
	def test_add(self):
		c = Calculette()
		assert c.add(1, 4) == 5
		assert c.add(10, 4) == 14
		assert c.add(1, 4) == assert c.add(5,0)
		assert c.add(1, 4) == c.add(4,1)

"""
LANCEMENT DES TEST
"""		
if __name__ == '__main__':
	unittest.main()