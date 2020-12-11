import sys
sys.path.append('../src/') 
from TP1 import *
import unittest
class TestTP1(unittest.TestCase):
    
    def test_Ajouter(self):
        print('je test l ajout du montant')
    def test_Retirer(self):
        print('je test le retrait d argent')
    def test_listerCompteAgence(self):
        print('je test listerCompteAgence')
    def test_multi(self):
         print('je test listerCompteClient')    

if _name_ == '_main_':
    unittest.main()