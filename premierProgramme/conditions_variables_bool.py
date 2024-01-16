def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? : ")
    return reponse_nom


def demander_age(nom_personne):
    age_prochaine_integer = 0
    while age_prochaine_integer == 0:
        age_string = input(nom_personne + " Quel est votre age ? : ")
        try:
            age_prochaine_integer = int(age_string)
        except:
            print("ERREUR: l'age doit etre en nombre !")
    return age_prochaine_integer


nom1 = demander_nom()
nom2 = demander_nom()

age1 = demander_age(nom1)
age2 = demander_age(nom2)


def info_personnelles(nom, age):
    print()
    print("votre nom est " + nom + ", vous avez " + str(age) + "ans")
    print("L'année prochaine vous aurez " + str(age + 1) + "ans")

    """boolean = age <= 18
    print(boolean)
    if boolean:
        print("Vous etes mineur")
    else:
        print("Vous etes majeur")"""

    if age == 17:
        print("Vous etes presque majeur")
    elif age == 18:
        print("Felicitation! tout juste majeur")
    elif 18 < age < 67:
        print("Vous etes majeur")
    elif age > 68:
        print("Vous etes senior")
    elif age < 10:
        print("Vous etes enfant")
    else:
        print("Vous etes mineur")


info_personnelles(nom1, age1)
info_personnelles(nom2, age2)
