import pymssql

connexion = pymssql.connect(server="localhost", user="sa", password="Pa$$w0rd", database="Pingouins")

print(connexion)

cursor = connexion.cursor(as_dict=True)
cursor.execute('SELECT id_pingouin, espece, ile FROM dbo.Pingouins')
for row in cursor:
    print(row)
    print("Id :", row['id_pingouin'], "; espèce :", row['espece'], "; île :", row['ile'])
cursor.close()

cursor = connexion.cursor(as_dict=True)
print("\t###\t Choissisez votre pingouin ! \t### ")
num = input("Entrez un numéro de pingouin :\n")
cursor.execute('SELECT * FROM dbo.Pingouins WHERE id_pingouin = %d', (int(num)))
result = cursor.fetchone()
if result:
    print(result)
else:
    print("Aucun pingouin n'a été trouvé ! 😥")
cursor.close()

connexion.close()
