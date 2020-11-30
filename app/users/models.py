from datetime import datetime


from flask_login import LoginManager
from flask_login import UserMixin
from pony.orm import Database, Required, Optional, PrimaryKey
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


db = Database()
login_manager = LoginManager()
login_manager.login_view = 'users.login'


class User(UserMixin, db.Entity):
    username=Required(str, unique=True)
    email=Required(str, unique=True)
    first_name=Required(str)
    second_name=Required(str)
    password=Required(str)
    last_login=Optional(datetime)

    def set_hash_password(self, password):
        self.password=generate_password_hash(
            password,
            method='sha256'
        )

    def check_hash_password(self, password):
        return check_password_hash(
            self.password,
            password
        )

    def __repr__(self):
        return f'<User {self.username}>'


@login_manager.user_loader
def load_user(user_id):
    return db.User.get(id=user_id)
