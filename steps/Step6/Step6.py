from flask import Flask, request, render_template
app = Flask(__name__)

#form

@app.route('/')
@app.route('/index')
def index():

	user = request.args.get('user')
	password = request.args.get('pass')

	if user and password:
		users.append({
			"user":user,
			"password":password
		})

	return render_template('index.html',user=user,password=password)

#list
@app.route('/list')
def list_users():
	return render_template('list.html',users=users)

users = []

app.run()