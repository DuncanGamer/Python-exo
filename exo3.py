#Exo 3: Ecrire un programme qui réalise la saisie par l’utilisateur d’un nombre et qui indique si ce nombre est divisible par 3 ou pas. On pourra par exemple utiliser le modulo (%) 

a=int(input("Sasir un nombre entier:"))
if (a%3==0):
    print(" Divisible par 3")
else:
    print("n'est pas divisible par 3")