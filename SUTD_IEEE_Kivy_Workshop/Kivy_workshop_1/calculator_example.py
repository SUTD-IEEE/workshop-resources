from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class CalculatorWindow(BoxLayout):

    pass


class CalculatorApp(App):
    def build(self):
        return CalculatorWindow()


if __name__== "__main__":
    display = CalculatorApp()
    display.run()