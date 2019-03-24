from functools import wraps

from flask import request, g

from app.common.errors import error_response
from app.database import User


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            try:
                auth_token = auth_header.split(" ")[1]
            except IndexError:
                return error_response(401, 'Bearer token malformed.')
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if isinstance(resp, str):
                return error_response(401, resp)
            g.user = User.query.get(resp)
        else:
            return error_response(401, 'Provide a valid auth token.')
        return f(*args, **kwargs)

    return decorated_function
