from database import * 




class Tarefa :

    def __init__(self) -> None:

        # self.nome = tarefa[0] 
        # self.desc = tarefa[1]  
        # self.data = tarefa[2]  
        # self.estado = tarefa[3]  
        self.banco = Database 

        # self.tarefa=(self.nome,self.desc,self.data,self.banco)

    def cadastrar ():

        try:

            banco=Database()
            nome = input("Qual O Nome Da Nova Tarefa ? \n")
            desc = input("Qual A Descrição Da Nova Tarefa ? \n")
            data = input("Qual A Data Da Tarefa ? Exemplo De Data 2023-10-05 ")
            estado = input("Qual Estado Da Tarefa ?")
            tarefa = (nome, desc, data, estado)
            banco.insert(tarefa)

            return True
        
        except Exception as erro: 

            return erro

    def listar_dados():
        banco=Database()

        x=banco.select()
        return x

    def atualizar_tarefa():
        try:

            banco=Database()
            id = int(input("Qual o ID Da Tarefa Que Deseja Atualizar ?"))
            nome = input("Qual O Nome Da Nova Tarefa ? \n")
            desc = input("Qual A Descrição Da Nova Tarefa ? \n")
            data = input("Qual A Data Da Tarefa ? Exemplo De Data 2023-10-05 ")
            estado = input("Qual Estado Da Tarefa ?")
            tarefa = (id,nome, desc, data, estado)
            banco.update(tarefa)

            return True
        
        except Exception as erro: 

            return erro







# x= Tarefa

# x.cadastrar()
        


        