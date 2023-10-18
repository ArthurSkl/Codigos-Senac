from PyQt6  import uic, QtWidgets 
from banco import Banco
from banco import *
from datetime import datetime, timedelta
import datetime


def converter_data_formato_banco(data_str):
    try:
        data_formato_banco = datetime.strptime(data_str, '%d/%m/%Y').date()
        return data_formato_banco
    except ValueError:
        print("Erro: Data em formato inválido")
        return None

def listar_dados():
    tela_aluguel_compra.show()

    cursor = banco.cursor()
    sql = "SELECT * FROM veiculos"
    cursor.execute(sql)
    dados_recebidos = cursor.fetchall()
    # print(dados_recebidos)

    tela_aluguel_compra.tableWidget.setRowCount(len(dados_recebidos))
    tela_aluguel_compra.tableWidget.setColumnCount(10) 
    tela_aluguel_compra.tableWidget.setHorizontalHeaderLabels(('ID', 'MODELO','COR', 'CATEGORIA','CHASSI' , 'VALOR DIARIA', 'VALOR MENSAL', 'VALOR DE COMPRA', 'JA FOI ALUGADO',  'ESTA ALUGADO'))  
    tela_aluguel_compra.tableWidget.setStyleSheet("QTableView::item:selected { color:white; background:#000000; font-weight:900; }"
                           "QTableCornerButton::section { background-color:#232326; }"
                           "QHeaderView::section { color:white; background-color:#232326; }")
    
    for linha in range(0,len(dados_recebidos)):
        for coluna in range(0,10):
            tela_aluguel_compra.tableWidget.setItem(linha,coluna,QtWidgets.QTableWidgetItem(str(dados_recebidos[linha][coluna])))
    
    tela_aluguel_compra.show() 
    
def listar_dados_clientes():
    form_usuario.show()

    cursor = banco.cursor()
    sql = "SELECT * FROM clientes"
    cursor.execute(sql)
    dados_recebidos = cursor.fetchall()
    # print(dados_recebidos)

    form_usuario.tableWidget.setRowCount(len(dados_recebidos))
    
    form_usuario.tableWidget.setColumnCount(7) 
    form_usuario.tableWidget.setHorizontalHeaderLabels(('ID', 'Nome','Telefone', 'E-mail','CPF' , 'Senha', 'ADM',))  
    form_usuario.tableWidget.setStyleSheet("QTableView::item:selected { color:white; background:#000000; font-weight:900; }"
                           "QTableCornerButton::section { background-color:#232326; }"
                           "QHeaderView::section { color:white; background-color:#232326; }")
    
    for linha in range(0,len(dados_recebidos)):
        for coluna in range(0,7):
            form_usuario.tableWidget.setItem(linha,coluna,QtWidgets.QTableWidgetItem(str(dados_recebidos[linha][coluna])))
    
    form_usuario.show() 

app = QtWidgets.QApplication([])

tela_login = uic.loadUi("PY_QT/Garagem_prova_enilda/Tela_login.ui")

tela_aluguel_compra = uic.loadUi("PY_QT/Garagem_prova_enilda/Tela_aluguel_compra.ui")

form_usuario = uic.loadUi("PY_QT/Garagem_prova_enilda/Tela_cadastro_usuario.ui")

tela_adm = uic.loadUi("PY_QT/Garagem_prova_enilda/painel_Adm.ui")

listar_usuarios = uic.loadUi("PY_QT/Garagem_prova_enilda/Cadastro_Listar_Veiculos.ui")

def cadastrando_cliente ():
    nome = form_usuario.nome.text()
    cpf = form_usuario.cpf.text()
    email = form_usuario.email.text()
    telefone = form_usuario.telefone.text()
    senha = form_usuario.senha.text()       
        

    dados = [str(nome),str(cpf),str(email),str(telefone),str(senha)]

    banco = Banco()
    banco.cadastrar_cliente(dados)

    form_usuario.nome.setText("")
    form_usuario.cpf.setText("")
    form_usuario.email.setText("")
    form_usuario.telefone.setText("")
    form_usuario.senha.setText("")
    
def fecha_tela_adm():
    tela_adm.close()

def volta_tela_adm():
    listar_usuarios.close()
    form_usuario.close()
    tela_aluguel_compra.close()
    tela_adm.show()

def tela_cadastro_listagem_usuario():
    form_usuario.show()
    tela_adm.close()
    listar_dados_clientes()

def cadastrando_veiculos():

    modelo = tela_adm .modelo.text()
    cor = tela_adm .cor.text()
    categoria = tela_adm .categoria.text()
    chassi = tela_adm .chassi.text()
    diaria = tela_adm .diaria.text()  
    mensal = tela_adm .mensal.text()  
    preço_compra = tela_adm .compra.text()       
    
       

    dados = [str(modelo),str(cor),str(categoria),str(chassi),float(diaria),float(mensal),float(preço_compra)]
    # dados = [modelo,cor,categoria,chassi,diaria,mensal,preço_compra]
    banco = Banco()
    banco.cadastrar_veiculo(dados)
    tela_adm .modelo.setText("")
    tela_adm .cor.setText("")
    tela_adm .categoria.setText("")
    tela_adm .chassi.setText("")
    tela_adm .diaria.setText("")
    tela_adm .mensal.setText("")
    tela_adm .compra.setText("")
    listar_dados()

