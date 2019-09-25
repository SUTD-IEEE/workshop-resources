from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder

Builder.load_file("login.kv") # we use Builder to build our "login.kv" file instead using the
                              # run function at the bottom, when this python file is executed as one of the screens

class loginWindow(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # passing all the arguments

    def validate_user(self):
        # get the username and password
        usr = self.ids.username_filled
        pwd = self.ids.password_filled
        info = self.ids.info

        usr_name = usr.text
        passwrd = pwd.text

        if usr_name == "" or passwrd == "":
            print("Username and/or password required!")
            info.text = "[color=#a92536]Username and/or password required![/color]"
        elif usr_name == "admin" and passwrd == "admin":
            print("Logged In Successfully!")
            info.text = "[color=#2fb25b]Logged In Successfully![/color]"
            self.parent.parent.current = "calculator"
        else:
            print("Wrong username and/or password!")
            info.text = "[color=#a92536]Wrong username and/or password![/color]"


class loginApp(App):
    def build(self):
        return loginWindow()

# If Builder is run in front, run function
# if __name__ == "__main__":
#     display = loginApp()
#     display.run()