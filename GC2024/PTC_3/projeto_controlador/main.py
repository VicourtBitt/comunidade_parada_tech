import package.SQLController as SQLController
from CleanTerminalModule import clean_terminal
import sys

alunosController = SQLController.AlunosController('paradaTech.db')

operacoes = {
    'newuser' : alunosController.inserirAluno,
    'allusers' : alunosController.todosOsAlunos,
    'deleteuser' : alunosController.deletaAluno
}


def menu():
    print("""
        SEJA BEM VINDO AO CADASTRO DE ALUNOS
    """)


def actions():
   while True:
        print('Ações > [NewUser] - [AllUsers] - [DeleteUser]')
        try:
            acao = input("Deseja fazer o que? ").lower()
            if acao == 'sair':
                sys.exit('Saindo devido ação do usuário')

            elif not acao in operacoes:
                clean_terminal()
                print(f'Operação invalida, I:{acao}')
                continue

            clean_terminal()
            operacoes[acao]()

        except (ValueError, TypeError, NameError) as e:
            SQLController.addIntoLog('error', e)

def main():
    menu()
    actions()

if __name__ == "__main__":
    main()