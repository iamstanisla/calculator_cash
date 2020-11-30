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
from flask import session
from flask_login import login_user
from flask_login import login_required
from flask_login import logout_user
from pony.orm import flush


users: Blueprint = Blueprint('users', __name__)


@users.route('/')
def index():
    return redirect(url_for('.login'))


@users.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(meta={'csrf': False})
    if login_form.validate_on_submit():
        username: str = login_form.username.data
        password: str = login_form.password.data

        possible_user: Union[User, None] = User.get(username=username)
        if possible_user is None:
            flash(f'User with username \"{username}\" does not exist', 'error')
            return render_template('users/login.html', login_form=login_form)
        elif possible_user.check_hash_password(password):
            possible_user.last_login = datetime.now()
            login_user(possible_user)
            flash('Authorization was successful!')
            current_app.logger.info(f'User \'{possible_user.username}\' was logged. ')
            return redirect(url_for('homepage'))
        else:
            # current_app.logger.warning('User')
            flash('Wrong password!', 'error')
            return render_template('users/login.html', login_form=login_form)
    else:
        return render_template('users/login.html', login_form=login_form)


@users.route('/logout')
@login_required
def logout():
    logout_user()
    # user_id = session.get('_user_id')
    # print(session)
    # user = User.get(id=user_id)
    # print(user)
    # current_app.logger.info(f'User \'{user.username} was logout.\'')
    return redirect(url_for('homepage'))


@users.route('/register', methods=['GET', 'POST'])
def register():
    reg_form = RegisterForm(meta={'csrf': False})
    if reg_form.validate_on_submit():
        username: str = reg_form.username.data
        password: str = reg_form.password.data
        first_name: str = reg_form.first_name.data
        second_name: str = reg_form.second_name.data
        email: str = reg_form.email.data

        exit_username: Union[User, None] = User.get(username=username)
        exit_email: Union[User, None] = User.get(email=email)
        if exit_username:
            flash(f'Username \'{username}\' is already taken, choose another one')
            current_app.logger.warning(f'trying to use an existing username \'{username}\'')
            return redirect(url_for('.register'))
        elif exit_email:
            flash(f'email \'{email}\' is already taken, choose another one')
            current_app.logger.warning(f'trying to use an existing email \'{email}\'')
            return redirect(url_for('.register'))
        else:
            # create instance of User
            user = User(
                username=username,
                password=password,
                first_name=first_name,
                second_name=second_name,
                email=email,
                last_login=datetime.now()
                )
            user.set_hash_password(password)

            current_app.logger.info(f'add a new user \'{user.username}\'.')
            flush()
            login_user(user)
            current_app.logger.info(f'user \'{user.username}\' logged in {user.last_login}.')
            flash('Successfully registered')
            return redirect(url_for('homepage'))
    else:
        return render_template('users/register.html', contact=reg_form)
