from kivy.app import App
from kivy.uix.label import Label
from math_operation import math_operation # this is where we import the class we create

class Hello_kivy(App): # our app class object inherits the App class from official Kivy library

    def build(self):
        a = math_operation(10,20) # instantiate class object
        b = a.output() # call out function under the class
        return Label(text=b) # return a label object to the kivy screen


if __name__ == "__main__":
    display = Hello_kivy() # instantiate our app class object
    display.run() # run the kivy app

