import sqlite3

path = r"C:\SQLite\Aulas"
banco = sqlite3.connect(path + r"\DBPerfumes.db")
cursor = banco.cursor()

#Marca
cursor.execute("INSERT INTO marca VALUES (1, 'Natura')")
cursor.execute("INSERT INTO marca VALUES (2, 'Boticario')")

#Fixacoes
cursor.execute("INSERT INTO Fixacoes VALUES (1, 'Alcool')")
cursor.execute("INSERT INTO Fixacoes VALUES (2, 'Essencia')")
cursor.execute("INSERT INTO Fixacoes VALUES (3, 'Agua')")

#Perfume
cursor.execute("INSERT INTO Perfumes VALUES (1, 'lua', 100, 1, 1, 3)")
cursor.execute("INSERT INTO Perfumes VALUES (2, 'Mirage', 150, 2, 1, 2)")
cursor.execute("INSERT INTO Perfumes VALUES (3, 'Doce Mel', 180, 1, 2, 3)")

#Volumes
cursor.execute("INSERT INTO Volumes VALUES (1, '100 Ml')")
cursor.execute("INSERT INTO Volumes VALUES (2, '150 Ml')")
cursor.execute("INSERT INTO Volumes VALUES (3, '30 Ml')")

#Essencias
cursor.execute("INSERT INTO Essencias VALUES (1, 'Madeira')")
cursor.execute("INSERT INTO Essencias VALUES (2, 'Laranja')")
cursor.execute("INSERT INTO Essencias VALUES (3, 'Balsamo')")
banco.commit()
