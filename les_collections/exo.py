noms = []

while True:  # boucle infini
    nom = input("Entrer votre nom : ")
    if nom == "":
        break
    noms.append(nom)

print(noms)

# La trie par ordre alphabetic
noms.sort()
print(noms)

print()
#Exo2:
print("__________EXO2___________")
print("________LISTES - ALGO : VALEUR LA PLUS PETITE________")

nom_chauffeur = ["Amadou", "Bamba", "Ali", "Balla", "Modou", "Ama", "Bal"]
distance_en_km = [3.5, 2.2, 0.4, 0.9, 7.1, 0.1, 0.6]

index_min = 0
distance_min = distance_en_km[0]
for i in range(len(distance_en_km)):
    distance = distance_en_km[i]
    if distance < distance_min:
        distance_min = distance
        index_min = i

print("La voiture la plus proche est à :", distance_min, "km")
print("index de la distance minimal : ", index_min)
print("Listes des chauffeurs : ", nom_chauffeur)
print("Nom du chauffeur est : ", nom_chauffeur[index_min])

print()
print("OU ENCOR")
print()
nom_et_distance = [("Amadou", 3.5), ("Bamba", 2.2), ("Ali", 0.4), ("Balla", 0.9), ("Modou", 7.1), ("Ama", 1.1), ("Bal", 0.6)]

nom_et_distance_min = nom_et_distance[0]
for nom_et_distance in nom_et_distance:
    if nom_et_distance[1] < nom_et_distance_min[1]:
        nom_et_distance_min = nom_et_distance

print("Distance minimal : ", nom_et_distance_min[1], "et le Nom du chauffeur : ", nom_et_distance_min[0])

