from flask import redirect
from flask import url_for
from flask import Blueprint
from flask import render_template
from flask import flash
from flask import redirect
from flask import current_app
from flask import request
from flask import abort


from app.users.forms import RegisterForm
from app.users.forms import LoginForm

users: Blueprint = Blueprint('users', __name__)


@users.route('/')
def index():
	return redirect(url_for('.login'))


@users.route('/login')
def login():
	login_form = LoginForm()
	return 'page for logining'


@users.route('/register')
def register():
	register_form = RegisterForm()
	return 'page for reg'
