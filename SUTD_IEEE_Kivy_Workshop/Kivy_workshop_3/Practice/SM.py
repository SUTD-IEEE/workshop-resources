from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class SM(BoxLayout):
    pass


class screenmanagerApp(App):
    def build(self):
        return SM()


display = screenmanagerApp()
display.run()