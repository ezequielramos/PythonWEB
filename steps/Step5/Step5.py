from flask import Flask, render_template
app = Flask(__name__)

#sayYourName

@app.route('/sayYourName/<name>')
def sayYourName(name):
	return render_template('index.html',name=name)

#hello

@app.route('/hello/')
def hello_no_name():
	return render_template('control_statemantes.html')

@app.route('/hello/<name>')
def hello(name):
	return render_template('control_statemantes.html',name=name)

#loop

@app.route('/loop')
def loop():
	users = [{
		"name":"Ezequiel",
		"pass":"helloWorld"
	},{
		"name":"test",
		"pass":"test"
	}]
	return render_template('loop.html',users=users)

app.run(debug=True)