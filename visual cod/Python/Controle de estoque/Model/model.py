import sqlite3
import os
import sys



class EstoqueModel:
    def __init__(self):
        # Obter o diretório do script atual
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))

        # Combinar o diretório atual com o nome do arquivo do banco de dados
        caminho_banco_dados = os.path.join(diretorio_atual, 'estoque.db')

        # Criar uma conexão com o banco de dados usando o caminho especificado
        self.conexao = sqlite3.connect(caminho_banco_dados)
        self.cursor = self.conexao.cursor()

    def inserir_item_estoque(self, dados_json):
        modelo = dados_json.get('modelo')
        numero = dados_json.get('numero')
        pecas = dados_json.get('pecas')
        
        comando_insert = '''
        INSERT INTO estoque (modelo, numero, pecas)
        VALUES (?, ?, ?);
        '''
        # Executar o comando SQL com os valores fornecidos
        self.cursor.execute(comando_insert, (modelo, numero, pecas))
        # Commit para salvar as alterações no banco de dados
        self.conexao.commit()

    # Outros métodos relacionados ao banco de dados...

    def fechar_conexao(self):
        # Fechar a conexão com o banco de dados
        self.conexao.close()