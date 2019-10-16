from flask import Flask, render_template, request, flash
from firebase_admin import credentials, firestore
import firebase_admin


app = Flask(__name__)

creds = credentials.Certificate("ieeeworkshopiot.json")
firebase = firebase_admin.initialize_app(creds)
db = firestore.client()

led = db.collection(u'led').document(u'led1')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        data = request.form['led_btn']
        if data == "OFF":
            # TURNED ON
            flash("LED has been turned ON!")
            data = "ON"
            led.update({
                'state': True
            })
            return render_template("index.html", data=data)
        else:
            # TURNED OFF
            data = "OFF"
            led.set({
                'state': False
            })
            flash("LED has been turned OFF!")
            return render_template("index.html", data=data)
    led.set({
        'state': False
    })
    return render_template("index.html", data="OFF")


if __name__ == '__main__':
    app.secret_key = "IEEEFLASK"
    app.run(debug=True, port=5000, host='0.0.0.0')
