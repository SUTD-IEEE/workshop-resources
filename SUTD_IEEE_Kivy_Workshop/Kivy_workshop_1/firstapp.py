from kivy.app import App
from kivy.uix.label import Label

class Hello_kivy(App):

    def build(self):
        return Label(text="Hello Kivy!")


if __name__ == "__main__": # this is just a safety check to make sure this file is run as a main file, not imported by someone else
    display = Hello_kivy()
    display.run()

