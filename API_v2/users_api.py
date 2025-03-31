from flask import jsonify, make_response
from flask_restful import Resource, reqparse
from data import db_session
from data.users import User
from .users_parser import parser
from werkzeug.security import generate_password_hash


def set_password(password):
    hashed_password = generate_password_hash(password)
    return hashed_password


class UserResource(Resource):
    def get(self, user_id):
        session = db_session.create_session()
        user = session.get(User, user_id)
        if not user:
            return make_response(jsonify({'error': 'Not found'}), 404)
        return jsonify({'user':
                            user.to_dict(only=('id', 'surname', 'age', 'position', 'address'))
                        })

    def delete(self, user_id):
        session = db_session.create_session()
        user = session.get(User, user_id)
        print(user)
        if not user:
            return make_response(jsonify({'error': 'Not found'}), 404)
        session.delete(user)
        session.commit()
        return make_response(jsonify({'message': f'Successfully deleted user with id: {user_id}'}), 200)


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [
            item.to_dict(only=('id', 'surname', 'name', 'age', 'position', 'address'))
            for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = User(
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['email'],
            hashed_password=set_password(args['password'])
        )
        session.add(user)
        session.commit()
        return jsonify({'id': user.id})
