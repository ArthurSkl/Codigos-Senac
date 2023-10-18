import sqlite3 as lite

conexao = lite.connect('banco_atividade.db')

class banco :

    def __init__(self) -> None:
        pass
    
    def cadastro (valores):

        with conexao:
            cur = conexao.cursor()

            # cur.execute("CREATE TABLE formulario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, telefone TEXT, dia_em DATE, estado TEXT, assunto TEXT)")

           
            query = "INSERT INTO formulario (nome, email, telefone, dia_em, estado, assunto) VALUES (?, ?, ?, ?, ?, ?)"
            
            # valores = ('Joao 5Futi Muanda', 'joao@mail.com', '123456789', '2010-12-19', 'Normal', 'gostaria de o consultar pessoalmente')

            cur.execute(query, valores)

            conexao.commit()

    
    
    def mostrar_dados():
        
        lista=[]
        
        with conexao: 
            
            cur = conexao.cursor()
            
            query="SELECT * FROM formulario "
            
            cur.execute(query) 
            
            dados=cur.fetchall()
            
            for i in dados:
                lista.append(i)
                
        return lista        
        
        
        
 

    # def update_registro():
        
    #     id_registro = int(input("Digite o ID do registro que deseja atualizar: "))

    #     with lite.connect('banco_atividade.db') as conexao:
    #         cur = conexao.cursor()

            
    #         cur.execute("SELECT * FROM formulario WHERE id=?", (id_registro,))
    #         registro = cur.fetchone()

    #         if registro is None:
    #             print("Registro com o ID fornecido não encontrado.")
    #         else:
                
    #             novo_nome = input("Digite o novo nome: ")
    #             novo_email = input("Digite o novo email: ")
    #             novo_telefone = input("Digite o novo telefone: ")
    #             novo_dia_em = input("Digite a nova data (no formato YYYY-MM-DD): ")
    #             novo_estado = input("Digite o novo estado: ")
    #             novo_assunto = input("Digite o novo assunto: ")

                
    #             query = "UPDATE formulario SET nome=?, email=?, telefone=?, dia_em=?, estado=?, assunto=? WHERE id=?"
    #             valores = (novo_nome, novo_email, novo_telefone, novo_dia_em, novo_estado, novo_assunto, id_registro)
    #             cur.execute(query, valores)
    #             conexao.commit()

    #             print("Registro atualizado com sucesso.")

    def atualiza_info(i):
        with conexao: 
            cur = conexao.cursor()
            query = "UPDATE formulario SET nome=?, email=?, telefone=?, dia_em=?, estado=?,assunto=? WHERE id=?"
            cur.execute(query,i)
            
    
    def deletar(id):
        # id=int(input("qual id deseja deletar ?"))
        with lite.connect('banco_atividade.db') as  conexao:
            cur = conexao.cursor()
            
            
            query = "DELETE FROM formulario WHERE id = ?"
            
            
            valores = (id)
            
            cur.execute(query, valores)
            conexao.commit()
            
        
        




                
#x=banco
#lista=['fffffffffff','email','telefone','data','estado','assunto']
#x.cadastro(lista)
# x.update_registro()
# x.deletar()
# x.mostrar_dados()                   