def mostrar_tela_aluguel():
    tela_adm.close()
    tela_aluguel_compra.show()
    
    
    cursor = banco.cursor()
    sql = "SELECT * FROM alugueis"
    cursor.execute(sql)
    dados_recebidos = cursor.fetchall()
    # print(dados_recebidos)

    tela_aluguel_compra.tableWidget.setRowCount(len(dados_recebidos))
    tela_aluguel_compra.tableWidget.setColumnCount(5) 
    tela_aluguel_compra.tableWidget.setHorizontalHeaderLabels(('ID', 'ID CLIENTE','ID VEICULO', 'DATA DE INICIO','DATA DE DEVOLUÇÃO'))  
    tela_aluguel_compra.tableWidget.setStyleSheet("QTableView::item:selected { color:white; background:#000000; font-weight:900; }"
                           "QTableCornerButton::section { background-color:#232326; }"
                           "QHeaderView::section { color:white; background-color:#232326; }")
    
    for linha in range(0,len(dados_recebidos)):
        for coluna in range(0,5):
            tela_aluguel_compra.tableWidget.setItem(linha,coluna,QtWidgets.QTableWidgetItem(str(dados_recebidos[linha][coluna])))
    
    tela_aluguel_compra.show() 

def obter_perfil_do_cliente():
    
    login = tela_login.login.text()
    senha = tela_login.senha.text()
    
    banco=Banco()
    retorno=banco.perfil(login,senha)
    # print(retorno)
    if (retorno == "adm"):
        tela_adm.show() 
       
        tela_adm.pushButton.clicked.connect(listar_dados)
        tela_adm.pushButton_2.clicked.connect(tela_cadastro_listagem_usuario)
        tela_adm.pushButton_3.clicked.connect(mostrar_tela_aluguel)      
       
    elif (retorno == "cliente"):
       listar_dados()  
    else:
        print("Dados invalidos")             

def cadastro_adm ():    
    cpf = tela_adm.cpf.text()

    banco = Banco()
            
    banco.cadastrar_ADM(cpf)

    # btn_cadastrar_ADM
                
    tela_adm.cpf.setText("")     
    
def fecha_tela_login():
    tela_login.close()

def aluguel_veiculos():
    
    nome = tela_aluguel_compra.nome.text()
    cpf = tela_aluguel_compra.cpf.text()
    id = tela_aluguel_compra.id.text()
    quantidade_dias = tela_aluguel_compra.quantidade_dias.text()
    
    cursor = banco.cursor()
                
    cursor.execute("SELECT * FROM clientes WHERE cpf = %s", (cpf))
    resultado = cursor.fetchone()
    
    # cursor = banco.cursor()
                
    # cursor.execute("SELECT * FROM veiculos WHERE cpf = %s", (cpf))
    # resultado = cursor.fetchone()
    
    data_atual = datetime.date.today()
    # print(data_atual)
    
    # data_atual2= datetime.strptime(f'{data_atual}', '%Y-%m-%d')
    # print(data_atual2)
    quantidade_dias = int(quantidade_dias)
    
    nova_data = data_atual + timedelta(days=quantidade_dias)
    
    # print(nova_data)
    # print(nova_data.strftime('%Y-%m-%d'))
    
    # print(resultado[0])
    
    dados = [int(resultado[0]),int(id),str(data_atual),str(nova_data)]

    x=Banco()
    x.veiculo_alugado(dados)
    
    mostrar_tela_aluguel()
      
    tela_aluguel_compra.nome.setText("")
    tela_aluguel_compra.cpf.setText("")
    tela_aluguel_compra.id.setText("")
    tela_aluguel_compra.quantidade_dias.setText("")
    
def consulta_veiculo():
    
    id = tela_aluguel_compra.id.text() 
    
    
    cursor = banco.cursor()
    sql =  f"SELECT * FROM veiculos WHERE ID = {id}"
    cursor.execute(sql)
    dados_recebidos = cursor.fetchall()  
    # print(dados_recebidos)
    # print(dados_recebidos[0][5]) #posição 
    
    
    
    
    tela_aluguel_compra.diaria.setText(f"{dados_recebidos[0][5]}")
    tela_aluguel_compra.mensal.setText(f"{dados_recebidos[0][6]}")
    tela_aluguel_compra.valor_compra.setText(f"{dados_recebidos[0][7]}")

