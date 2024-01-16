# Les variables string
fullName = "Mohamed Diallo"
print("hello python c'est moi "+ fullName + ".")
print("C'est bien " + fullName + ".")

#interaction avec le user
name = input("What's your name please ? ")
print("My name is " + name)

#multi line comment
"""La suite de mon
programme en python 
est pour bientot"""

# Les variables numeriques
#nom = "Diallo"
#print(type(nom))
#age = 25
#ageProchain = age + 1
#print(type(age))

"""print("Vous etes " + nom + ", vous avez " + str(age) + "ans")
print("L'année prochaine vous aurez " + str(ageProchain) + "ans")"""

#Conversion de string en int et Gestion des ERREURS

nom = input("Tapez votre nom ")
age = input("tapez votre age ")

try:
    ageProchain = int(age) + 1
except:
    print("ERROR: Vous devez entrer un entier pour l'age")
else:
    print("Vous etes " + nom + ", vous avez " + str(age) + "ans")
    print("L'année prochaine vous aurez " + str(ageProchain) + "ans")




