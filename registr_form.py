from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField, IntegerField, EmailField
from wtforms.validators import DataRequired, EqualTo


class RegistrForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')])
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[DataRequired()])
    position = StringField('Должность', validators=[DataRequired()])
    speciality = StringField('Специальность', validators=[DataRequired()])
    address = StringField('Модуль проживания', validators=[DataRequired()])

    submit = SubmitField('Добавить')
