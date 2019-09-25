from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class myscreen(BoxLayout):
    pass


class screenmanagerApp(App):
    def build(self):
        return myscreen()


display = screenmanagerApp()
display.run()