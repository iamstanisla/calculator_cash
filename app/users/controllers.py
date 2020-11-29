from app.users.forms import RegisterForm
from app.users.forms import LoginForm
from app.users.models import db
from app.users.models import User
from app.users.models import login_manager


from typing import Union
from datetime import datetime


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
from flask_login import login_required
from flask_login import logout_user
from pony.orm import flush


users: Blueprint = Blueprint('users', __name__)


@users.route('/')
@login_required
def index():
    return redirect(url_for('.login'))


@users.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(meta={'csrf': False})
    if login_form.validate_on_submit():
        username: str = login_form.username.data
        password: str = login_form.password.data

        possible_user: Union[User, None] = User.get(username=username, password=password)
        if not possible_user:
            flash('Wrong username or password!', 'error')
            return render_template('users/login.html', login_form=login_form)
        elif possible_user.password == password:
            possible_user.last_login = datetime.now()
            login_user(possible_user)
            flash('Authorization was successful!')
            current_app.logger.info(f'User \'{possible_user.username}\' was logged successfully! ')
            return redirect(url_for('homepage'))
        else:
            # current_app.logger.warning('User')
            flash('Wrong username or password!', 'error')
            return redirect(url_for('.login'), login_form=login_form)
    else:
        return render_template('users/login.html', login_form=login_form)


@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))


@users.route('/register', methods=['GET', 'POST'])
def register():
    reg_form = RegisterForm(meta={'csrf': False})
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data
        first_name = reg_form.first_name.data
        second_name = reg_form.second_name.data
        email = reg_form.email.data

        exist = db.User.get(username=username)
        if exist:
            flash('Username %s is already taken, choose another one' % username)
            current_app.logger.info(f'username {username} already exit.')
            return redirect(url_for('.register'))
        else:
            user = db.User(username=username, password=password)
            user.last_login = datetime.now()
            current_app.logger.info(f'add a new user {user.username}.')
            flush()
            login_user(user)
            current_app.logger.info(f'user {user.username} logged in {user.last_login}.')
            flash('Successfully registered')
            return redirect(url_for('homepage'))
    else:
        # current_app.logger.info(f'error in time logining. error log: -> {reg_form.errors}.')
        return render_template('users/register.html', contact=reg_form)
