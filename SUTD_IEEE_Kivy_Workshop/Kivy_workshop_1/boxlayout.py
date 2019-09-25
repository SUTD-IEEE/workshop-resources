from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class LayoutWindow(BoxLayout):
    pass


class boxlayoutApp(App):
    def build(self):
        return LayoutWindow()


if __name__== "__main__":
    display = boxlayoutApp()
    display.run()