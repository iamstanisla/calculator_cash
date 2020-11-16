from flask import redirect
from flask import url_for
from flask import Blueprint
from flask import render_template
from flask import flash
from flask import redirect
from flask import current_app
from flask import request
from flask import abort


users: Blueprint = Blueprint('users', __name__)


@users.route('/')
def index():
	return redirect(url_for('.login'))


@users.route('/login')
def login():

	return 'page for logining'
