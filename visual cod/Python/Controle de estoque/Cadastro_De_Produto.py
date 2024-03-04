from Controller.Controller import EstoqueController
from View.Interface import *
import sys
import os



app = QApplication(sys.argv)

# Criar uma instância da MainWindow
view = MainWindow()
view.show()
# Obter o diretório do script atual
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Adicionar o diretório do projeto ao sys.path
sys.path.append(os.path.join(diretorio_atual, '..'))

# produto = {
#     "modelo": "4330",
#     "numero": 1,
#     "peças": 100
# }


controller = EstoqueController()

modelo = ""
numero = ""
pecas = ""

modelo=input(str("Digite o modelo do produto."))
numero=input(str("qual o tamanho do alzol."))
pecas=input(str("quantas unidades por caixa ou pacote ?"))

# print(modelo)
# print(numero)
# print(pecas)

produto = {
    "modelo": modelo,
    "numero": numero,
    "pecas": pecas
}


# Chamada do método de cadastro no controlador
# controller.cadastrar_produto(produto)


