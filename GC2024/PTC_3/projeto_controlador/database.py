# Importação do SQLite3, biblioteca nativa do Python
import sqlite3

# Criação de uma conexão, caso não haja, ele cria uma
# na pasta raiz do projeto.
conn = sqlite3.connect('paradaTech.db')

# Criação de um cursor para navegação e execução de query
c = conn.cursor()

# c.execute("DROP TABLE alunos")

# c.execute("""
#     CREATE TABLE alunos (
#           id INTEGER PRIMARY KEY AUTOINCREMENT,
#           firstName VARCHAR(40) NOT NULL,
#           lastName VARCHAR(40) NOT NULL,
#           createdAt DATETIME NOT NULL DEFAULT (strftime('%Y-%m-%d %H:%M:%f', 'now', 'localtime'))
#     )
# """)

# c.execute(f"INSERT INTO alunos (firstName, lastName) VALUES ('Victor', 'Bittencourt')")

# O comando commit é responsável por aprovar as mudanças de maneira
# permanente no DB.
conn.commit()