from flask import Flask, redirect, request, abort
from flask import render_template

from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from login_form import LoginForm
from registr_form import RegistrForm
from addjob_form import AddJobForm
from data import db_session
from data.jobs import create_job, Job
from data.users import User, create_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super_dooper_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Job).all()
    out_jobs = []
    for job in jobs:
        team_leader = db_sess.query(User).get(job.team_leader)
        surname = team_leader.surname
        name = team_leader.name
        out_jobs.append(
            {'id': job.id, 'job_title': job.job, 'team_leader': f'{surname} {name}', 'duration': job.work_size,
             'collaborators': job.collaborators, 'is_finished': job.is_finished})

    return render_template('index.html', jobs=out_jobs)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


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


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        user = create_user(form.surname.data, form.name.data, form.age.data, form.position.data, form.speciality.data,
                           form.address.data, form.email.data, form.password.data)
        session.add(user)
        session.commit()
        login_user(user, remember=True)
        return redirect("/")
    return render_template('registration.html', title='Регистрация', form=form)


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


@login_required
@app.route('/editjob/<int:job_id>', methods=['GET', 'POST'])
def edit_job(job_id):
    form = AddJobForm()
    session = db_session.create_session()
    if request.method == 'GET':
        editing_job = session.get(Job, job_id)
        if current_user.id != editing_job.team_leader and current_user.id != 1:
            return render_template('fail.html', message="Ваши права не позволяют редактировать эту работу!")

        form.team_leader.data = editing_job.team_leader
        form.job_title.data = editing_job.job
        form.work_size.data = editing_job.work_size
        form.collaborators.data = editing_job.collaborators
        form.is_finished.data = editing_job.is_finished
    if form.validate_on_submit():
        job = session.get(Job, job_id)
        if job:
            job.team_leader = form.team_leader.data
            job.job = form.job_title.data
            job.work_size = form.work_size.data
            job.collaborators = form.collaborators.data
            job.is_finished = form.is_finished.data
            session.commit()
            return redirect("/")
        else:
            abort(404)
    return render_template('addjob.html', title='Изменение работы', form=form)


@login_required
@app.route('/deletejob/<int:job_id>', methods=['GET', 'POST'])
def delete_job(job_id):
    session = db_session.create_session()
    job = session.get(Job, job_id)
    if current_user.id != job.team_leader and current_user.id != 1:
        return render_template('fail.html', message="Ваши права не позволяют удалять эту работу!")
    if job:
        session.delete(job)
        session.commit()
    else:
        abort(404)
    return redirect("/")


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
    return redirect('/index/logout')


if __name__ == '__main__':
    db_session.global_init('db/mars.db')
    app.run(port=8080, host='127.0.0.1')
