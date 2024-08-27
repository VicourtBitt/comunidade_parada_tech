# Importação do SQLite3, biblioteca nativo do Python
import sqlite3

# Importação da biblioteca de log, nativa do Python.
import logging

# Referenciação do log na raiz do projeto.
logger = logging.getLogger('main.log')

# Configuração do arquivo de log.
logging.basicConfig(
    filename='main.log', 
    level= logging.ERROR,
    format="%(levelname)s - %(asctime)s - %(message)s"
)


class AlunosController:
    def __init__(self, database: str):
        self._connection = SQLiteConnection(database)
    
    def inserirAluno(self):
        """ Função do controlador que recebe o nome do usuário e 
        insere ele na classe de conexão do SQL, mediando informação. """
        while True:
            cpfCnpj = self.pegaInput(str, "Escreva o CPF/CNPJ somente com números: ")
            nome = self.pegaInput(str, "Escreva o nome do aluno: ")
            sobrenome = self.pegaInput(str, 'Escreva o sobrenome do aluno: ')
            idade = self.pegaInput(int, "Escreva a idade do aluno: ")
            genero = self.pegaInput(str, "Escreva o gênero\n[Masculino]-[Feminino]-[Não-Binário]: ")
            telefone = self.pegaInput(str, "Escreva o telefone do aluno, somente numeros: ")

            if not nome or not sobrenome or not cpfCnpj or not idade or not genero:
                break

            idRegistro = self._connection.criarRegistro((cpfCnpj,))
            idInfo = self._connection.criarEstudante((nome, sobrenome, idade, genero, idRegistro))
            return self._connection.criarTelefone((telefone, idInfo))


    def todosOsAlunos(self):
        """ Função do controlador que pega todos os alunos dentro do
        DB pela SQLConnection e os devolve para exibição na tela. """
        print("ID - NOME - SOBRENOME - IDADE - GENERO - REGISTRO")
        alunos = self._connection.pegarTodosOsEstudantes()
        if not alunos:
            print("Nenhum aluno cadastrado")
            return False
        
        for aluno in self._connection.pegarTodosOsEstudantes():
            print(f'{aluno[0]} | {aluno[1]} | {aluno[2]} | {aluno[3]} | {aluno[4]} | {aluno[5]}')
        print()

    def deletaAluno(self):
        """ Função do controlador responsável por receber um ID e passar
        para a query responsável por deletar um registro de aluno no SQL
        Connection. """
        print("É recomendado ver a lista de alunos antes de executar.")
        id = self.pegaInput(int, "Insira o ID do estudante que deseja remover: ")
        tabela = self.pegaInput(str, "Insira a tabela da qual deseja excluir: ")
        
        try:
            if not isinstance(id, int):
                print("ID não foi inserido corretamente.")
                raise ValueError('ID foi inserido incorretamente.')
            
        except (ValueError) as e:
            addIntoLog('info', e)

        self._connection.apagarEstudanteEspecifico(id, tabela)

    @staticmethod
    def pegaInput(type, texto: str, lower= False):
        try:
            value = type(input(texto)).lower() if lower else type(input(texto))
            if value == 'sair':
                return False
            
        except (ValueError, TypeError, NameError) as e:
            addIntoLog('info', e)
            return False
        return value

    
class SQLiteConnection:
    """Classe responsável por se conectar a database, permitindo
    ações como select, insert, update e delete. Tudo com DocStrings
    e seus parametros adicionais conforme documentação."""

    def __init__(self, database):
        self._database = sqlite3.connect(database)

    def criarRegistro(self, valuesToInsert: tuple):
        """Cria registro de aluno na tabela alunosRegistro"""
        try:
            sql = """
                INSERT INTO alunosRegistro (cpf_cnpj)
                VALUES (?)
            """

            cur = self._database.cursor()
            cur.execute(sql, valuesToInsert)
            self._database.commit()
            return cur.lastrowid
        
        except (ValueError, TypeError) as e:
            addIntoLog('error', e)

    def criarTelefone(self, valuesToInsert: tuple):
        """Cria telefone do aluno na tabela alunosTelefone"""
        try:
            sql = """
                INSERT INTO alunosTelefone (telefone, idInfo)
                VALUES (?, ?)
            """
            cur = self._database.cursor()
            cur.execute(sql, valuesToInsert)

            # ENVIO DOS VALORES DE FORMA PERMANENTE
            self._database.commit()
            return cur.lastrowid
        
        except (ValueError, TypeError) as e:
            addIntoLog('error', e)

    def criarEstudante(self, valuesToInsert: tuple):
        """Cria informações do aluno na tabela alunosInfo"""
        try: 
            # QUERY LITERAL
            sql = """
                INSERT INTO alunosInfo (nome, sobrenome, idade, genero, idRegistro)
                VALUES (?, ?, ?, ?, ?)
            """

            cur = self._database.cursor()
            cur.execute(sql, valuesToInsert)

            # ENVIO DOS VALORES DE FORMA PERMANENTE
            self._database.commit()
            return cur.lastrowid
        
        except (ValueError, TypeError) as e:
            addIntoLog('error', e)
    
    def pegarTodosOsEstudantes(self, table: str = 'alunosInfo'):
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

    def apagarEstudanteEspecifico(self, id: int, table: str):
        try: 
            sql = f'DELETE FROM {table} WHERE id = {id};'

            cur = self._database.cursor()
            cur.execute(sql)
            self._database.commit()

        except (ValueError, TypeError, NameError) as e:
            addIntoLog('error', e)

    def atualizaEstudanteEspecifico(self, id: int):
        ...

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