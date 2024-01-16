"""
n = 0
while n < 4:
    print("la valeur de n est: " + str(n))
    n = n + 1


motDePass = ""

while not motDePass == "passer":
    motDePass = input("Quel est le mot de passe ? ")

print("mot de passe correct")

"""
nom = input("Tapez votre nom : ")

ageProchainInt = 0
while ageProchainInt == 0:
    ageStr = input("tapez votre age : ")
    try:
        ageProchainInt = int(ageStr)
    except:
        print("ERROR: Vous devez entrer un entier pour l'age")

print("Vous etes " + nom + ", vous avez " + str(ageProchainInt) + "ans")
print("L'année prochaine vous aurez " + str(ageProchainInt + 1) + "ans")
