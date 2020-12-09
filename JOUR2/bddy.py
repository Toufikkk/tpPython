#BASE DE DONNEES 
from sqlite3 import *
#CRUD : Create, Read, Update, Delete

#Connexion
connection = connect("base.db")
cursor = connection.cursor()
#requete
"""
new_etudiant = (cursor.lastrowid, "ZEC", "Union",20)
cursor.execute('INSERT INTO etudiant VALUES(?,?,?,?)',new_etudiant)
connection.commit()
print("le nouvel utilisateur a ete ajoute en BDD")
"""
"""
cursor.execute('SELECT * FROM etudiant WHERE id=?')
print(cursor.fetchall())
"""
"""
mon_etudiant=1,
cursor.execute('SELECT * FROM etudiant WHERE id=?',mon_etudiant)
print(cursor.fetchone())
"""
"""
modif_etudiant=('ZEC','UNION',20,1)
cursor.execute('UPDATE etudiant SET nom=?, prenom=?, age=? WHERE id=?',modif_etudiant)
connection.commit()
print("le nouvel utilisateur a ete mis a jour")
"""
del_etudiant=(2,)
cursor.execute('DELETE from etudiant WHERE id=?',del_etudiant)
connection.commit()
print("l'utilisateur a ete supprime")

cursor.execute('SELECT * FROM etudiant')
print(cursor.fetchall())

#restitution de resultat

#fermeture
cursor.close()
connection.close()