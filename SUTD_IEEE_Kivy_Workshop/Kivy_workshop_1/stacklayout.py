from kivy.app import App
from kivy.uix.stacklayout import StackLayout


class LayoutWindow(StackLayout):
    pass


class stacklayoutApp(App):
    def build(self):
        return LayoutWindow()


if __name__== "__main__":
    display = stacklayoutApp()
    display.run()