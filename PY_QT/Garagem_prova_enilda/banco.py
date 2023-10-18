import pymysql.connections

banco = pymysql.connections.Connection(
    host="localhost",
    user="root",
    passwd="",
    database="locadora_veiculos"
)


class Banco ():

    def __init__(self) -> None:
        pass

    def cadastrar_cliente (self,dados=[]):
        
        cursor = banco.cursor()

        sql = "INSERT INTO clientes (nome,cpf,email,telefone,senha) VALUES (%s,%s,%s,%s,%s)"
    
        cursor.execute(sql,dados)
        banco.commit() 
    
        
    def atualizar_cliente_banco(self,dados=[]):
        # banco = Banco()
        cursor = banco.cursor()

        sql = f"UPDATE clientes SET nome = '{dados[0]}', cpf =  '{dados[1]}', email =  '{dados[2]}', telefone =  '{dados[3]}' WHERE cpf = {dados[1]}"
              
        cursor.execute(sql)
        banco.commit() 
        
        print("atualizou?",dados)
        
    def veiculo_alugado(self,dados=[]):      
        cursor = banco.cursor()
        sql = "INSERT INTO alugueis (cliente_id,veiculo_id,data_inicio,data_fim) VALUES (%s,%s,%s,%s)"	
        sql2 = "UPDATE veiculos SET ja_foi_alugado = 1"
        sql3 = "UPDATE veiculos SET esta_alugado = 1"
        cursor.execute(sql,dados)
        cursor.execute(sql2)
        cursor.execute(sql3)
        banco.commit() 
        print("Cadastrou")
        
    def cadastrar_ADM(self,cpf=""):
        cursor = banco.cursor()           
        cursor.execute("UPDATE clientes  SET adm = 1 WHERE cpf = %s ", (cpf))
        banco.commit() 
        print("novo adm cadastrado")
        
    def deletar_veiculo(self,id):
        cursor = banco.cursor()           
        cursor.execute(f"DELETE FROM veiculos WHERE id = {id}")
        banco.commit() 
     
    def cadastrar_veiculo (self,dados=[]):
        cursor = banco.cursor()
        sql = "INSERT INTO veiculos (modelo,cor,categoria,chassi,valor_diaria,valor_mensal,valor_compra) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,dados)
        banco.commit()  

    def perfil(self,login,senha):   
        
        try:
           
            cursor = banco.cursor()
            

            
            cursor.execute("SELECT adm FROM clientes WHERE email = %s AND senha = %s", (login, senha))
            resultado = cursor.fetchone()

            if resultado is not None:
                if resultado[0] == 1:
                    return "adm"
                elif resultado[0] == 0:
                    return "cliente"
                else:
                    return "perfil desconhecido"
            else:
                return "Credenciais inválidas"
        except Exception as e:
            print(f"Erro ao obter perfil do cliente: {e}")
            return "Erro"


    def vender_veiculos(self,dados=[]):
        cursor = banco.cursor()

        sql = "INSERT INTO veiculos_vendidos (id_veiculo,id_cliente,preco) VALUES (%s,%s,%s)"
        
        # print(dados)
        # id=int(dados[0])
        # sql2=f"DELETE FROM veiculos WHERE veiculos id = {id}"
        # print(id)
      
        
        cursor.execute(sql,dados)
        # cursor.execute(sql2)
        banco.commit() 
        
        
 