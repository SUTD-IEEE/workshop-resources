from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from Practice.login import loginWindow
from Practice.calculator import calculatorWindow

class mainWindow(BoxLayout):
    login_page = loginWindow()
    calculator_page = calculatorWindow()

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        main_login_screen = self.ids.login
        main_cal_screen = self.ids.calculator

        # add the window into the screen
        main_login_screen.add_widget(self.login_page)
        main_cal_screen.add_widget(self.calculator_page)


class finalApp(App):
    def build(self):
        return mainWindow()


if __name__ == "__main__":
    display = finalApp()
    display.run()