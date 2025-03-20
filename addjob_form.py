from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, DateField, SubmitField, StringField,IntegerField, EmailField
from wtforms.validators import DataRequired


class AddJobForm(FlaskForm):
    team_leader = IntegerField('ID тим лидера', validators=[DataRequired()])
    job_title = StringField('Название работы', validators=[DataRequired()])
    work_size = IntegerField('Продолжительность работы', validators=[DataRequired()])
    collaborators = StringField('Коллабораторы', validators=[DataRequired()])
    is_finished = BooleanField('Работа завершена')

    submit = SubmitField('Добавить')
