from typing import Any
import mysql.connector 


class Database():
    def __init__(self,banco="tasks") -> None:
        self.banco = banco 

    def connect(self):
        self.conn = mysql.connector.connect(host="192.168.22.9",
                                            database=self.banco,
                                            user="fabrica",
                                            password="fabrica@2022")
        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            print("conectado com sucesso !", db_info )

        else:
            print("Erro ao conectar")


    def insert (self,tarefa): 
        self.connect()
        
        try:
            self.cursor.execute("INSERT INTO arthur_frantz (nome,descricao,data_tarefa,estado_tarefa) VALUES (%s,%s,%s,%s)",(tarefa[0],tarefa[1],tarefa[2],tarefa[3]))
            self.conn.commit()

            return 1   
          
        except Exception as erro: 
            return erro


        finally:
            self.close_connection()       


    def select(self):
        self.connect()
        try:

            self.cursor.execute("SELECT * FROM arthur_frantz ORDER BY ID ")
            result = self.cursor.fetchall()
            return result
        
            

        except Exception as erro:
            return erro

        finally:
            self.close_connection()  


    def update(self,dados):
        self.connect()
        try:
            self.cursor.execute(f"""
                                UPDATE arthur_frantz SET 
                                nome = '{dados[1]}', 
                                descricao = '{dados[2]}',
                                estado_tarefa = '{dados[3]}'
                                WHERE id='{dados[0]}'  
                                """)
            self.conn.commit()
            self.select()          
        except Exception as erro:
            print(erro)

        finally:
            self.close_connection() 


    def filter(self,texto):
        self.connect()

        try:
            self.cursor.execute(f"""
                                SELECT * FROM arthur_frantz 
                                WHERE estado_tarefa LIKE '%{texto}%';
                                """)
            result = self.cursor.fetchall()

            for task in result:
                print(task)

        except Exception as erro:
            print(erro)

        finally:
            self.close_connection()                      


    def delete (self,id):

        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM arthur_frantz WHERE id={id}")
            self.conn.commit()
            print("Task Deletada ")
            self.select()
        except Exception as erro:
            print(erro)
        finally:
            self.close_connection()                

    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("Conexao encerrada !")



if __name__ == "__main__":
    db = Database()

    # nome=input("digite a tarefe")
    # desc=input("digite a descrição")
    # data=input("digite a data")
    # estado=input("digite o estado") 

    # task = (nome,desc,data,estado)

    # data_tarefa = '{dados[4]}',

    # id=int(input("Digite o ID da tarefa !"))
    # nome=input("Digite o ID da tarefa !")
    # desc=input("Digite o ID da tarefa !")
    # estado=input("Qual o estado da tarefa ? ")
    # data=input("Digite o ID da tarefa !")

    # dados=(id,nome,desc,estado)
    

    
   
    # db.insert(task)
    # db.update(dados)
    # db.select()
    # db.delete(id)
    db.filter("pendente")
    