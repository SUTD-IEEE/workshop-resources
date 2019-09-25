from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class LayoutWindow(FloatLayout):
    pass


class floatlayoutApp(App):
    def build(self):
        return LayoutWindow()


if __name__== "__main__":
    display = floatlayoutApp()
    display.run()