from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class stackWindow(BoxLayout):
    pass


class stack_activityApp(App):

    def build(self):
        return stackWindow()


display = stack_activityApp()
display.run()