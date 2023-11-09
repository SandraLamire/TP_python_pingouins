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
        id, island, specie, long, beak, depth_beak, mass, sex, year = line.split(",")
        list_species.append(specie)

with open("data/resultats.txt", "w") as resultats_file:
    # -	Combien il y a-t-il de pingouins au total ?
    resultats_file.write(f"Nombre total de pingouins : {len(list_species)}\n")

    # -	Pour chaque espèce, combien il y a-t-il d’individus ?
    # Librairie = resultats_file.write(f"Nombre d'individus par espece : {dict(Counter(list_species))}\n")
    resultats_file.write(f"Nombre d'individus par espece :\t")
    for specie in list_species:
        if specie in nb_by_specie:
            nb_by_specie[specie] += 1
        else:
            nb_by_specie[specie] = 1
    for specie, count in nb_by_specie.items():
        resultats_file.write(f"{specie}: {count} individus, ")
    resultats_file.write("\n")

    # -	Combien il y a-t-il d’espèces ?
    resultats_file.write(f"Nombre d'especes au total : {len(set(list_species))}\n")

    # -	Pour chaque île, combien il y a-t-il d’individus ?
    for island in list_species:
        if island in nb_by_island:
            nb_by_island[island] += 1
        else:
            nb_by_island[island] = 1
    for island, count in nb_by_island.items():
        resultats_file.write(f"{island}: {count} individus\t")
    resultats_file.write("\n")

    # -	Combien il y a-t-il d’îles ?
    resultats_file.write(f"Nombre d'iles: {len(set(nb_by_island))}\n")

    # -	Quelle est la longueur moyenne des becs ?
    if beak != "NA":
        nb_pingouins_with_beak += 1
        size_beak += float(beak)
    resultats_file.write(f"Longueur moyenne d'un bec de pingouins : {round(size_beak / nb_pingouins_with_beak, 2)} mm\n")

    # -	Quelle est la plus grande profondeur de bec ?
    if depth_beak != "NA":
        if max_depth_beak < float(depth_beak):
            max_depth_beak = float(depth_beak)
    resultats_file.write(f"Plus grande profondeur de bec: {max_depth_beak} mm")

    # -	Combien il y a-t-il de pingouins pour chaque sexe ?
    resultats_file.write(f"Nombre de pingouins de chaque sexe: \n")
    if sex != "NA":
        nb_by_sex[sex] += 1
    else:
        nb_by_sex["unknown"] += 1
    for key, value in nb_by_sex.items():
        resultats_file.write(f"\t{key} : {value} \t")
    resultats_file.write("\n")

    # -	Quel est l’âge du plus jeune pingouin ?
    if current_year - int(year) < youngest_pinguin:
        youngest_pinguin = current_year - int(year)
    resultats_file.write(f"Age du pingouin le plus jeune: {youngest_pinguin} ans\n")

    # -	Quel est l’âge du pingouin le plus âgé ?
    if current_year - int(year) > oldest_pinguin:
        oldest_pinguin = current_year - int(year)
    resultats_file.write(f"Age du pingouin le plus vieux: {oldest_pinguin} ans\n")
