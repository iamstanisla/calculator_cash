from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo


class RegisterForm(FlaskForm):
    first_name = StringField("first name: ", validators=[DataRequired()])
    second_name = StringField("second name: ", validators=[DataRequired()])
    username = StringField("username: ", validators=[DataRequired()])
    email = StringField("email: ", validators=[Email()])
    password = PasswordField("password", validators=[DataRequired()])
    confirm = PasswordField("repeat password", validators=[DataRequired(), EqualTo('password', 'password must match')])

    submit = SubmitField("Submit")


class LoginForm(FlaskForm):
    username = StringField("username: ", validators=[DataRequired()])
    password = PasswordField("password")
    submit = SubmitField("Submit")
