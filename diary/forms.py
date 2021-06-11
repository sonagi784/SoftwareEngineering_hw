from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from diary.models import User


# login form
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me') # 자동로그인 T/F == 서버가 세션을 종료하지 않음
    submit = SubmitField('Sign In')


# signup(registration) form
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    # 이미 있는 사용자명일 경우 사용 불가
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')
    # 이미 있는 이메일일 경우 사용 불가
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


# blog post
class PostForm(FlaskForm):
    title = StringField('title field (max 30)', validators=[DataRequired(), Length(min=1, max=30)])
    post = TextAreaField('body field (max 140)', validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Post It')
    
