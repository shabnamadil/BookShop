from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email, Length



class Review(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(max=30)])
    email = StringField('email', validators=[DataRequired(), Email(), Length(max=30)])
    comments = TextAreaField('message', validators=[DataRequired()])
    