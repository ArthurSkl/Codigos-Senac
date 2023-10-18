import pyrebase 
from getpass import getpass
 

firebaseConfig = {
  "apiKey": "AIzaSyDRmP9v4Mtk4ZTjU8FdLvfG0cYHsdV80EU",
  "authDomain": "teste-8bd61.firebaseapp.com",
  "databaseURL":"https://teste-8bd61-default-rtdb.firebaseio.com",
  "projectId": "teste-8bd61",
  "storageBucket": "teste-8bd61.appspot.com",
  "messagingSenderId": "142677050268",
  "appId": "1:142677050268:web:9feec9d968004931db7e59",
  "measurementId": "G-V1J26L6TQ1"

} 


class Banco:

    def __init__(self,nome,descricao,data,estado) -> None:
            
        self.nome = nome
        self.descricao = descricao
        self.data = data
        self.estado = estado
    
    def cadastro (self):


        data = {

            "Nome": f"{self.nome}",
            "Descriçâo": f"{self.descricao}",
            "Data": f"{self.data}",
            "Estado": f"{self.estado}"

        }    



        firebase = pyrebase.initialize_app(firebaseConfig) 
        db = firebase.database()
        db.child("Tarefas").push(data)

# autenticacao = firebase.auth()

# email = input("Digite Seu Email \n")

# senha = getpass("Digite Sua Senha \n")

# new_usuario = autenticacao.create_user_with_email_and_password(email,senha) 

# print("Usuario Criado Com Sucesso !") 

firebase = pyrebase.initialize_app(firebaseConfig) 
db = firebase.database()



# data = {

#     "Nome": "Arthur Frantz",
#     "idade": 22,
#     "Endereço": "Endereço aleatorio",
#     "Fone": "Campo Grande"

# } 


# data2 = {

#     "Tarefa": "Vir Para O Senac ",
#     "Data": "28/09/2023",
#     "Status": "Feito",
#     "Paçoca": "123"

# } 

# db.child("Tarefas").push(data)
# db.push(data)

# db.child("Tarefas").push(data2) 

Tarefas = db.child("Tarefas")
tarefas = Tarefas.get()



for tarefas_banco in tarefas.each():
    print(tarefas_banco.val())

    

    
    


    