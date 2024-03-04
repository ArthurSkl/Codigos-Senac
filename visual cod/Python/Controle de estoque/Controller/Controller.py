from Model.model import EstoqueModel
import sys
import os

class EstoqueController:
    def __init__(self):
        # Inicialização do controlador...
        self.modelo = EstoqueModel()

    def cadastrar_produto(self, dados_json):
        # Chamar método de inserção no modelo
        self.modelo.inserir_item_estoque(dados_json)

    # Outros métodos relacionados à lógica de negócios...