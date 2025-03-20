from flask import Flask, redirect
from flask import render_template

from flask_login import LoginManager, login_user, login_required, logout_user

from login_form import LoginForm
from addjob_form import AddJobForm
from data import db_session
from data.jobs import create_job
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super_dooper_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/addjob', methods=['GET', 'POST'])
def add_job():
    form = AddJobForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        job = create_job(form.team_leader.data, form.job_title.data, form.work_size.data, form.collaborators.data,
                         form.is_finished.data)
        session.add(job)
        session.commit()
        return redirect("/")
    return render_template('addjob.html', title='Добавление работы', form=form)


@app.route('/<title>')
@app.route('/index/<title>')
def base(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<list>')
def list_prof(list):
    profs = ['инженер', 'строитель', "врач", "водитель", "биолог", "геодезист"]
    return render_template('list_prof.html', list=list, profs=profs)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


if __name__ == '__main__':
    db_session.global_init('db/mars.db')
    app.run(port=8080, host='127.0.0.1')
