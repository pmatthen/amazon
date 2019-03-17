from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def home():
	username = 'Poulose'
	return render_template('home.html', title = 'Home', name = username, home = 'home')

@app.route('/about')
def about():
	return render_template('about.html', title = 'About')

@app.route('/contact')
def contact():
	return render_template('contact.html', title = 'Contact')

if __name__ == '__main__':
	app.run(debug = True)