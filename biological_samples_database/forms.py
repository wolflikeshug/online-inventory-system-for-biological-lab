from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, DateField, SelectMultipleField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp, InputRequired, Optional
from .model.user import Group, User
from datetime import datetime
from .model import Base
from .model.sample import Vial


vial = None
sample_classes = []
    
for mapper in Base.registry.mappers:
    table = mapper.class_
    vial_subclass = issubclass(table, Vial)
    if vial_subclass and table.__tablename__ == 'vial':
        vial = table
    elif vial_subclass:
        sample_classes.append(table)

sample_classes = sorted(sample_classes, key=lambda h: h.__tablename__)
sample_names = []
for sample in sample_classes:
    name = ''
    print(sample.__tablename__.replace('_',' ').capitalize())
    for name_part in sample.__tablename__.split('_'):
        name.join(name_part.capitalize())
    sample_names.append(name)
print(sample_names)
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

class SearchForm(FlaskForm):
    '''Sample specific data'''
    
    sample_type = SelectMultipleField(choices = [name for name in sample_names] , default = [False, "Sample Type"], validators=([Optional()]))
    '''Serum_sele = BooleanField('Serum', default=False)
    Virus_Isolation_sele = BooleanField('Virus Isolation', default=False)
    Virus_Culture_sele = BooleanField('Virus Culture', default=False)
    Plasma_sele = BooleanField('Plasma', default=False)
    PBMC_sele = BooleanField('PBMC', default=False)
    Cell_Line_sele = BooleanField('Cell Line', default=False)
    Mosquito_sele = BooleanField('Mosquito', default=False)
    Antigen_sele = BooleanField('Antigen', default=False)
    Rna_sele = BooleanField('Rna', default=False)
    Peptide_sele = BooleanField('Peptide', default=False)
    Supernatant_sele = BooleanField('Supernatant', default=False)
    Other_sele = BooleanField('Other', default=False)'''

    pw_id = StringField('PW_ID', validators=([Optional()]))
    id = StringField('Lab ID', validators=([Optional()]))
    cell_type = StringField('Type', validators=([Optional()]))

    start_date = DateField(
        'Start Date',
        default=datetime.strptime(
            '2022-01-01',
            '%Y-%m-%d'),
        format='%Y-%m-%d'
    , validators=([Optional()]))
    end_date = DateField(
        'End Date(This need to be later than the start date)',
        default=datetime.strptime(
            '2022-01-01',
            '%Y-%m-%d'),
        format='%Y-%m-%d'
    , validators=([Optional()]))
    need_date = BooleanField('Search in Date Range', default=False, validators=([Optional()]))

    visit_number = IntegerField('Visit Number', validators=([Optional()]))
    batch_number = IntegerField('Batch Number', validators=([Optional()]))
    passage_number = IntegerField('Passage Number', validators=([Optional()]))
    cell_count = IntegerField('Total Count', validators=([Optional()]))
    growth_media = StringField('Media', validators=([Optional()]))
    vial_source = StringField('Source', validators=([Optional()]))
    lot_number = StringField('Lot Number', validators=([Optional()]))
    volume_ml = FloatField('Volume (ml)', validators=([Optional()]))
    patient_code = StringField('Patient Code', validators=([Optional()]))
    user_id = StringField('Initials', validators=([Optional()]))
    notes = StringField('Other', validators=([Optional()]))
    submit = SubmitField("Search", validators=([Optional()]))
