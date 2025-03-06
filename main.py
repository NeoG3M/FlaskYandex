from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super_dooper_secret_key'


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя:', validators=[DataRequired()])
    password = PasswordField('Пароль:', validators=[DataRequired()])
    password_repeat = PasswordField('Повтор пароля:', validators=[EqualTo(password)])
    submit = SubmitField('Отправить')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<list>')
def list_prof(list):
    profs = ['инженер', 'строитель', "врач", "водитель", "биолог", "геодезист"]
    return render_template('list_prof.html', list=list, profs=profs)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
