import pymssql

# Connexion à la BDD
connexion = pymssql.connect(server="localhost", user="sa", password="Pa$$w0rd", database="Pingouins")
# Vérification de la connexion
print(connexion)


# -	Combien il y a-t-il de pingouins au total ?
# pas besoin de renvoyer le résultat sous forme de dictionnaire dans ce cas :
# cursor = connexion.cursor(as_dict=True)
cursor = connexion.cursor()
cursor.execute('SELECT COUNT(*) FROM dbo.Pingouins')
# fetchone pour un seul résultat
total_pingouins = cursor.fetchone()[0]
print(f"Le nombre total de pingouins est : {total_pingouins}")
cursor.close()

print("#######################################################")

# -	Pour chaque espèce, combien il y a-t-il d’individus ?
cursor1 = connexion.cursor()
cursor1.execute('SELECT espece, COUNT(*) AS nb_individus FROM dbo.Pingouins GROUP BY espece')
# fetchall pour récupérer tous les résultats sur plusieurs lignes
resultats1 = cursor1.fetchall()
print("il y a :")
for row in resultats1:
    espece, nb_individus_par_espece = row
    print(f"\t- {nb_individus_par_espece} individus de l'espèce {espece}")
cursor1.close()

print("#######################################################")

# -	Combien il y a-t-il d’espèces ?
cursor2 = connexion.cursor()
cursor2.execute('SELECT espece, COUNT(*) FROM dbo.Pingouins GROUP BY espece')
resultat_especes = cursor2.fetchall()
nb_especes = len(resultat_especes)
print(f"Il y a {nb_especes} espèces différentes :")
for espece in resultat_especes:
    print(f"\t- {espece[0]}")
cursor2.close()

print("#######################################################")

# -	Pour chaque île, combien il y a-t-il d’individus ?
cursor3 = connexion.cursor()
cursor3.execute('SELECT ile, COUNT(*) AS nb_individus_par_ile FROM dbo.Pingouins GROUP BY ile')
# fetchall pour récupérer tous les résultats sur plusieurs lignes
resultats2 = cursor3.fetchall()
print("Il y a : ")
for row in resultats2:
    ile, nb_individus_par_ile = row
    print(f"\t- {nb_individus_par_ile} individus sur l'île de {ile}")
cursor3.close()

print("#######################################################")

# -	Combien il y a-t-il d’îles ?
cursor4 = connexion.cursor()
cursor4.execute('SELECT ile, COUNT(*) FROM dbo.Pingouins GROUP BY ile')
resultats_iles = cursor4.fetchall()
nb_iles = len(resultats_iles)
print(f"Il y a {nb_iles} îles")
for ile in resultats_iles:
    print(f"\t- {ile[0]}")
cursor4.close()

print("#######################################################")

# -	Quelle est la longueur moyenne des becs ?
cursor5 = connexion.cursor()
cursor5.execute('SELECT AVG(DISTINCT longueur_bec) FROM dbo.Pingouins')
longueur_bec_moyenne = round(cursor5.fetchone()[0], 2)
print(f"La longueur moyenne des becs est de {longueur_bec_moyenne} mm")
cursor5.close()

print("#######################################################")

# -	Quelle est la plus grande profondeur de bec ?
cursor6 = connexion.cursor()
cursor6.execute('SELECT MAX(DISTINCT profondeur_bec) FROM dbo.Pingouins')
profondeur_bec_max = round(cursor6.fetchone()[0], 2)
print(f"La plus grande profondeur de bec est de {profondeur_bec_max} mm")
cursor6.close()

print("#######################################################")

# -	Combien il y a-t-il de pingouins pour chaque sexe ?
cursor7 = connexion.cursor()
cursor7.execute('SELECT sex, COUNT(*) FROM dbo.Pingouins GROUP BY sex')
resultats_sexe = cursor7.fetchall()
print("Il y a :")
for row in resultats_sexe:
    sex, nb_individus_par_sexe = row
    sex_label = "de sexe indéterminé" if sex is None else "femelles" if sex == "female" else "mâles" if sex == "male" else sex
    print(f"\t- {nb_individus_par_sexe} individus {sex_label}")
cursor7.close()


print("#######################################################")

# -	Quel est l’âge du plus jeune pingouin ?
cursor8 = connexion.cursor()
cursor8.execute('SELECT YEAR(GETDATE()) - MAX(annee_naissance) as age_min FROM dbo.Pingouins WHERE annee_naissance IS NOT NULL')
age_min = cursor8.fetchone()[0]
print(f"Le plus jeune pingouin a {age_min} ans")
cursor8.close()

print("#######################################################")

# -	Quel est l’âge du pingouin le plus âgé ?
cursor9 = connexion.cursor()
cursor9.execute('SELECT YEAR(GETDATE()) - MIN(annee_naissance) as age_max FROM dbo.Pingouins WHERE annee_naissance IS NOT NULL')
age_max = cursor9.fetchone()[0]
print(f"Le pingouin le plus âgée a {age_max} ans")
cursor9.close()

print("#######################################################")
connexion.close()

with open("data/resultats_bdd.txt", "w", encoding="UTF-8") as resultats_file:
    resultats_file.write(f"Nombre total de pingouins : {total_pingouins}\n")
    resultats_file.write("\n")

    resultats_file.write(f"Nombre d'individus par espece : \n")
    for row in resultats1:
        espece, nb_individus_par_espece = row
        resultats_file.write(f"\t- {nb_individus_par_espece} individus de l'espèce {espece}\n")
    resultats_file.write("\n")

    resultats_file.write(f"Il y a {nb_especes} espèces différentes :\n")
    for espece in resultat_especes:
        resultats_file.write(f"\t- {espece[0]}\n")
    resultats_file.write("\n")

    resultats_file.write(f"Nombre d'individus par île :\n")
    for row in resultats2:
        ile, nb_individus_par_ile = row
        resultats_file.write(f"\t- {nb_individus_par_ile} individus sur l'île de {ile}\n")
    resultats_file.write("\n")

    resultats_file.write(f"Il y a {nb_iles} îles :\n")
    for ile in resultats_iles:
        resultats_file.write(f"\t- {ile[0]}\n")
    resultats_file.write("\n")

    resultats_file.write(f"La longueur moyenne des becs est de {longueur_bec_moyenne} mm\n")
    resultats_file.write("\n")

    resultats_file.write(f"La plus grande profondeur de bec est de {profondeur_bec_max} mm\n")
    resultats_file.write("\n")

    resultats_file.write(f"Nombre d'individus de chaque sexe :\n")
    for row in resultats_sexe:
        sex, nb_individus_par_sexe = row
        sex_label = "de sexe indéterminé" if sex is None else "femelles" if sex == "female" else "mâles" if sex == "male" else sex
        resultats_file.write(f"\t- {nb_individus_par_sexe} {sex_label}\n")
    resultats_file.write("\n")

    resultats_file.write(f"Le plus jeune pingouin a {age_min} ans\n")
    resultats_file.write("\n")

    resultats_file.write(f"Le pingouin le plus âgée a {age_max} ans\n")
    resultats_file.write("\n")



