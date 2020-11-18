from flask_login import LoginManager
from pony.orm import Database, Required, Optional
from flask_login import UserMixin
from datetime import datetime


db = Database()
login_manager = LoginManager()
login_manager.login_view = 'login'


class User(db.Entity, UserMixin):
    username = Required(str, unique=True)
    password = Required(str)
    last_login = Optional(datetime)


@login_manager.user_loader
def load_user(user_id):
    return db.User.get(id=user_id)
