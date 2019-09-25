from kivy.uix.boxlayout import BoxLayout
from kivy.app import App


class ID(BoxLayout):

    def explode(self):
        explosion_button = self.ids.explosion
        try:
            if explosion_button.font_size == explosion_button.height:
                explosion_button.background_normal = "explosion.jpg"
                explosion_button.text = "EXPLODE!!!"
            else:
                explosion_button.font_size += 10
        except Exception as e:
            print(e)
            pass



class idApp(App):

    def build(self):
        return ID()

if __name__ == "__main__":
    calculator = idApp()
    calculator.run()

