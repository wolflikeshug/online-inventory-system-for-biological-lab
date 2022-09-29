from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp, InputRequired
from .model.user import Group, User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    first = StringField('First Name', validators=[DataRequired(), Length(min = 1, max=20),
    Regexp(r"^[a-zA-Z]+$",message="Names may only contain letters.")])
    last = StringField('Last Name', validators=[DataRequired(), Length(min= 1, max=20),
    Regexp(r"^[a-zA-Z]+$",message="Names may only contain letters.")])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max =20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=8, max =20), EqualTo('password')])
    submit = SubmitField('Submit')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already taken')
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already taken')



class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max =20)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')



class CreateAdminForm(FlaskForm):
    
    group = SelectField(u'Set My Role:',choices=[(member.value, member.name)for member in Group], validators=[DataRequired()])
    submit = SubmitField('Submit')

class DeleteUserForm(FlaskForm):
    deluser = SelectField(u'Delete User:')
    delete = SubmitField('Delete')

    @classmethod
    def new(cls):
        form = cls()

        form.deluser.choices = [(user.id, user.first+" "+user.last)for user in User.query.all() ]

        return form

class UploadFileForm(FlaskForm):
    file = FileField("Excel File", validators=[InputRequired(), FileAllowed(['xlsx'])])
    submit = SubmitField("Upload")