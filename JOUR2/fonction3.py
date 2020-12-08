#coding:utf8
"""
DEFINITION DES FONCTIONS
"""
def perimetre(a, b):
    """Méthode pour l'addition"""
    return (a + b)*2

def surface(a, b):
    """Méthode pour la soustraction"""
    return  a * b

# PROGRAMME PRINCIPAL (main)
x=int(input("saisir la longueur:"))
y=int(input("saisir la largeur:"))
print("Resultats périmètre={} et surface={}".format(perimetre(x,y),surface(x,y)))