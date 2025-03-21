import datetime

import sqlalchemy
from sqlalchemy import orm
from flask_login import UserMixin
from .db_session import SqlAlchemyBase
from werkzeug.security import generate_password_hash, check_password_hash



class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String)
    name = sqlalchemy.Column(sqlalchemy.String)
    age = sqlalchemy.Column(sqlalchemy.Integer)
    position = sqlalchemy.Column(sqlalchemy.String)
    speciality = sqlalchemy.Column(sqlalchemy.String)
    address = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String)
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now())

    jobs = orm.relationship('Job', back_populates='user')

    def __repr__(self):
        return f'<Colonist> {self.id} {self.surname} {self.name}'

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)


def create_user(*args):
    args = list(args)
    user = User()
    user.surname = args.pop(0)
    user.name = args.pop(0)
    user.age = args.pop(0)
    user.position = args.pop(0)
    user.speciality = args.pop(0)
    user.address = args.pop(0)
    user.email = args.pop(0)
    user.hashed_password = args.pop(0)
    user.set_password(user.hashed_password)
    return user