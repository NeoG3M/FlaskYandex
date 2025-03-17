from flask import Flask

from data.users import User
from data import db_session
from data.db_session import create_session, global_init

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    global_init(input())
    session = create_session()

    users = session.query(User).filter(User.address == 'module_1', User.speciality.notlike('%engineer%'),
                                       User.position.notlike('%engineer%'))
    for us in users:
        print(us.id)

    # app.run()


if __name__ == '__main__':
    main()
