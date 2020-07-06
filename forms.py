from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):              # Class for form input (from flask_wtf)
    username = StringField("Username",          # Form field belonging to form class (from wtforms)
        validators=[                            # Validators to control (validate) input (from wtforms.validators)
        DataRequired(),                             # Field can not be empty
        Length(min=2, max=20)                       # Min and max length of field
        ])
    
    email = StringField("Email", validators=[DataRequired(), Email()]) 
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("Password")])
    submit = SubmitField("Sign up")

class LoginForm(FlaskForm):                  
    email = StringField("Email", validators=[DataRequired(), Email()]) 
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("Password")])
    remember = BooleanField("Remember me")
    submit = SubmitField("Login")