from flask import Flask
app = Flask(__name__)

#Hello World! :)

@app.route("/")
def hello():
	return "Hello World!"

app.run(debug=True)