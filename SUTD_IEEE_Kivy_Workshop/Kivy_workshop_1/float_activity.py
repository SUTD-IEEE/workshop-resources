from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class IEEE_workshop(FloatLayout):
    pass


class float_activityApp(App):

    def build(self):
        return IEEE_workshop()


display = float_activityApp()
display.run()