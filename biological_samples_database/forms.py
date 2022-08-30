from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class SampleForm(FlaskForm):
    sampletype = StringField('stype', validators=[DataRequired(), Length(min=3, max=20)])
    pwid = StringField('stype', validators=[DataRequired(), Length(min=3, max=20)])

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    first = StringField('First Name', validators=[DataRequired(), Length(min=3, max=20)])
    second = StringField('Second Name', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max =20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=8, max =20), EqualTo('password')])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max =20)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')