
#Exo 2: Ecrire un programme qui demande à l'utilisateur de saisir un nombre entier et qui indique selon le cas : Ce nombre est positif ou nul. Ce nombre est négatif 


a=int(input("saisir un nombre entier: "))
if (a==0):
    print("C'est null")
elif (a>0):
    print("C'est positif")
else:
    print("C'est negatif")