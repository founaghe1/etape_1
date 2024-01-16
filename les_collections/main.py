# Tuple()
print("LES TUPLES")
personnes = ("Moha", "Sarifou", "Diallo", "Sow")
print(personnes)

for i in range(0, len(personnes)):
    print(personnes[i])

print()
for i in personnes:
    print(i)

print()
# les liste[]
print("LES LISTES")
personnes = ["Moha", "Sarifou", "Diallo", "Sow"]
new_person = "Diop"

print(personnes)
print("Add new person : ", new_person)
personnes.append(new_person)
print(personnes)

print("delete person : ", personnes[0])
del personnes[0]
print(personnes)

print()
print("Modification : ")


def modif_valeur(a):
    a[0] = 7


modif = [1, 2, 3, 4, 5]
print(modif)
modif_valeur(modif)
print(modif)


print()
# Function et tuples
print("FUNCTIONS ET TUPLES")


def obtenir_infos():
    return "Moha", 25, 1.87

obtenir_infos()

infos = obtenir_infos()
print(infos)
print("Nom :", infos[0])
print("Age :", infos[1])
print("Taille :", infos[2])

print("OR")

nom, age, taille = obtenir_infos()
print(f"Informations : Nom : {nom}; Age : {age}; Taille : {taille}")

print("OR AGAIN")


def afficher_infos(nom, age, taille):
    print(f"Informations : Nom : {nom}; Age : {age}; Taille : {taille}")

# Ici le *infos dit à la function afficher_infos(*infos) que infos concerne les 3 parametres

afficher_infos(*infos)
print(infos)
print(*infos)  # unpack tuple

print()
# LES SLICES
print("______________LES SLICES_____________")
personnes = ("Moha", "Sarifou", "Diallo", "Sow", "Sarr")

# slice[debut:stop:step]

for i in personnes[::2]:
    print(i)


print()
#LISTES - ALGO : VALEUR LA PLUS PETITE
print("________LISTES - ALGO : VALEUR LA PLUS PETITE________")

nom_chauffeur = ["Amadou", "Bamba", "Ali", "Balla", "Modou", "Ama", "Bal"]
distance_en_km = [3.5, 2.2, 0.4, 0.9, 7.1, 0.1, 0.6]


distance_min = distance_en_km[0]
for distance in distance_en_km:
    if distance < distance_min:
        distance_min = distance

print("La voiture la plus proche est à :", distance_min, "km")




