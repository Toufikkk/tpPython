#BASE DE DONNEES 
from sqlite3 import *
#CRUD : Create, Read, Update, Delete

#Connexion
connection = connect("GestionFormation.bdd.db")
cursor = connection.cursor()

#fonctions pour les Ajouts en BDD

new_Matiere=(cursor.lastrowid, "java", "pyhton","c#","html","css")
cursor.execute('INSERT INTO Matiere VALUES(?,?,?,?,?)',new_Matiere)
new_Cursus=(cursor.lastrowid, "Devops", "Developpeur Java","Developpeur c#","Developpeur c#")
cursor.execute('INSERT INTO Cursus VALUES(?,?)',new_Cursus)
new_Etudiant=(cursor.lastrowid, "michel", "corine","benjamin","cothilde","anais")
cursor.execute('INSERT INTO Etudiant VALUES(?,?,?,?,?)',new_Etudiant)

connection.commit()
print("succesfully added on BDD")

cursor.execute('SELECT * FROM Etudiant, Matiere, Cursus')
print(cursor.fetchall())

#fonctions pour les modif

modif_etudiant=('lionel','Messi',33,1)
cursor.execute('UPDATE etudiant SET nom=?, prenom=?, age=? WHERE id=?',modif_etudiant)
connection.commit()
print("le nouvel utilisateur a ete mis a jour")

modif_Matiere=('math','physique','java','c#','html')
cursor.execute('UPDATE Matiere SET idMatiere=?, nomMatiere=?',modif_Matiere)
connection.commit()
print("la mise a jour s'est deroulé avec succée")

#fonctions pour supprimer

del_Cursus=(1,)
cursor.execute('DELETE from Cursus WHERE id=?',del_Cursus)
connection.commit()
print("le cursus a correctement ete supprime")

cursor.execute('SELECT * FROM Matiere')
print(cursor.fetchall()) 


del_etudiant=(2,)
cursor.execute('DELETE from etudiant WHERE id=?',del_etudiant)
connection.commit()
print("l'utilisateur a ete supprime")

cursor.execute('SELECT * FROM etudiant')
print(cursor.fetchall())

del_Matiere=(3,)
cursor.execute('DELETE from Matiere WHERE id=?',del_Matiere)
connection.commit()
print("la matiere a correctement ete supprime")

cursor.execute('SELECT * FROM Matiere')
print(cursor.fetchall())




#fermeture
cursor.close()
connection.close()