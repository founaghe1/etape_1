def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? : ")
    return reponse_nom


def demander_age():
    age_prochaine_integer = 0
    while age_prochaine_integer == 0:
        age_string = input("Quel est votre age ? : ")
        try:
            age_prochaine_integer = int(age_string)
        except:
            print("ERREUR: l'age doit etre en nombre !")
    return age_string, age_prochaine_integer


nom = demander_nom()
age_str, age_prochaine_int = demander_age()

print("votre nom est " + nom + ", vous avez " + age_str + "ans")
print("L'année prochaine vous aurez " + str(age_prochaine_int + 1) + "ans")


