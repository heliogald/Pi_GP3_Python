import sqlite3
#Conexão com o banco
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# lendo os dados
cursor.execute("""
SELECT * FROM pesquisas_pesquisa WHERE country = 'Brazil'
""")
for linha in cursor.fetchall():
    print(linha)

conn.close()