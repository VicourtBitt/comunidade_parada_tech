# Importação do SQLite3, biblioteca nativa do Python
import sqlite3

# Criação de uma conexão, caso não haja, ele cria uma
# na pasta raiz do projeto.
conn = sqlite3.connect('paradaTech.db')

# Criação de um cursor para navegação e execução de query
c = conn.cursor()

# c.execute("""
#     DROP TABLE cursos
# """)

c.execute("""
     CREATE TABLE alunosRegistro (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          cpf_cnpj VARCHAR(14) NOT NULL
    )
""")

c.execute("""
    CREATE TABLE alunosInfo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(40) NOT NULL,
        sobrenome VARCHAR(40) NOT NULL,
        idade INTEGER NOT NULL,
        genero VARCHAR(12) NOT NULL,
        idRegistro INTEGER,
        FOREIGN KEY (idRegistro) REFERENCES alunosRegistro(id)
    )
""")

c.execute("""
    CREATE TABLE alunosTelefone (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telefone VARCHAR(15) NOT NULL,
        idInfo INTEGER,
        FOREIGN KEY (idInfo) REFERENCES alunosInfo(id)
    )
""")

# c.execute(f"INSERT INTO alunosRegistro (cpf_cnpj) VALUES ('05400042000'), ('04200065400')")

# c.execute("""
#     INSERT INTO alunosInfo (nome, sobrenome, idade, genero, idRegistro) 
#     VALUES 
#         ('Victor', 'Bittencourt', 20, 'Masculino', 1),
#         ('Lauro', 'Mendelski', 20, 'Masculino', 2)
# """)

# c.execute("""
#     INSERT INTO alunosTelefone (telefone, idInfo)
#     VALUES
#           ('51983149920', 1),
#           ('51991000016', 2)
# """)

# O comando commit é responsável por aprovar as mudanças de maneira
# permanente no DB.
conn.commit()