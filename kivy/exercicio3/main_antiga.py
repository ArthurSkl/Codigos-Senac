from database import *

while True:
    try:
        banco = Database()

        opção = int(input(f"""Escolha Uma Das Opções Abaixo !
            1 - Cadastrar Nova Tarefa
            2 - Atualizar Uma Tarefa
            3 - Listar Todas Tarefas Cadastradas
            4 - Deletar Uma Tarefa
            0 - Para Sair Do Aplicativo \n """))

        if opção == 1:
            nome = input("Qual O Nome Da Nova Tarefa ? \n")
            desc = input("Qual A Descrição Da Nova Tarefa ? \n")
            data = input("Qual A Data Da Tarefa ? Exemplo De Data 2023-10-05 ")
            estado = input("Qual Estado Da Tarefa ?")
            task = (nome, desc, data, estado)
            banco.insert(task)
            
        elif opção == 2:
            id = int(input("Qual O ID Da Tarefa Que Deseja Atualizar ? \n"))
            nome = input("Qual O Nome Da Nova Tarefa ? \n")
            desc = input("Qual A Descrição Da Nova Tarefa ? \n")
            estado = input("Qual Estado Da Tarefa ?")
            dados = (id, nome, desc, estado)
            banco.update(dados)

        elif opção == 3:
            banco.select()
            
        elif opção == 4:
            x = int(input("Qual O ID Da Tarefa Que Deseja Deletar ? "))
            banco.delete(x)
            print(f"Tarefa {x} Deletada Com Sucesso !")

        elif opção == 0:
            break
        
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

    except ValueError:
        print("Erro: Entrada inválida. Certifique-se de inserir um número válido para a opção.")

    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")
