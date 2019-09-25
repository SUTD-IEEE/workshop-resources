from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class LayoutWindow(BoxLayout):
    pass


class grid_activityApp(App):
    def build(self):
        return LayoutWindow()


if __name__== "__main__":
    display = grid_activityApp()
    display.run()