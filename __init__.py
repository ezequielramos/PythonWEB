from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return "Hello World!"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User ' + username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post ' + str(post_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #do_the_login()
        pass
    else:
        #show_the_login_form()
        return "login_form"

app.run(debug=True)