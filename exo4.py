


#Exo 4: Écrire un programme qui détermine la valeur de la racine carrée d’un entier sans jamais utiliser la fonction racine carrée.

a=float(input("Sasir un nombre entier: "))

if (a>0):
    abas = -a
    ahaut = a
    i = 0
    while (ahaut-abas>0.001): 
        i = i+1
        if(((abas+ahaut)/2)*((abas+ahaut)/2)<a):
            abas=(abas+ahaut)/2
        else:
            ahaut=(ahaut+abas)/2
    print(str(abas) + " et " + str(ahaut))
    a = ahaut * abas
    print(a)
    print("nombre d'iterations: " + str(i))
