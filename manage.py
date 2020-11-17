from app import create_app


from flask_script import Manager
from flask import render_template, redirect, url_for


app = create_app('config.DevelopmentConfig')
# app = create_app()


@app.route('/')
def homepage():
	return render_template('index.html')


@app.route('/index')
def index():
	return redirect(url_for('.homepage'))


@app.route('/register')
def register():
	return 'register page'


@app.route('/logining')
def logining():
	return redirect(url_for('users.login'))


manager = Manager(app)


if __name__ == '__main__':
	# print(app.url_map)
	manager.run()
