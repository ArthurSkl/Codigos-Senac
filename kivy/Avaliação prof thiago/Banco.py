import sqlite3 as lite


class Banco: 
    def __init__(self):
        self.conexao = lite.connect('AvaliaçãoThiago.db')
        pass       
    def cadastro(self, valores):
        with self.conexao:
            cur = self.conexao.cursor()
            query = "INSERT INTO Tarefas (nome, descricao, dia_em) VALUES (?, ?, ?)"
            cur.execute(query, valores)
            self.conexao.commit()    
             
                    
    # def mostrar_dados(self):
    #     with self.conexao:
    #         lista = []
    #         cur = self.conexao.cursor()
    #         query = "SELECT * FROM Tarefas"
    #         cur.execute(query)
    #         dados = cur.fetchall()
    #         for i in dados:
    #             lista.append(i)
    #     return lista    
    
    
    def mostrar_dados(self):
        with self.conexao:
            lista = []
            cur = self.conexao.cursor()
            query = "SELECT * FROM Tarefas"
            cur.execute(query)
            dados = cur.fetchall()
        for i in dados:
            # Adicione um valor que indica se a tarefa está "Feita" ou "Pendente"
            
            lista.append(i)
        return lista

    def consultar_tarefa(self,id):
        with self.conexao:
            lista = []
            cur = self.conexao.cursor()
            query = "SELECT * FROM Tarefas WHERE id = ?"  # Use ? como marcador de posição
            cur.execute(query, (id,))  # Passe o ID como um parâmetro
            dados = cur.fetchall()

        for i in dados:
            # Adicione os dados relevantes à lista
            lista.append(i)

        return lista 
    
    
    
    
    def atualizar_tarefa(self, id, nome, descricao, data):
        with self.conexao:
            cur = self.conexao.cursor()
            query = "UPDATE Tarefas SET nome = ?, descricao = ?, dia_em = ? WHERE id = ?"
            self.conexao.commit()  
            cur.execute(query,(nome,descricao,data,id))
            self.conexao.commit()     
    
    
    
    def deletar_tarefa(self, id):
        with self.conexao:
            cur = self.conexao.cursor()
            query = "DELETE FROM Tarefas WHERE id = ?"
            cur.execute(query, (id,))
            self.conexao.commit()
    
    
    
    
    
    
    
    
    
    
    # def atualiza_info(i):
    #     with conexao: 
    #         cur = conexao.cursor()
    #         query = "UPDATE formulario SET nome=?, email=?, telefone=?, dia_em=?, estado=?,assunto=? WHERE id=?"
    #         cur.execute(query,i)
            
    # def deletar(id):
        # id=int(input("qual id deseja deletar ?"))
        # with lite.connect('banco_atividade.db') as  conexao:
        #     cur = conexao.cursor()
            
            
        #     query = "DELETE FROM formulario WHERE id = ?"
            
            
        #     valores = (id)
            
        #     cur.execute(query, valores)
        #     conexao.commit()
            

# banco = Banco()
# lista=banco.mostrar_dados()
# print(lista)
# valores = ('Exemplo', 'Descrição do exemplo', '2023-10-22', 'A Fazer')
# banco.cadastro(valores)

    def save_checked(self, checkbox, value, a, b, c, w):
        if value:
            new_status = 'Feito'
        else:
            new_status = 'Pendente'
            cursor=self.conexao.cursor()
            cursor.execute("UPDATE Tarefas SET status = ? WHERE coluna_w = ?", (new_status, w))
            self.conexao.commit()
            self.conexao.close()

    # Exemplo de uso da função save_checked
    # Substitua os valores apropriados para a, b, c e w
   



