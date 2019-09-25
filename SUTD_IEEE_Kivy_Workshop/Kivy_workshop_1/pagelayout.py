from kivy.app import App
from kivy.uix.pagelayout import PageLayout


class LayoutWindow(PageLayout):
    pass


class pagelayoutApp(App):
    def build(self):
        return LayoutWindow()


if __name__== "__main__":
    display = pagelayoutApp()
    display.run()