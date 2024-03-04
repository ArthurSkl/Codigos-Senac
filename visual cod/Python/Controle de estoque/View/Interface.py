from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5 import uic
import sys
sys.path.append('./')
from Controller.Controller import EstoqueController




controler = EstoqueController()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Controle de estoque/View/tela_cadastro.ui", self)

           # Conectar botão a uma função
        self.pushButton.clicked.connect(self.obter_dados_produto)

        # Exibir a janela
        self.show()

    def obter_dados_produto(self):
        modelo = self.lineEdit.text()
        numero = self.lineEdit_2.text()
        pecas = self.lineEdit_3.text()

        dados_produto = {
            "modelo": modelo,
            "numero": numero,
            "pecas": pecas
        }

        print(dados_produto)
        controler.cadastrar_produto(dados_produto)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())        

