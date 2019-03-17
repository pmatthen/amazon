from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
	username = 'Poulose'
	return render_template('home.html', title = 'home', name = username)

@app.route('/about')
def about():
	return render_template('about.html', title = 'about')

@app.route('/contact')
def contact():
	return render_template('contact.html', title = 'contact')

if __name__ == '__main__':
	app.run(debug = True)