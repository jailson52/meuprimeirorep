import sqlite3
def titulo(n,s):
    print("=" * n)
    print(f"{s}".center(n))
    print("=" * n)
path = r"C:\SQLite\Aulas"
banco = sqlite3.connect(path + r"\DBPerfumes.db")
cursor = banco.cursor()
#MARCA
cursor.execute("SELECT * FROM marca")
tabela=cursor.fetchall()
titulo(10, "MARCA")
print("id".ljust(0)+"nome".ljust(2)")
for linha in tabela:
    print(linha[0]).ljust(1), end="")
