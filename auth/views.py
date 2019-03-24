from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from app import bcrypt, db
from common.errors import error_response
from database import User

auth_blueprint = Blueprint('auth', __name__)


class RegisterAPI(MethodView):
    """
    User Registration Resource
    """

    @staticmethod
    def post():
        post_data = request.get_json()
        user = User.query.filter_by(email=post_data.get('email')).first()
        if not user:
            try:
                user = User(
                    email=post_data.get('email'),
                    password=post_data.get('password')
                )
                db.session.add(user)
                db.session.commit()
                auth_token = user.encode_auth_token(user.id)
                response_object = {
                    'status': 'success',
                    'message': 'Successfully registered.',
                    'auth_token': auth_token.decode()
                }
                return make_response(jsonify(response_object)), 201
            except Exception:
                return error_response(401, 'Some error occurred. Please try again.')
        else:
            return error_response(202, 'User already exists. Please Log in.')


class LoginAPI(MethodView):
    """
    User Login Resource
    """

    @staticmethod
    def post():
        post_data = request.get_json()
        try:
            user = User.query.filter_by(email=post_data.get('email')).first()
            if user and bcrypt.check_password_hash(user.password, post_data.get('password')):
                auth_token = user.encode_auth_token(user.id)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'auth_token': auth_token.decode()
                    }
                    return make_response(jsonify(response_object)), 200
            else:
                return error_response(404, 'User does not exist.')
        except Exception as e:
            print(e)
            return error_response(500, 'Try again')


registration_view = RegisterAPI.as_view('register_api')
login_view = LoginAPI.as_view('login_api')

auth_blueprint.add_url_rule(
    '/register',
    view_func=registration_view,
    methods=['POST']
)
auth_blueprint.add_url_rule(
    '/login',
    view_func=login_view,
    methods=['POST']
)
