from flask import session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField, BooleanField, DateField, IntegerField, FloatField
from wtforms.validators import ValidationError, DataRequired, DataRequired, EqualTo, Length, Email


class OrgRegisterForm(FlaskForm):
  org_name = StringField("Organization Name", validators=[DataRequired()])
  password = PasswordField("Password", validators=[DataRequired(), Length(min=3, max=80)])
  org_email = StringField("Organization Email", validators=[DataRequired(), Email()])
  submit = SubmitField('Register')

class PositionForm(FlaskForm):
  pos_name = StringField("Position Title", validators=[DataRequired()])
  pos_summary = StringField("Position Summary", validators=[DataRequired()])
  pos_location = StringField("Location", validators=[DataRequired()])
  submit = SubmitField('Send')

class ApplicantForm(FlaskForm):
  name = StringField("Name", validators=[DataRequired()])
  about = StringField("About", validators=[DataRequired()])
  city = StringField("City", validators=[DataRequired()])
  indoors = BooleanField("Indoor activities")
  outdoors = BooleanField("Outdoor activities")
  remote = BooleanField("Remote")
  submit = SubmitField('Send')

class OrgLogin(FlaskForm):
  org_email = StringField("Organization Email", validators=[DataRequired(), Email()])
  password = PasswordField("Password", validators=[DataRequired()])
  submit = SubmitField('Login')

class OrgSummary(FlaskForm):
    org_summary = StringField("Summary", validators=[DataRequired()])
    submit = SubmitField('Update')

class Filter(FlaskForm):
  city = StringField("City", validators=[DataRequired()])
  indoors = BooleanField("Indoor activities")
  outdoors = BooleanField("Outdoor activities")
  remote = BooleanField("Remote")
  submit = SubmitField('Refresh')