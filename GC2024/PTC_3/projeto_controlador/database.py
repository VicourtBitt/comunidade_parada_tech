import sqlite3

conn = sqlite3.connect('paradaTech.db')

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

c.execute(f"INSERT INTO alunos (firstName, lastName) VALUES ('Victor', 'Bittencourt')")
conn.commit()