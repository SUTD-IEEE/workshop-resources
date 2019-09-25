from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.lang.builder import Builder

# comment out this block and keep the run code to run this screen individually as an app
Builder.load_file("calculator.kv")

class calculatorWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def evaluate(self,inp):
        # This is where you do the error handling to make sure your app don't crash
        try:
            output = eval(inp)
            self.ids.display.text = str(output)
        except Exception as e:
            self.ids.display.text = str(e)

class calculatorApp(App):

    def build(self):
        return calculatorWindow()

# comment out this block if you want this be a screen in your app
# if __name__ == "__main__":
#     calculator = calculatorApp()
#     calculator.run()