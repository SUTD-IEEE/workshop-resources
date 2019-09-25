from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class calWin(BoxLayout):
    pass


class calApp(App):

    def build(self):
        return calWin()


if __name__ == "__main__":
    display = calApp()
    display.run()
