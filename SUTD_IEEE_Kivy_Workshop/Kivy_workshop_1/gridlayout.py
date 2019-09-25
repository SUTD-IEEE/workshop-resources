from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class LayoutWindow(GridLayout):
    pass


class gridlayoutApp(App):
    def build(self):
        return LayoutWindow()


if __name__== "__main__":
    display = gridlayoutApp()
    display.run()