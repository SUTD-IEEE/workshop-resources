from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
# from calculator module import calculator window class
# from login module import login window class

class mainWindow(BoxLayout):
    pass
    # store both calculator and login windows as two variables in this class
    # initialise this class with passing all keyword arguments (**kwargs)
        # add the two windows under the screen of the screenmananger in this class (use add_widget() method)


class mainApp(App):
    def build(self):
        return mainWindow()



if __name__ == "__main__":
    display = finalApp()
    display.run()