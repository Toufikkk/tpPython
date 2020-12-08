#BASE DE DONNEES 
from sqlite3 import *
#CRUD : Create, Read, Update, Delete

#Connexion
connection = connect("base.db")
cursor = connection.cursor()
#requete
new_etudiant = (cursor.lastrowid, "ZEC", "Union",20)
cursor.execute('INSERT INTO etudiant VALUES(?,?,?,?)',new_etudiant)
connection.commit()
print("le nouvel utilisateur a ete ajoute en BDD")
#restitution de resultat

#fermeture
cursor.close()
connection.close()