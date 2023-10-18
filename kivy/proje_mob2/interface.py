from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView

KV = '''
<ContentNavigationDrawer>

    MDList:

        OneLineListItem:
            text: "Screen 1"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 1"
                
                

        OneLineListItem:
            text: "Screen 2"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 2"


MDScreen:

    MDTopAppBar:
        pos_hint: {"top": 1}
        elevation: 4
        title: "MDNavigationDrawer"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:

        MDScreenManager:

        
            id: screen_manager

            MDScreen:
                name: "scr 1"

                MDLabel:
                    text: "Formulario De Cadastro"
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}



                MDTextField:
                    id: text_field_error6
                    hint_text: "Nome"
                    helper_text: "There will always be a mistake"
                    helper_text_mode: "on_error"
                    pos_hint: {"center_x": .5, "center_y": .7}
                    size_hint_x: .6  


                MDTextField:
                    id: text_field_error6
                    hint_text: "Descrição"
                    helper_text: "There will always be a mistake"
                    helper_text_mode: "on_error"
                    pos_hint: {"center_x": .5, "center_y": .6}
                    size_hint_x: .6  


                MDTextField:
                    id: text_field_error6
                    hint_text: "Data"
                    helper_text: "There will always be a mistake"
                    helper_text_mode: "on_error"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    size_hint_x: .6  

                MDTextField:
                    id: text_field_error6
                    hint_text: "Estado"
                    helper_text: "There will always be a mistake"
                    helper_text_mode: "on_error"
                    pos_hint: {"center_x": .5, "center_y": .4}
                    size_hint_x: .6      


                    
                           

            MDScreen:
                name: "scr 2"

                MDLabel:
                    text: "Screen 2"
                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''


class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class Example(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)



Example().run()