from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from database import Database

class TarefaApp(App):
    def build(self):
        self.banco = Database()
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Escolha Uma Das Opções Abaixo !")
        self.layout.add_widget(self.label)
        self.criar_botoes()
        return self.layout
    
    def criar_botoes(self):
        botoes = ["Cadastrar Nova Tarefa", "Atualizar Uma Tarefa",
                  "Listar Todas Tarefas Cadastradas", "Deletar Uma Tarefa", "Sair"]
        
        for texto in botoes:
            botao = Button(text=texto)
            botao.bind(on_release=self.acao_botao)
            self.layout.add_widget(botao)
    
    def acao_botao(self, instance):
        texto = instance.text
        if texto == "Cadastrar Nova Tarefa":
            self.cadastrar_tarefa()
        elif texto == "Atualizar Uma Tarefa":
            self.atualizar_tarefa()
        elif texto == "Listar Todas Tarefas Cadastradas":
            self.listar_tarefas()
        elif texto == "Deletar Uma Tarefa":
            self.deletar_tarefa()
        elif texto == "Sair":
            self.sair()
    
    def cadastrar_tarefa(self):
        nome_input = TextInput(hint_text="Nome da Tarefa")
        desc_input = TextInput(hint_text="Descrição da Tarefa")
        data_input = TextInput(hint_text="Data da Tarefa (Exemplo: 2023-10-05)")
        estado_input = TextInput(hint_text="Estado da Tarefa")
        cadastrar_button = Button(text="Cadastrar")
        
        def cadastrar_callback(instance):
            nome = nome_input.text
            desc = desc_input.text
            data = data_input.text
            estado = estado_input.text
            task = (nome, desc, data, estado)
            self.banco.insert(task)
            nome_input.text = ""
            desc_input.text = ""
            data_input.text = ""
            estado_input.text = ""
        
        cadastrar_button.bind(on_release=cadastrar_callback)
        
        self.layout.clear_widgets()
        self.layout.add_widget(self.label)
        self.layout.add_widget(nome_input)
        self.layout.add_widget(desc_input)
        self.layout.add_widget(data_input)
        self.layout.add_widget(estado_input)
        self.layout.add_widget(cadastrar_button)
    
    def atualizar_tarefa(self):
        # Implemente a lógica para atualizar uma tarefa aqui
        pass
    
    def listar_tarefas(self):
        # Implemente a lógica para listar as tarefas cadastradas aqui
        pass
    
    def deletar_tarefa(self):
        # Implemente a lógica para deletar uma tarefa aqui
        pass
    
    def sair(self):
        self.stop()

if __name__ == '__main__':
    TarefaApp().run()
