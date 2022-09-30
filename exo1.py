
#Exo 1: Ecrire un programme qui demande à l’utilisateur 3 nombres entiers positifs et plus petits que 40000, 
#puis effectue la moyenne de ces trois nombres et affiche la valeur de cette moyenne. Le code n'effectuera pas de vérification concernant l'intervalle de 0 à 40000.

from multiprocessing.resource_sharer import stop


a=int(input("Sasir un nombre entier positif et plus petit que 40000: "))

if (0<a<4000):
    b=int(input("Sasir un nombre entier positif et plus petit que 40000: "))
    if (0<b<4000):
        c=int(input("Sasir un nombre entier positif et plus petit que 40000: "))
        if (0<c<4000):
            moyenne=(a+b+c)/3
            print(moyenne)
   