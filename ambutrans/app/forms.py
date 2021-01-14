from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User

SEX_CHOICES = [('1', 'M'), ('2','V'), ('3','X')]

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    
    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')

    def validate_username(self, username):

        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

def validate_email(self, email):

        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    
    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    
    remember = BooleanField('Remember Me')
    
    submit = SubmitField('Login')

class PatientForm(FlaskForm):

    first_name = StringField('Voornaam', validators=[DataRequired(), Length(min=2, max=20)])
    
    last_name= StringField('Achternaam', validators=[DataRequired(), Length(min=2, max=40)])

    rijksregisternummer = IntegerField('Rijksregisternr', validators=[DataRequired(), Length(min=11, max=11)])

    sex = SelectField('Geslacht', choices = SEX_CHOICES)

    from_hospital = StringField('Ziekenhuis vertrek', validators=[DataRequired(), Length(min=2, max=40)])

    too_hospital = StringField('Ziekenhuis aankomst', validators=[DataRequired(), Length(min=2, max=40)])


