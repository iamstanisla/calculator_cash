from app.users.forms import RegisterForm
from app.users.forms import LoginForm
from app.users.models import db
from app.users.models import User
from app.users.models import login_manager


from typing import Union


from flask import redirect
from flask import url_for
from flask import Blueprint
from flask import render_template
from flask import flash
from flask import redirect
from flask import current_app
from flask import request
from flask import abort
from flask_login import login_user


users: Blueprint = Blueprint('users', __name__)


@users.route('/')
def index():
	return redirect(url_for('.login'))


@users.route('/login', methods=['GET', 'POST'])
def login():
    contact_form = LoginForm(meta={'csrf': False})
    if request.method == 'POST' and contact_form.validate():
        username: str = contact_form.username.data
        password: str = contact_form.password.data
        # email: str = contact_form.email.data

        possible_user: Union[User, None] = User.get(login=username, password=password)
        if not possible_user:
            flash('check the entered data correctly', 'warning')
            return render_template('users/login.html', contact=contact_form)
        elif possible_user.password == password:
            possible_user.last_login = datetime.now()
            login_user(possible_user)
            return redirect(url_for('.index'))
        else:
            flash('Wrong password')
            return redirect(url_for('.login'), contact=contact_form)
    else:
        return render_template('users/login.html', contact=contact_form)




@users.route('/register')
def register():
	register_form = RegisterForm()
	return 'page for reg'
