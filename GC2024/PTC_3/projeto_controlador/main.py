# Importação do arquivo do controlador e suas outras funções.
import package.SQLController as SQLController

# Importação do módulo de limpeza do terminal.
from CleanTerminalModule import clean_terminal

# Importação da biblioteca de manipulação do sistema.
import sys


def menu():
    """ Menu visual que recebe o usuário. 
    Texto feito em: https://edukits.co/text-art/"""
    return """
     ____ _____ ____ _____           ____        _   _                          ____   ___  _     
    |  _ \_   _/ ___|___ /          |  _ \ _   _| |_| |__   ___  _ __     ___  / ___| / _ \| |    
    | |_) || || |     |_ \   _____  | |_) | | | | __| '_ \ / _ \| '_ \   / _ \ \___ \| | | | |    
    |  __/ | || |___ ___) | |_____| |  __/| |_| | |_| | | | (_) | | | | |  __/  ___) | |_| | |___ 
    |_|    |_| \____|____/          |_|    \__, |\__|_| |_|\___/|_| |_|  \___| |____/ \__\_\_____|
                                            |___/                                                  
    """


def actions(dict):
   """ Função responsável por realizar a chamada de outras funções
   presentes em módulos fora do escopo da main por meio de um input
   e de um dicionário com todos os callbacks necessários. """
   while True:
        # Mostra as opções que o usuário pode escolher
        print('Ações > [NewUser] - [AllUsers] - [DeleteUser]')

        # Um bloco try para guiar o fluxo em caso de erro.
        try:

            # Pega a escolha do usuário e coloca em minusculo
            acao = input("Deseja fazer o que? ").lower()
            # Verifica se o usuário deseja sair do programa
            if acao == 'sair':
                # Chama o terminal e sai do código
                sys.exit('Saindo devido ação do usuário')

            # Outro processo defensivo, para ver se a opção
            # existe ou não na chamada de funções
            elif not acao in dict:
                clean_terminal()
                print(f'Operação invalida, I:{acao}')
                continue
            
            clean_terminal()
            # Chama a função sem necessidade do else
            dict[acao]()

        # Em caso de alguns dos seguintes erros
        except (ValueError, TypeError, NameError) as e:
            # Armazena os mesmos no main.log
            SQLController.addIntoLog('error', e)

def main():
    # Instanciamos o objeto do controlador de alunos
    alunosController = SQLController.AlunosController('paradaTech.db')

    # Já deixamos definido o callback de cada função
    operacoes = {
        'newuser' : alunosController.inserirAluno,
        'allusers' : alunosController.todosOsAlunos,
        'deleteuser' : alunosController.deletaAluno
    }

    print(menu())
    actions(operacoes)

if __name__ == "__main__":
    main()