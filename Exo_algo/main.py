'''
# EXO2:
print("_______ EXO2: ________ ")


# Lire C (chaîne de caractères)
C = ""
while not C == "algorithme":
    C = input("Entrez le mot 'algorithme' : ")

# D = valeur du neuvième caractère de C : index [8]
D = C[8]

# E = valeur du premier caractère de C : index [0]
E = C[0]

# F = valeur du septième caractère de C : index [6]
F = C[6]

# G = valeur du huitième caractère de C : index [7]
G = C[7]

# Calcul de S
S = D + E + F + G

# Afficher S
print("Le résultat de S est :", S)

print()

#Exo3:
print("____EXO3: CALCUL DE LA MOYENNE____")
# Saisie des notes A, B et C
note_A = float(input("Entrez la note A : "))
note_B = float(input("Entrez la note B : "))
note_C = float(input("Entrez la note C : "))

# Coefficients des notes
coeff_A = 2
coeff_B = 1
coeff_C = 1

# Calcul de la moyenne pondérée
moyenne = (coeff_A * note_A + coeff_B * note_B + coeff_C * note_C) / (coeff_A + coeff_B + coeff_C)

# Affichage de la moyenne
print("La moyenne de Amine est :", moyenne)

print()

# EXO4:
print("_____EXO4: CALCUL DE LA SUPERFICIE_____")

# Saisie de la longueur et de la largeur en mètres
L = float(input("Entrez la longueur du terrain en mètres : "))
l = float(input("Entrez la largeur du terrain en mètres : "))

# Calcul de la superficie en mètres carrés
M = L * l

# Conversion de la superficie en hectares
H = M / 10000

# Affichage de la superficie en hectares
print("La superficie du terrain est de", H, "hectares.")

print()

# EXO5:
print("_______ EXO5: La Permutation _______")

x = float(input("Saisissez la valeur de x : "))
y = float(input("Saisissez la valeur de y : "))

z = x
x = y
y = z

print("La valeur de x est : ", x)
print("La valeur de y est : ", y)

print()

#EXO7:
print("_______ EXO:7 _________")

# Saisie de N (entier)
N = int(input("Entrez la valeur de N : "))

# Calcul de A et B
A = 2 / N
B = 1 / N + 1 / (2 * N) + 1 / (3 * N) + 1 / (6 * N)

# Affichage de A et B
print("A =", A)
print("B =", B)


print()

#EXO:8
print("_________ EXO8: ________")

X = int(input("Saisis la valeur de X : "))

if X % 9 == 0:
    Y = X / 9
else:
    Y = X - 9

print("La valeur de Y est : ", Y)


print()

#EXO 9:
print("_________ EXO 9 ___________")

# Saisie du nombre de personnes (N)
N = int(input("Entrez le nombre de personnes dans le groupe : "))

# Calcul du prix par personne
if N >= 5:
    P = 170 * N
else:
    P = 700 + 210 * N

# Calcul du prix total payé par le groupe
#P_total = P * N

# Afficher le prix total payé par le groupe
print("Le prix total payé par le groupe est :", P, "euros")

# Afficher le prix par personne
P_par_personne = P / N
print("Le prix que doit payer chaque membre du groupe est :", P_par_personne, "euros")


print()

#EXO 10:
print("_________ EXO 10 ___________")

reponse = input("répondre oui ou non : ")
if reponse == "oui" or reponse == "non":
    print("La réponse est ", reponse)
else:
    print("C’est une mauvaise réponse")


print()
# EXo 10 modifier
print("_______ EXo 10 modifier _______")

reponse = input("enter oui ou non : ")

if reponse == "oui" or reponse == "non":
    print("correct reponse")
elif len(reponse) == 3:
    print("La réponse a trois caractères, mais n'est tout de même pas correcte.")
elif len(reponse) > 3:
    print("trop mauvaise reponse")


print()
# EXo 11 modifier
print("_______ EXo 11 modifier _______")

C="Je dis"
for i in range(1, 101):
    C=C+" youpi"
C=C+" !"

# Compter le nombre de fois que "youpi" apparaît dans la phrase
nombre_de_youpi = C.count("youpi")

print(C)
print("Nombre de fois que 'youpi' apparaît :", nombre_de_youpi)


print()
# EXo 12 modifier
print("_______ EXo 12 modifier _______")

# Saisie du capital initial, des intérêts annuels et du nombre d'années
C = int(input("Entrez le capital initial : "))
I = int(input("Entrez les intérêts annuels : "))
N = int(input("Entrez le nombre d'années : "))

# Calcul du capital après N années
for k in range(1, N + 1):
    C += I

# Affichage du capital après N années
print("Le capital après", N, "années est de", C, "euros.")

print()
# le nombre d'années le capital de 10000 euros aura doublé :
print("___ le nombre d'années le capital de 10000 euros aura doublé ___")

C_initial = 10000
I_annuel = 80
objectif = C_initial * 2
N_annees = 0

while C_initial < objectif:
    C_initial += I_annuel
    N_annees += 1

print("Le capital doublera au bout de", N_annees, "années.")


print()
# EXo 13 la somme S des n premiers entiers naturels
print("_______ EXo 13 la somme S des n premiers entiers naturels _______")

# Saisie du nombre d'entiers naturels à sommer
n = int(input("Entrez la valeur de n pour les premiers entiers naturels : "))

# Initialisation de la somme à 0
S = 0

# Calcul de la somme des n premiers entiers naturels
for i in range(1, n + 1):
    S += i

# Affichage de la somme
print("La somme des", n, "premiers entiers naturels est :", S)

print()
# EXo 14
print("_______ EXo 14 : Calcul du reste de X/Y si X>Y_______")

# Saisie des entiers X et Y
X = int(input("Entrez la valeur de X : "))
Y = int(input("Entrez la valeur de Y (doit être inférieur à X) : "))

# Vérification que Y < X
if Y >= X:
    print("Erreur : Y doit être strictement inférieur à X.")
else:
    # Calcul du reste de la division euclidienne
    reste = X % Y

    # Affichage du résultat
    print(f"Le reste de la division euclidienne de {X} par {Y} est : {reste}")


print()
#EXO 15: Calcul du Capital sur nbres années
print("Calcul du Capital sur nbres années")

# Saisie du capital initial, des intérêts annuels et du capital voulu
C = int(input("Veuillez saisir le Capital initial : "))
I = int(input("Veuillez saisir les Intérêts : "))
V = int(input("Veuillez saisir le Capital Voulu : "))

# Initialisation du nombre d'années à 0
N = 0

# Boucle tant que pour calculer le nombre d'années nécessaires
while C < V:
    C = C + I  # Ajouter les intérêts au capital
    N += 1     # Incrémenter le nombre d'années

# Affichage du résultat
print(f"Le nombre d'années nécessaires pour atteindre un Capital de {V} est : {N} ans")

print()
print("Calcul du nbres années pour C * 2 ")

# Saisie du capital initial et des intérêts annuels
C = 10000  # capital initial
I = int(input("Veuillez saisir les Intérêts : "))

# Initialisation du nombre d'années à 0
N = 0
C_initial = 0
C_initial = C
print("C_initial = ", C_initial)
# Calcul du capital voulu (le double du capital initial)
C_double = 2 * C
print("C1 = ", C)
# Boucle tant que pour calculer le nombre d'années nécessaires
while C < C_double:
    C += I  # Ajouter les intérêts au capital
    N += 1     # Incrémenter le nombre d'années
    if C == C_double:
        break
print("C2 = ", C)
# Affichage du résultat
print(f"Le capital de {C_initial} euros aura doublé au bout de {N} ans.")


print()
#EXO 16: Calcul du prix du loyer
print("Calcul du prix du loyer")

P = float(input("Veuillez saisir le prix moyen de location : "))
X = float(input("Veuillez saisir le montant à depasser : "))

P_Moyen = 0
P_Moyen = P
N = 0
while P <= X:
    P = P * (1 + 8/100)
    N += 1

#print("le prix de location aura dépasser 11 euros dans : ", N, "ans")
print(f"Le prix moyen de {P_Moyen: .2f} euros de location dépassera {X} euros en: ", N, "ans")


print()
#EXO 17: function 1
print("EXO 17: function 1")


def f(x):
    return (2 * x - 4)

print(f(2))


print()
#EXO 18: function 2: les arguments
print("EXO 18: function 2: les arguments")


def g(a, b, x):
    return a*x+b

print(g(-1, 2, 4))


print()
#EXO 19: function 2: les arguments
print("EXO 19: function 3: ")


def aryt(a, b, n):
    for i in range(1, n):
        a = a + b
        print(a)

aryt(0, 2, 101)
'''


print()
#EXO 20: function 2: les arguments
print("EXO 20: function 3: ")


def cube(x):
    return x**3

n = int(input("Entrer n : "))
for i in range(1, n+1):
    print(cube(i))


