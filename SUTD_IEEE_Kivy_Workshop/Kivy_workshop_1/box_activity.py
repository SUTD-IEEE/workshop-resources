from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class LayoutWindow(BoxLayout):
    pass


class box_activityApp(App):
    def build(self):
        return LayoutWindow()


if __name__== "__main__":
    display = box_activityApp()
    display.run()

