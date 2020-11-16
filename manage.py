from app import create_app


from flask_script import Manager
from flask import render_template


app = create_app('config.DevelopmentConfig')
# app = create_app()


@app.route('/')
def homepage():
	app.logger.info('asdfasdf')
	return render_template('index.html')


@app.route('/index')
def index():
	return 'Index page'


@app.route('/register')
def register():
	return 'register page'


@app.route('/logining')
def logining():
	return 'login page'


manager = Manager(app)


if __name__ == '__main__':
	# print(app.url_map)
	manager.run()
