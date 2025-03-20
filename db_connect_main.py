from flask import Flask

from data.users import User
from data import db_session
from data.jobs import Job
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def create_job(*args):
    args = list(args)
    job = Job()
    job.team_leader = args.pop(0)
    job.job_title = args.pop(0)
    print('TITLE', job.job_title)
    job.work_size = args.pop(0)
    job.collaborators = args.pop(0)
    job.is_finished = args.pop(0)
    print('создал')
    return job


def main():
    db_session.global_init('mars.db')
    session = db_session.create_session()

    job = create_job(1, 'обычная работа', 20, '1, 2', False)
    session.add(job)
    session.commit()

    # app.run()


if __name__ == '__main__':
    main()
