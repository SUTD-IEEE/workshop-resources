# Special thanks to our IEEE Vice Pres Shi Hui who made this example!!

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class CustomScreen0(Screen):
    pass
class CustomScreen1(Screen):
    pass
class CustomScreen2(Screen):
    pass
class CustomScreen3(Screen):
    pass

class MultiScreenApp(App):

    def build(self):
        root = ScreenManager()
        for x in range(4):
            if x == 0:            
                root.add_widget(CustomScreen0(name='Screen %d' % x))
            elif x == 1:
                root.add_widget(CustomScreen1(name='Screen %d' % x))
            elif x == 2:
                root.add_widget(CustomScreen2(name='Screen %d' % x))
            else:
                root.add_widget(CustomScreen3(name='Screen %d' % x))
        return root

if __name__ == '__main__':
    display = MultiScreenApp()
    display.run()
