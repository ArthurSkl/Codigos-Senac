from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDBoxLayout:
    padding: "10dp"

    MDProgressBar:
        value: 75
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()