from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.lang.builder import Builder

Builder.load_file("calculator.kv")

class calculatorWindow(BoxLayout):

    def evaluation(self):
        TextInput = self.ids.display
        try:
            results = eval(TextInput.text) # this is not a string
            results = str(results)
            TextInput.text = results
        except:
            TextInput.text = "Please input a valid operation!!!"



class calculatorApp(App):

    def build(self):
        return calculatorWindow()


if __name__ == "__main__":
    calculator = calculatorApp()
    calculator.run()
