from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.pickers import MDDatePicker
from Banco import *
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.icon_definitions import md_icons
from kivymd.uix.screen import MDScreen




class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    
class ListItemWithCheckbox(OneLineAvatarIconListItem):
    '''Custom list item.'''
    
    
class Example(MDApp):
    
    def build(self):
        screen_manager = MDScreen()    
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"
        
        scr2 = MDScreen(name="scr 2")
        screen_manager.add_widget(scr2)
        
        
        return Builder.load_file('interface.kv')

    def get_dados(self):

        nome=self.root.ids.nome.text
        descricao=self.root.ids.descricao.text
        self.data=self.root.ids.data.text
        
        # estado=self.root.ids.estado.text

        # print(nome,descricao,self.data,estado)

        # dados=[nome,descricao,self.data,estado]
        
        db = Banco()
        dados=[str(nome),str(descricao),str(self.data)]
        db.cadastro(dados)

        self.root.ids.nome.text=""
        self.root.ids.descricao.text=""
        self.root.ids.data.text = ""
        # self.root.ids.estado.text=""
      


    def on_save(self, instance, value, date_range):
        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;
        :param value: selected date;
        :type value: <class 'datetime.date'>;
        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''

        # print(instance, value, date_range)
        # print(value)
        # print(self.data)
        self.root.ids.data.text=str(value)
        self.data=value
        

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()    

    # def listar_tarefas(self):
        
    #     #define a tela 
        screen = Screen()

    #     #define a tabela
    #     tabela = MDDataTable(
    #         pos_hint={'center_x': 0.5, 'center_y': 0.5},
    #         size_hint=(0.9, 0.6),
    #         use_pagination=True,  # Você pode querer habilitar a paginação para conjuntos de dados grandes
    #         column_data=[
    #             ("Nome", dp(30)),
    #             ("Sobrenome", dp(30)),
    #             ("Email", dp(30))
    #         ],
    #         row_data=[
    #             ("Arthur", "Frantz", "email@hotmail.com"),
    #             ("João", "João", "email@hotmail.com")
    #         ]
    #     )
    #     screen.add_widget(tabela)

    #     return screen
        self.root.ids.screen_manager.get_screen("scr 2").add_widget(screen)

    # def listar_tarefas(self):
    #     # Crie a tabela de tarefas
    #     tabela = MDDataTable(
    #         pos_hint={'center_x': 0.5, 'center_y': 0.5},
    #         size_hint=(0.9, 0.6),
    #         use_pagination=True,  # Você pode querer habilitar a paginação para conjuntos de dados grandes
    #         column_data=[
    #             ("Nome", dp(30)),
    #             ("Sobrenome", dp(30)),
    #             ("Email", dp(30))
    #         ],
    #         row_data=[
    #             ("Arthur", "Frantz", "email@hotmail.com"),
    #             ("João", "João", "email@hotmail.com")
    #         ]
    #     )

    #     # Adicione a tabela à tela "scr 2" usando o gerenciador de tela
    #     self.root.ids.screen_manager.get_screen("scr 2").add_widget(tabela)

    # def add_item_to_list(self, text):
    #         # Crie uma instância de OneLineListItem com o texto fornecido
    #         item = OneLineListItem(text=text)
    #         # Acesse o MDList através do seu ID e adicione o item
    #         self.root.ids.id_item_lista.add_widget(item)        

    def on_start(self):
        self.banco=Banco()
        dados=self.banco.mostrar_dados()
        icons = list(md_icons.keys())
        print(dados)
        for i in range(len(dados)):
            informacoes=dados[i]
            print(informacoes)
            print(informacoes[1])
            self.root.ids.id_item_lista.add_widget(
                OneLineListItem(text=f"{dados[i]}"),
            )
    # def on_start(self):
    #     icons = list(md_icons.keys())
    #     for i in range(20):
    #         self.root.ids.id_item_lista.add_widget(
    #             OneLineListItem(text=f"Single-line item {i}"),
    #             # ListItemWithCheckbox(text=f"Item {i}", icon=icons[i])
    #         )
            
            
    




if __name__ == '__main__':
    app = Example()
    app.run()








