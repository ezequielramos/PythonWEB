from flask import Flask
app = Flask(__name__)

@app.route('/sayYourName/<name>')
def sayYourName(name):
	return name

@app.route('/sayYourAge/<int:number>')
def sayYourAge(number):
	return str(number + 3)

app.run(debug=True)