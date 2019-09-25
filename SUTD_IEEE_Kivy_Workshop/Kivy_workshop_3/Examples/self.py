from kivy.uix.boxlayout import BoxLayout
from kivy.app import App


class selfWindow(BoxLayout):
    pass

class selfApp(App):

    def build(self):
        return selfWindow()

if __name__ == "__main__":
    calculator = selfApp()
    calculator.run()