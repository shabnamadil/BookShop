from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email, Length, ValidationError



class Review(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(max=30)])
    email = StringField('email', validators=[DataRequired(), Email(), Length(max=30)])
    comments = TextAreaField('message', validators=[DataRequired()])


class RegisterForm(FlaskForm):
    def validate_email(form,field):
      if not field.data:
         raise ValidationError()
    name = StringField('name', validators=[DataRequired(), Length(max=30)])
    username = StringField('name', validators=[DataRequired(), Length(max=30)])
    email = StringField('email', validators=[DataRequired(), Email(), validate_email, Length(max=30)])
    password = StringField('password', validators=[DataRequired(), Length(min=8, max=30)])
    


class LoginForm(FlaskForm):
    username = StringField('name', validators=[DataRequired(), Length(max=30)])
    password = StringField('password', validators=[DataRequired(), Length(min=8, max=30)])
    signed_in = BooleanField('signed_in')
    