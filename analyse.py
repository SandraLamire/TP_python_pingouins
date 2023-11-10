# Chaque ligne contient les informations d’un individu. Vous trouverez sur chaque ligne, et dans cet ordre :
# -	L’identifiant du pingouin
# -	L’espèce du pingouin
# -	L’île sur laquelle habite le pingouin
# -	La longueur de son bec (en mm)
# -	La profondeur de son bec (en mm)
# -	La longeur de sa nageoire (en mm)
# -	Le poids mass
# -	le sexe
# -	l’année de naissance
# Attention : lorsqu’une information est manquante, la valeur est remplacée par la chaîne de caractère « NA »
# Exemple : 1,Adelie,Torgersen,39.1,18.7,181,3750,male,2007

# -	Combien il y a-t-il de pingouins au total ?
# -	Pour chaque espèce, combien il y a-t-il d’individus ?
# -	Combien il y a-t-il d’espèces ?
# -	Pour chaque île, combien il y a-t-il d’individus ?
# -	Combien il y a-t-il d’îles ?
# -	Quelle est la longueur moyenne des becs ?
# -	Quelle est la plus grande profondeur de bec ?
# -	Combien il y a-t-il de pingouins pour chaque sexe ?
# -	Quel est l’âge du plus jeune pingouin ?
# -	Quel est l’âge du pingouin le plus âgé ?

# Ecrivez-les réponses à ces questions dans un fichier résultats.txt
# Précision de deux chiffres après la virgule pour valeurs non entières
import pickle
from datetime import datetime

list_species = []
nb_penguins = 0
nb_by_specie = {}
nb_by_island = {}
size_beak = 0
nb_pingouins_with_beak = 0
max_depth_beak = 0.0
nb_by_sex = {"male": 0, "female": 0, "unknown": 0}
youngest_pinguin = 200
oldest_pinguin = -1
current_year = datetime.now().year

# with ... as ... ferme automatiquement le fichier après
with open("data/pingouins.txt", encoding="UTF-8") as pingouins_file:
    for line in pingouins_file:
        nb_penguins += 1
        id, specie, island, beak, depth_beak, size, mass, sex, year = line.split(",")
        list_species.append(specie)

        # -	Pour chaque espèce, combien il y a-t-il d’individus ?
        if specie in nb_by_specie:
            nb_by_specie[specie] += 1
        else:
            nb_by_specie[specie] = 1

        # -	Pour chaque île, combien il y a-t-il d’individus ?
        if island in nb_by_island:
            nb_by_island[island] += 1
        else:
            nb_by_island[island] = 1

        # -	Quelle est la longueur moyenne des becs ?
        if beak != "NA":
            nb_pingouins_with_beak += 1
            size_beak += float(beak)

        # -	Quelle est la plus grande profondeur de bec ?
        if depth_beak != "NA":
            if max_depth_beak < float(depth_beak):
                max_depth_beak = float(depth_beak)

        # -	Combien il y a-t-il de pingouins pour chaque sexe ?
        if sex != "NA":
            nb_by_sex[sex] += 1
        else:
            nb_by_sex["unknown"] += 1

        # -	Quel est l’âge du plus jeune pingouin ?
        if current_year - int(year) < youngest_pinguin:
            youngest_pinguin = current_year - int(year)

        # -	Quel est l’âge du pingouin le plus âgé ?
        if current_year - int(year) > oldest_pinguin:
            oldest_pinguin = current_year - int(year)

with open("data/resultats.txt", "w", encoding="UTF-8") as resultats_file:
    # -	Combien il y a-t-il de pingouins au total ?
    resultats_file.write(f"Nombre total de pingouins : {len(list_species)}\n")
    resultats_file.write("\n")

    # -	Pour chaque espèce, combien il y a-t-il d’individus ?
    # Librairie = resultats_file.write(f"Nombre d'individus par espece : {dict(Counter(list_species))}\n")
    resultats_file.write(f"Nombre d'individus par espèce :\n")
    for specie, count in nb_by_specie.items():
        resultats_file.write(f"\t{specie}: {count} individus\n")
    resultats_file.write("\n")

    # -	Combien il y a-t-il d’espèces ?
    resultats_file.write(f"Nombre d'espèces au total : {len(set(list_species))}\n")
    resultats_file.write("\n")

    # -	Pour chaque île, combien il y a-t-il d’individus ?
    resultats_file.write(f"Nombre d'individus par île :\n")
    for island, count in nb_by_island.items():
        resultats_file.write(f"\t{island}: {count} individus\n")
    resultats_file.write("\n")

    # -	Combien il y a-t-il d’îles ?
    resultats_file.write(f"Nombre d'îles: {len(set(nb_by_island))}\n")
    resultats_file.write("\n")

    # -	Quelle est la longueur moyenne des becs ?
    resultats_file.write(f"Longueur moyenne d'un bec de pingouins : {round(size_beak / nb_pingouins_with_beak, 2)} mm\n")
    resultats_file.write("\n")

    # -	Quelle est la plus grande profondeur de bec ?
    resultats_file.write(f"Plus grande profondeur de bec: {max_depth_beak} mm\n")
    resultats_file.write("\n")

    # -	Combien il y a-t-il de pingouins pour chaque sexe ?
    resultats_file.write(f"Nombre de pingouins de chaque sexe: \n")
    for key, value in nb_by_sex.items():
        resultats_file.write(f"\t{key} : {value} \n")
    resultats_file.write("\n")

    # -	Quel est l’âge du plus jeune pingouin ?
    resultats_file.write(f"Age du pingouin le plus jeune: {youngest_pinguin} ans\n")
    resultats_file.write("\n")

    # -	Quel est l’âge du pingouin le plus âgé ?
    resultats_file.write(f"Age du pingouin le plus vieux: {oldest_pinguin} ans\n")
    print(oldest_pinguin)
    resultats_file.write("\n")
