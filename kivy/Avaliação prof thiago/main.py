from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.pickers import MDDatePicker
from Banco import *
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.icon_definitions import md_icons
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import IRightBodyTouch, TwoLineAvatarIconListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.list import TwoLineAvatarIconListItem, ILeftBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox
from datetime import datetime


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
        scr2 = MDScreen(name="scr 2")
        
        
        return Builder.load_file('interface.kv')

    def get_dados(self):
        nome=self.root.ids.nome_cadastro.text
        # print(nome)
        descricao=self.root.ids.descricao_cadastro.text
        # print(descricao)
        self.data=self.root.ids.data.text 
        print("NAO TA PEGANDO DATA ",self.data)
        dados=[str(nome),str(descricao),str(self.data)]
        # print("TESTANDO CADASTROOOOOOOOOOO",dados)
        db = Banco()
        db.cadastro(dados)

        self.root.ids.nome_cadastro.text="" 
        self.root.ids.descricao_cadastro.text=""
        self.root.ids.data.text =""
      
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
        screen = Screen()
        self.root.ids.screen_manager.get_screen("scr 2").add_widget(screen)
 
    def on_start(self):
        self.banco=Banco()
        dados=self.banco.mostrar_dados()
        # icons = list(md_icons.keys())
        # print(dados)
        for i in range(len(dados)): 
            
            # msg = "".join(list(dados[i])) 
            # print(msg)
            msg = ""
            for x in dados[i]:
                msg += f"  {str(x)}  "
            
            
            self.root.ids.id_item_lista.add_widget(
            
                OneLineListItem(text=f"{msg}"),
            )
    
    def get_id(self):
        self.id=self.root.ids.id_tarefa.text
        # print(id)
        db = Banco()
        self.dados=db.consultar_tarefa(self.id)
        # print(self.dados)
        self.root.ids.nome.text=(f"{self.dados[0][1]}")
        self.root.ids.descricao.text=(f"{self.dados[0][2]}")
        self.root.ids.data.text=(f"{self.dados[0][3]}")
        
    def get_id_ATT(self):
        self.id=self.root.ids.id_tarefa_att.text
        # print(id)
        db = Banco()
        self.dados=db.consultar_tarefa(self.id)
        # print(self.dados)
        self.root.ids.nome_tarefa_att.text=(f"{self.dados[0][1]}")
        self.root.ids.descricao_tarefa_att.text=(f"{self.dados[0][2]}")
        self.root.ids.data.text=(f"{self.dados[0][3]}")    

    def atualizar (self):
        db = Banco()
        
        nome=self.root.ids.nome_tarefa_att.text
        desc=self.root.ids.descricao_tarefa_att.text
        data=self.root.ids.data.text
        
        db.atualizar_tarefa(self.id,nome,desc,data)
        
        
        
        self.root.ids.id_tarefa_att.text=""
        self.root.ids.nome_tarefa_att.text=""
        self.root.ids.descricao_tarefa_att.text=""
        self.root.ids.data.text=""
    
    def get_id_deletar(self):
        self.id=self.root.ids.id_tarefa_deletar.text
        # print(id)
        db = Banco()
        self.dados=db.consultar_tarefa(self.id)
        # print(self.dados)
        self.root.ids.nome_tarefa_deletar.text=(f"{self.dados[0][1]}")
        self.root.ids.descricao_tarefa_deletar.text=(f"{self.dados[0][2]}")
        self.root.ids.data.text=(f"{self.dados[0][3]}")
    
    def deletar_tarefa(self):
        
        db=Banco()
        id=self.root.ids.id_tarefa_deletar.text
        db.deletar_tarefa(id) 
        
        self.root.ids.id_tarefa_deletar.text=""    
        self.root.ids.nome_tarefa_deletar.text=""
        self.root.ids.descricao_tarefa_deletar.text=""
        self.root.ids.data.text =""
        
if __name__ == '__main__':
    app = Example()
    app.run()








