from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout




class CalculatorApp(App):
    def build(self):
        container = BoxLayout(orientation='vertical')

        self.label = Label(text='0', font_size='50')
        self.current_input = ''
        self.current_operation = ''

        buttons1 = ['1', '2', '3', '+', '<<']
        div1 = self.create_button_row(buttons1)

        buttons2 = ['4', '5', '6', '*', '**']
        main = self.create_button_row(buttons2)

        buttons3 = ['7', '8', '9', '-', 'R']
        footer = self.create_button_row(buttons3)

        buttons4 = ['C', '0', '.', '/','=']
        bottom = self.create_button_row(buttons4)

        container.add_widget(self.label)
        container.add_widget(div1)
        container.add_widget(main)
        container.add_widget(footer)
        container.add_widget(bottom)

        return container

    def create_button_row(self, button_texts):
        button_row = BoxLayout(orientation='horizontal')
        for text in button_texts:
            if text == '<<':
                button = Button(text=text, font_size=50)
                button.bind(on_release=self.delete_last_char)
            elif text == 'R':
                button = Button(text=text, font_size=50)
                button.bind(on_release=self.calculate_sqrt)
            elif text == 'C':
                button = Button(text=text, font_size=50)
                button.bind(on_release=self.reset)
            else:
                button = Button(text=text, font_size=50)
                button.bind(on_release=self.on_button_press)
            button_row.add_widget(button)
        return button_row

    def on_button_press(self, instance):
        button_text = instance.text
        if button_text == '=':
            self.calculate()
        else:
            self.current_input += button_text
            self.label.text = self.current_input

    def delete_last_char(self, instance):
        self.current_input = self.current_input[:-1]
        self.label.text = self.current_input

    def calculate(self):
        try:
            result = str(eval(self.current_input))
            self.label.text = result
            self.current_input = result
        except Exception as e:
            self.label.text = 'Error'
            self.current_input = ''

    def calculate_sqrt(self, instance):
        try:
            result = (float(self.current_input)) ** 0.5
            self.label.text = str(result)
            self.current_input = str(result)
        except ValueError:
            self.label.text = 'Error'
            self.current_input = ''

    def reset(self, instance):
        self.current_input = ''
        self.label.text = '0'

if __name__ == '__main__':
    CalculatorApp().run()
