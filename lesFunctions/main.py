#definition d'une function et parametres
def infos_personnelles(nom, age):
    print("Je m'appelle", nom + ", j'ai", age, "ans")
    print("Le nom comporte", len(nom), "caracteres")

#appel d'une function
infos_personnelles("mohamed", 22)


#Les parametres optionnelles
def affiche_infos_personnelles(nom="", age=0):

    if age == 0 and nom == "":
        print("Il n'existe ni de nom, ni d'age.")
    elif age == 0:
        print("Son nom est ", nom)
    else:
        print("Son nom est", nom + ", il a", age, "ans")

affiche_infos_personnelles()


#Le return
def est_majeur(age2):
    if age2 >= 18:
        return True
    return False

print("est-il majeur ?", est_majeur(15))

age2 = 17
print("Son age est ", age2)
if est_majeur(age2):
    print("Il est majeur")
else:
    print("Il est mineur")


def recuperer_infos_personne(num_personne):
    nom_personne = input("Nom de la personne " + str(num_personne) + " : ")
    age_personne = input("L'age de la personne " + str(num_personne) + " : ")
    return nom_personne, age_personne


def affiche_infos_personne(num_personne, nom, age):
    print("La personne", num_personne, "est", nom, "son age est", age, "ans")
    print("le nom comporte", len(nom), "caracteres")


#refactorisation du code
def recuperer_afficher_infos_personne(num_personne):
    nom, age = recuperer_infos_personne(num_personne)
    affiche_infos_personne(num_personne, nom, age)


#recuperer_afficher_infos_personne(1)
#recuperer_afficher_infos_personne(2)
#recuperer_afficher_infos_personne(3)

nb_personne = 1

for i in range(nb_personne):
    recuperer_afficher_infos_personne(i + 1)


# Exo: Table de Multiplication


def afficher_table_de_multiplication(n, min=12, max=10):
    if min > max:
        print("ERROR: La valeur de depart est superieur à la valeur d'arriver")
        return

    for i in range(min, max + 1):
        print(i, "X", n, "=", i * n)

print("Exo: Table de Multiplication")
afficher_table_de_multiplication(5, max=12)


# Exo: Le Questionaire

'''
titre = question[0]
choix = question[1]
bonne_reponse = question[2]
'''


def questionaire(question):
    choix = question[1]
    choix_bon = question[2]
    global score
    print("Question : ", question[0])
    print("", choix[0])
    print("", choix[1])
    print("", choix[2])
    print("", choix[3])
    print()
    reponse = input("Donnez une reponse : ")

    if reponse.lower() == choix_bon.lower():
        print("bonne reponse")
        score += 1
    else:
        print("Mauvaise reponse")

    print()

'''
Ameliorer le questionaire avec un tuple

questionaire[]
    question
        title = "Quel est la capitale de la france ?"
        reponses = ("Marseille", "Paris", "Nice", "Nantes")
        bonne_reponse = "Paris"
'''


print("Exo: Le Questionaire")
score = 0
question1 = ("Quel est la capitale de la france ?", ("Marseille", "Paris", "Nice", "Nantes"), "Paris")
question2 = ("Quel est la capitale du Senegal ?", ("Louga", "Kaolack", "Thies", "Dakar"), "Dakar")
questionaire(question1)
questionaire(question2)

#questionaire("Quel est la capitale de la france ?", "Marseille", "Paris", "Nice", "Nantes", "b")
#questionaire("Quel est la capitale du Senegal ?", "Louga", "Kaolack", "Thies", "Dakar", "d")
print("Final Score : ", score)



