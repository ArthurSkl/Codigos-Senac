import sqlite3 as lite


class Banco: 
    def __init__(self):
        self.conexao = lite.connect('AvaliaçãoThiago.db')
        pass       
    def cadastro(self, valores):
        with self.conexao:
            cur = self.conexao.cursor()
            # cur.execute("CREATE TABLE Tarefas (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, descricao TEXT, dia_em DATE, status TEXT DEFAULT 'A Fazer')")
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
            status = "Feito" if i[1] == "Feito" else "Pendente"
            lista.append((i[0], status, i[2], i[3], i[4]))
        return lista

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
   



