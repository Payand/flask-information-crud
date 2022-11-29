import email
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField
from wtforms.validators import DataRequired,Length,Email




class InformationForm(FlaskForm):
    first_name = StringField('Firstname',validators=[DataRequired(),Length(min=3 ,max=30)])
    last_name = StringField('Lastname',validators=[DataRequired(),Length(min=3,max=30)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    phone_number=IntegerField('Phone number',validators=[DataRequired()])
    submit = SubmitField('submit')