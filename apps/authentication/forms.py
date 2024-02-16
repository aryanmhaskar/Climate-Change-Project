# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FloatField
from wtforms.validators import Email, DataRequired

# login and registration

class LoginForm(FlaskForm):
    username = StringField('Username',
                         id='username_login',
                         validators=[DataRequired()])
    password = PasswordField('Password',
                             id='pwd_login',
                             validators=[DataRequired()])

class CreateAccountForm(FlaskForm):
    username = StringField('Username',
                         id='username_create',
                         validators=[DataRequired()])
    email = StringField('Email',
                      id='email_create',
                      validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             id='pwd_create',
                             validators=[DataRequired()])

class EmissionsForm(FlaskForm):
    house = FloatField('House', id='house', validators = [DataRequired()])
    car = FloatField('Car', id='car', validators = [DataRequired()])
    flight = FloatField('Flight', id='flight', validators = [DataRequired()])
    Other = FloatField('Other', id='other', validators = [DataRequired()])
    Secondary = FloatField('Secondary', id="secondary", validators=[DataRequired()])