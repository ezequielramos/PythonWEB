from flask import Flask, request
import json


app = Flask(__name__)

#Query and Payload Params

@app.route('/login', methods=['POST', 'GET'])
def login():

	if request.method == 'GET':
		user = request.args.get('user')
		password = request.args.get('pass')

	if request.method == 'POST':
		dataDict = json.loads(request.data)
		user = dataDict["user"]
		password = dataDict["pass"]

	return "user:" + user + " pass:" + password

app.run(debug=True)