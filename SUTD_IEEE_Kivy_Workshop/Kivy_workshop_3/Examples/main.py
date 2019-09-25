from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from Examples.login import loginWindow
from Examples.calculator import calculatorWindow

class mainWindow(BoxLayout):
    login_page = loginWindow()
    calculator_page = calculatorWindow()

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        main_login_screen = self.ids.login
        main_cal_screen = self.ids.calculator
        main_login_screen.add_widget(self.login_page)
        main_cal_screen.add_widget(self.calculator_page)


class mainApp(App):
    def build(self):
        return mainWindow()


if __name__ == "__main__":
    display = mainApp()
    display.run()