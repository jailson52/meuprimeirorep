import sqlite3

path = r"C:\SQLite\Aulas"
banco = sqlite3.connect(path + r"\DBPerfumes.db")
cursor = banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Marca (id integer, nome text)")
cursor.execute("CREATE TABLE IF NOT EXISTS Fixacoes (id integer, nome text)")
cursor.execute("CREATE TABLE IF NOT EXISTS Volumes (id integer, nome text)")
cursor.execute("CREATE TABLE IF NOT EXISTS Essencia_Perfume (id integer, Essencias_FK, Perfumes_FK)")
cursor.execute("CREATE TABLE IF NOT EXISTS Essencias (id integer, nome text)")
cursor.execute("CREATE TABLE IF NOT EXISTS Perfumes (id integer, nome text, quantidade integer, Volumes_FK integer, marca_FK integer, Fixacoes_FK integer)")