def consulta_cpf():
    cpf = tela_aluguel_compra.cpf.text()
    
    cursor = banco.cursor()
    sql =  f"SELECT * FROM clientes WHERE cpf = '{cpf}';"
    
    cursor.execute(sql)
    dados_recebidos = cursor.fetchall() 
    
     
    # print("dados do cliente",dados_recebidos) 
       
    tela_aluguel_compra.nome.setText(dados_recebidos[0][1])
    
    data = tela_aluguel_compra.quantidade_dias.text()
    
    data_int = int(data)
    
    # print(data_int)
    # print(data_int + data_int)
    
    if(data_int < 30):
        id = tela_aluguel_compra.id.text()
        cursor = banco.cursor()
        sql =  f"SELECT * FROM veiculos WHERE ID = {id}"
        cursor.execute(sql)
        dados_recebidos = cursor.fetchall()  
        # print(dados_recebidos)
        # print(dados_recebidos[0][5]) #posição 
        
        x=data_int * dados_recebidos[0][5]
        
        t=str(x)
        
        tela_aluguel_compra.total.setText(t)
                    
    elif(data_int >= 30):
        
        id = tela_aluguel_compra.id.text()
        cursor = banco.cursor()
        sql =  f"SELECT * FROM veiculos WHERE ID = {id}"
        cursor.execute(sql)
        dados_recebidos = cursor.fetchall()  
        # print(dados_recebidos)
        # print(dados_recebidos[0][5]) #posição 
        
        x=data_int * dados_recebidos[0][6]
        
        # print(x)
        
        t=str(x)
        
        tela_aluguel_compra.total.setText(t)
            
def tela_adm_buscar_cliente():
    
    cpf = tela_adm.cpf_2.text()
    
    # print(cpf)
    
    # cpf2 = int(cpf)
    cursor = banco.cursor()
    print(cpf)
    sql =  f"SELECT * FROM clientes WHERE cpf = {cpf}"

    cursor.execute(sql)
    dados_recebidos = cursor.fetchall()  
    
    print("DADOS RECEBIDOSSSSSSSSSSSSSSSSSSSSSSSSS",dados_recebidos)  


    
    
    
    tela_adm.nome.setText(f"{dados_recebidos[0][1]}")
    tela_adm.email.setText(f"{dados_recebidos[0][3]}")
    tela_adm.telefone.setText(f"{dados_recebidos[0][4]}")
    tela_adm.senha.setText(f"{dados_recebidos[0][5]}")  
       
def atualizar_cliente():
    
    banco2 = Banco()
    
    nome = tela_adm.nome.text() 
    cpf = tela_adm.cpf_2.text()
    email = tela_adm.email.text() 
    telefone = tela_adm.telefone.text() 
    senha = tela_adm.senha.text()     
        
    dados = [str(nome),str(cpf),str(email),str(telefone),str(senha)]
    print(dados)
        
        
        
    banco2.atualizar_cliente_banco(dados)
    
def deletar_veiculo_por_id():
    
    banco2=Banco()
    
    id = tela_adm.id_veiculo.text()
    id2 = int(id)
    cursor = banco.cursor()
    sql =  f"SELECT * FROM veiculos WHERE id = {id2}"
    cursor.execute(sql)
    dados_recebidos = cursor.fetchone() 
    
    print(dados_recebidos)
     
    banco2.deletar_veiculo(id2)
    
def vender_veiculo():
    banco=Banco()   
    
    id_veiculo = tela_adm.id_veiculo_2.text()
    id_cliente = tela_adm.id_cliente3.text() 
    valor = tela_adm.valor.text() 
    
    dados=(id_veiculo,id_cliente,valor)
    
    banco.vender_veiculos(dados) 
    
    print("VENDEU")
      
tela_aluguel_compra.btn_buscar_id_veiculo.clicked.connect(consulta_veiculo) 

tela_aluguel_compra.btn_buscar_id_veiculo.released.connect(consulta_cpf)

tela_adm.btn_deletar_veiculo.clicked.connect(deletar_veiculo_por_id) 

tela_adm.atualizar_cliente.clicked.connect(atualizar_cliente) 

tela_adm.buscar_cpf.clicked.connect(tela_adm_buscar_cliente) 

tela_adm.btn_cadastrar_ADM.clicked.connect(cadastro_adm) 

tela_aluguel_compra.btn_alugar.clicked.connect(aluguel_veiculos) 

listar_usuarios.btn_cadastrar.clicked.connect(cadastrando_veiculos)

form_usuario.btn_cadastrar_cliente.clicked.connect(listar_dados_clientes)

form_usuario.btn_cadastrar_cliente.released.connect(cadastrando_cliente)

form_usuario.btn_voltar.released.connect(volta_tela_adm)

tela_aluguel_compra.btn_voltar.clicked.connect(volta_tela_adm)

tela_login.btn_login.clicked.connect(obter_perfil_do_cliente)

tela_login.btn_login.released.connect(fecha_tela_login)

tela_login.show() 

listar_usuarios.btn_voltar.clicked.connect(volta_tela_adm)

tela_adm.Vender.clicked.connect(vender_veiculo) 

tela_adm.cadastrar_veiculo_adm.clicked.connect(cadastrando_veiculos) 

# form_usuario.show()
# listar_usuarios.show()
# tela_login.close()
# tela_login.hide()

app.exec() 