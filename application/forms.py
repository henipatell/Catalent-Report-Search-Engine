from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError

from application.models import User


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    retypedEmail = StringField("Re-type Email", validators=[DataRequired(), Email(), EqualTo('email')])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    confirmPassword = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password'), Length(min=8)])
    submit = SubmitField("Register")

    def validate_email(self,email):
        user = User.objects(email=email.data).first()
        if user:
            raise ValidationError("Email is already in use. Pick another one.")
    