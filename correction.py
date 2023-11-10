import datetime

list_species = []
nb_penguins = 0
nb_penguins_by_species = {}
nb_penguins_by_islands = {}
size_beak = 0
nb_pengouins_with_beak = 0
max_depth_beak = 0.0
nb_by_sex = {"male": 0, "female": 0, "unknown": 0}
youngest_penguin = 200
oldest_penguin = -1
current_year = datetime.datetime.now().year

with open("data/pingouins.txt") as f:
    for line in f:
        nb_penguins += 1
        id, specie, island, beak, depth_beak, size, mass, sex, year = line.split(",")
        list_species.append(specie)

        if specie in nb_penguins_by_species:
            nb_penguins_by_species[specie] += 1
        else:
            nb_penguins_by_species[specie] = 1

        if island in nb_penguins_by_islands:
            nb_penguins_by_islands[island] += 1
        else:
            nb_penguins_by_islands[island] = 1

        if beak != "NA":
            nb_pengouins_with_beak += 1
            size_beak += float(beak)

        if depth_beak != "NA":
            if max_depth_beak < float(depth_beak):
                max_depth_beak = float(depth_beak)

        if sex != "NA":
            nb_by_sex[sex] += 1
        else:
           nb_by_sex["unknown"] += 1

        if current_year - int(year) < youngest_penguin:
            youngest_penguin = current_year - int(year)

        if current_year - int(year) > oldest_penguin:
            oldest_penguin = current_year - int(year)


print("Début du traitement : ")

with open("data/resultat_correction.txt", "w", encoding="UTF-8") as f_result:
    f_result.write(f"Nombre de pingouins : {nb_penguins}\n")
    f_result.write("Nombre d'individus par espèce de pingouins : \n")
    for key, value in nb_penguins_by_species.items():
        f_result.write(f"\t{key} : {value} \n")
    f_result.write(f"Nombre d'espèces de pingouins : {len(nb_penguins_by_species)}\n")
    f_result.write("Nombre de pingouins par île : \n")
    for key, value in nb_penguins_by_islands.items():
        f_result.write(f"\t{key} : {value} \n")
    f_result.write(f"Nombre d'îles : {len(nb_penguins_by_islands)}\n")
    f_result.write(f"Longueur moyenne d'un bec de pingouins : {round(size_beak / nb_pengouins_with_beak, 2)} mm\n")
    f_result.write(f"Plus grande profondeur de bec de pingouins : {max_depth_beak} mm\n")
    f_result.write("Nombre de pingouins pour chaque sexe : \n")
    for key, value in nb_by_sex.items():
        f_result.write(f"\t{key} : {value} \n")
    f_result.write(f"Age du pingouin le plus jeune : {youngest_penguin} ans\n")
    f_result.write(f"Age du pingouin le plus âgé : {oldest_penguin} ans\n")

print("Fin du traitement dans le fichier : data/resultat_correction.txt")
