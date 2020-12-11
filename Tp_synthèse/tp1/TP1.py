from connection import create_connection

new_conn = create_connection("TP1.db")

if new_conn is None:
    raise Exception("Erreur! impossible de se connecter à la base de données.")

def Ajouter(conn,montant,nomClient):
    cur = conn.cursor()
    cur.execute("SELECT c.solde FROM CompteBancaire c join Client_Compte mc on mc.idClient=c.idCompt join Client m on mc.idClient = m.idClient where c.nomClient = ?)", nomClient)
    solde = cur.get()
    
    new_solde= solde + montant
    print(new_solde)
    """
        print('le nouveau solde de {} est egal à {}'.format(nomClient,new_solde))
"""

def Retirer(conn,montant,idClient):
    cur = conn.cursor()
    cur.execute("SELECT c.solde FROM CompteBancaire c join Client_Compte mc on mc.idClient=c.idCompte join Client m on mc.idClient = m.idClient where m.idClient = ?)", idClient)
    solde = cur.get()
    decouvert=c.decouvert()
    try:
        new_solde= solde + montant
        print('le nouveau solde de {} est egal à {}'.format(nomClient,new_solde))
        assert ((solde - montant) > (solde + decouvert))
    except AssertionError:
        print ("Vous avez dépasser le montant autorisé! Vous pouvez essayer avec le montant {} comme plafond ".format(dec))

def  listerCompteAgence(conn,nomAgence):
    cur = conn.cursor()
    cur.execute("SELECT c.idCompte FROM CompteBancaire c join Compte_Agence mc on mc.idAgence=c.idCompte join Agence m on mc.idAgence = m.idAgence where c.nomAgence = ?)", nomAgence)
    rows = cur.fetchall()
    for Compte in rows:
        print(Compte)

def  listerCompteClient(conn,nomClient):
    cur = conn.cursor()
    cur.execute("SELECT c.idCompte FROM CompteBancaire c join Client_Compte mc on mc.idClient=c.idCompte join Client m on mc.idClient = m.idClient where c.nomClient = ?)", nomClient)
    rows = cur.fetchall()

    for Compte in rows:
        print(Compte)



#Programme Principal (Test Tp1)


new_conn = create_connection("TP1.db")

if new_conn is None:
    raise Exception("Erreur! impossible de se connecter à la base de données.")

Ajouter(new_conn,500,(1,))
Retirer(new_conn,500,('ZACK',))
listerCompteAgence(new_conn,('SAM',))
listerCompteClient(new_conn,('Benjamin',))