import sqlite3
import os
import sys


class Banco:
    
    def __init__(self):
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))

        caminho_banco_dados = os.path.join(diretorio_atual, 'estoque.db')


        conexao = sqlite3.connect(caminho_banco_dados)



        comando_insert = '''
        INSERT INTO estoque (modelo, numero, pecas)
        VALUES (?, ?, ?);
        '''