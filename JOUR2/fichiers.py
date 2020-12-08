try: 
	with open("depart.txt", 'r') as fic:
		# récupération du contenu
		content = fic.read()
		#affichage
		print(content)
#Gestion de l'erreur
except FileNotFoundError:
	print("fichier introuvable")

try:
	with open("arrivee.txt",'w') as fic:
		#ecrire le contenu du fichier depart dans le fichier arrivee
		fic.write(content)

#gestion de l'erreur
except FileNotFoundError:
	print("fichier introuvable")