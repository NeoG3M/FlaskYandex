from flask import Flask

from data.users import User
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init('db/mars.db')

    session = db_session.create_session()

    def create_user(*args):
        args = list(args)
        user = User()
        user.surname = args.pop()
        user.name = args.pop()
        user.age = args.pop()
        user.position = args.pop()
        user.speciality = args.pop()
        user.address = args.pop()
        user.email = args.pop()
        user.hashed_password = args.pop()
        user.set_password(user.hashed_password)
        return user

    user = create_user("Scott",
                       "Ridley",
                       21,
                       "captain",
                       "research engineer",
                       "module_1",
                       "scott_chief@mars.org",
                       "cap")
    session.add(user)
    user = create_user("Lebron",
                       "James",
                       44,
                       "just a man",
                       "research engineer",
                       "module_2",
                       "lebron@mars.org",
                       "duuude")
    session.add(user)
    user = create_user("Britney",
                       "Spirs",
                       55,
                       "crew member",
                       "singerr",
                       "module_3",
                       "onlygirlintheworld@mars.org",
                       "mymaaan")
    session.add(user)
    user = create_user("Donald",
                       "Trump",
                       72,
                       "ex captain",
                       "builder",
                       "module_6",
                       "makecountrygreatAGAIN@mars.org",
                       "imagod")
    session.add(user)
    session.commit()

    # app.run()


if __name__ == '__main__':
    main()
