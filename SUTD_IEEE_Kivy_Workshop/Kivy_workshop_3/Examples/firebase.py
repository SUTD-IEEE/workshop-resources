from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import firebase_admin
from firebase_admin import credentials, firestore

# Initialise your firebase and database
cred = credentials.Certificate("<Here put in the admin SDK .json file>") # this is the security key to your firebase account
FireBase = firebase_admin.initialize_app(cred) # this is your firebase instance
db = firestore.client() # this is your database instance



collection = db.collection(u'<your collection name>')
output = collection.document(u'<your document name>').get() # This will return you a Google cloud object
username = output.to_dict()['name'] # use .to_dict() method to convert output to a python dictionary

# if you are not sure, try print out the output and see what does it look like, what is its type
# print(output.to_dict())


class mainWindow(BoxLayout):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    # this is the funciton that will be executed when SUBMIT button is pressed
    def send_info(self):
        NAME = self.ids.username.text # get the username input
        AGE = self.ids.age.text # get the age input

        # use .set() method to update your firestore data. If name of document not found, it will
        # automatically create a new document.
        # inside set() need to put as a dictionary format, with keys and values
        collection.document(NAME).set(
            {
                u"name": NAME,
                u"age": AGE
            }
        )


class firebaseApp(App):
    def build(self):
        return mainWindow()


if __name__ == "__main__":
    display = firebaseApp()
    display.run()