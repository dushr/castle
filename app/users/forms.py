from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, BooleanField
from wtforms.validators import Required, EqualTo, Email


class LoginForm(Form):
    email = TextField('Email', [Required(), Email()])
    password = PasswordField('Password', [Required()])

class RegisterForm(Form):

    name = TextField('Name', [Required()])
    email = TextField('Email', [Required(), Email()])
    password = PasswordField('Password', [Required()])
    confirm = PasswordField('Repeat', [
        Required(),
        EqualTo('password', message='Passwords must match')
    ])
    accept_tos = BooleanField('Accept TOS', [Required()])
