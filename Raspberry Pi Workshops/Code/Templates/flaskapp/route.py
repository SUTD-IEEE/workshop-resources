from flask import Flask, render_template, request
import serial

ser = serial.Serial('/dev/ttyUSB0',9600)

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
	if request.method == 'POST':
		input = request.form['points']
		input = str(input) + '\n'
		if not ser.isOpen():
			ser.open()
		ser.write(str.encode(input))
		ser.close()
		return render_template('page.html',num=request.form['points'])
	elif request.method == 'GET':
		print(request.method)
		return render_template('page.html',num=0)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=80)
