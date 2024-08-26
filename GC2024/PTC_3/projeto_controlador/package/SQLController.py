import sqlite3
import logging

logger = logging.getLogger('main.log')
logging.basicConfig(
    filename='main.log', 
    level= logging.ERROR,
    format="%(levelname)s - %(asctime)s - %(message)s"
)


class AlunosController:
    def __init__(self, database: str):
        self._connection = SQLiteConnection(database)
    
    # @classmethod
    # def criarAluno(cls, name, surname):
    #     return cls(name, surname)
    
    def inserirAluno(self):
        while True:
            nome = input('Insira o nome do novo aluno: ')
            sobrenome = input('Insira o sobrenome do novo aluno: ')

            if (nome == 'sair' or sobrenome == 'sair'):
                break

            return self._connection.criarEstudante((nome, sobrenome))
        
    def todosOsAlunos(self):
        print("ID - NOME - SOBRENOME - CRIADO EM")
        for alunos in self._connection.pegarTodosOsEstudantes():
            print(alunos)
        print()

    def deletaAluno(self):
        print("É recomendado ver a lista de alunos antes de executar.")
        id = input('Escolha o ID do estudante a ser eliminado: ')

        if not isinstance(id, int):
            return False
        
        self._connection.apagarEstudanteEspecifico(int(id))

    
class SQLiteConnection:
    """Classe responsável por se conectar a database, permitindo
    ações como select, insert, update e delete. Tudo com DocStrings
    e seus parametros adicionais conforme documentação
    """

    def __init__(self, database):
        self._database = sqlite3.connect(database)

    def criarEstudante(self, valuesToInsert: tuple):
        """ Query com docstring literal para postar
        o novo estudante no sistema. Alunos também 
        será a tabela default 
        > Example:
        - sql = '''INSERT INTO alunos (firstName, lastName) VALUES (?, ?)'''
        - valuesToInsert = ('Victor', 'Bittencourt')
        - c = cursor.execute(sql, valuesToInsert) """

        try: 
            # QUERY LITERAL
            sql = """
                INSERT INTO alunos (firstName, lastName)
                VALUES (?, ?)
            """

            cur = self._database.cursor()
            cur.execute(sql, valuesToInsert)

            # ENVIO DOS VALORES
            self._database.commit()
            return cur.lastrowid
        
        except (ValueError, TypeError) as e:
            addIntoLog('error', e)
    
    def pegarTodosOsEstudantes(self, table: str = 'alunos'):
        """ Query com f-strig literal para resgatar
        todos os estudantes cadastrados. Com alunos 
        como a tabela default. """

        try:
            # QUERY LITERAL DO SQL
            sql = f'SELECT * FROM {table}'

            # CRIAÇÃO DE UM CURSOR PARA A QUERY
            cur = self._database.cursor()
            cur.execute(sql)

            # RESGATE DOS RESULTADOS (TODOS)
            values = cur.fetchall()
            if not values:
                return "Nenhum estudate cadastrado"
            return values
        
        except (ValueError, TypeError) as e:
            addIntoLog('error', e)

    def apagarEstudanteEspecifico(self, id: int):
        try: 
            sql = f'DELETE FROM alunos WHERE id = {id}'

            cur = self._database.cursor()
            cur.execute(sql)
            self._database.commit()

        except (ValueError, TypeError, NameError) as e:
            addIntoLog('error', e)


def addIntoLog(type: str, mensagem: str):
    """ Função utilizada para colocar erros/avisos
    no log do projeto. Para futuramente serem avaliados
    pelos desenvolvedores.
    
    Atributos:
    ----------
    - logTypes : Um dicionário para chamadas de função.
    - type : A chave que será chamada no dicionário.
    - mensagem : A mensagem colocada nessa chamada do log.
    """
    
    logTypes = {
        'error' : logger.error,
        'info' : logger.info,
        'warning' : logger.warning,
        'debug' : logger.debug 
    }

    logTypes[type](mensagem)