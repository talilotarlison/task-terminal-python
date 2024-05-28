# https://www.hashtagtreinamentos.com/arquivos-de-texto-com-python
# https://pt.rakko.tools/tools/68/
# https://pythongeeks.org/switch-in-python/
from random import randrange, uniform

def showTasks():
    print('Todas as suas Tarefas:')
    arquivo = open("task.txt", "r")
    conteudo = arquivo.read()  # Lê todo o conteúdo do arquivo
    print(conteudo)
    arquivo.close()  # Não esqueça de fechar o arquivo após a leitura

def showTasksShow():
    print('Todas as suas Tarefas:')
    # Abre o arquivo em modo de leitura
    with open("task.txt", "r") as arquivo:
        linhas = arquivo.read()
        for linha in arquivo:
            print(linha)

    # Agora 'conteudo' contém todo o texto do arquivo
    print(linhas)

def deleteTask():
    print('Excluir suas Tarefas:')
    tarefaID = input('Id da tarefa:')
    path = r'task.txt'
    texto_id_procurado = tarefaID

    # Abre o arquivo em modo de leitura e escrita
    with open(path, 'r') as arquivo_aberto:
        todas_linhas = arquivo_aberto.readlines()

    # Remove as linhas que contêm o texto procurado
    novas_linhas = [linha for linha in todas_linhas if texto_id_procurado not in linha]

    # Abre o arquivo novamente em modo de escrita e escreve as novas linhas
    with open(path, 'w') as arquivo_modificado:
        arquivo_modificado.writelines(novas_linhas)


def addTarefas():
    idTask = randrange(1, 999) #faixa de inteiro
    tarefa = input('Adicionar tarefa:')
    linha_especifica = -1
    texto = f'{idTask} - {tarefa}'

    with open('task.txt', 'r') as file:
        lines = file.readlines()

    lines.insert(linha_especifica, texto + "\n")

    with open('task.txt', 'w') as file:
        file.writelines(lines)

 # escolha do usuario       
def escolhaUser(escolha):
    if(escolha==1):
        separador()
        showTasksShow()
        main()
    elif(escolha==2):
        separador()
        addTarefas()
        main()
    elif(escolha==3):
        separador()
        deleteTask()
        showTasksShow()
        main()
    elif(escolha==4):
        separador()
        print("Obrigado por usar nosso programa!")
        exit()
    else:
        separador()
        print("Opçaõ invalida tente novamente!")
        main()

def separador():
      print("##############################")
    
def logo():
    print("".center(20))
    print("  /__  ___/ ".center(20))
    print("    / /         ___        ___       / ___ ".center(20))
    print("   / /        //   ) )   ((   ) )   //\ \ ".center(20))
    print("  / /        //   / /     \ \      //  \ \ ".center(20))
    print(" / /        ((___( (   //   ) )   //    \ \ ".center(20))
    print("".center(20))

logo()

def main():
    print("Escolhar uma das opções.")
    print("[1] - Listar todas as tarefas!")
    print("[2] - Adcionar tarefa!")
    print("[3] - Excluir tarefa!")
    print("[4] - Sair!")
    escolha = input('Escolhar uma opção:')
    escolhaUser(int(escolha))

if __name__ == "__main__":
    main()
