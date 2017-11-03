from flask import Flask
app = Flask(__name__)

#Path Params

@app.route('/sayYourName/<name>')
def sayYourName(name):
	return '''<html>
<head>
	<title>''' + name + '''</title>
</head>
<body>
	<h1>Hello, ''' + name + '''</h1>
</body>
</html>'''

app.run()