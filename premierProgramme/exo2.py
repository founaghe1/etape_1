#nom = input("Quel est votre nom : ")

nom = ""
while nom == "":
    nom = input("Quel est votre nom ? : ")

ageProchaineInt = 0
while ageProchaineInt == 0:
    ageStr = input("Quel est votre age ? : ")
    try:
        ageProchaineInt = int(ageStr)
    except:
        print("ERREUR: l'age doit etre en nombre !")

print("votre nom est " + nom + ", vous avez " + ageStr + "ans")
print("L'année prochaine vous aurez " + str(ageProchaineInt + 1) + "ans")


