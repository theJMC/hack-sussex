from functools import wraps
from flask import abort, request
from app.models import User
from hashlib import sha256


def page_auth(f):
    @wraps(f)
    def decorated_func(*args, **kws):
        user = User.query.filter_by(id=request.cookies.get("userID")).first()
        if user is None:
            return abort(401)

        generated_token = sha256(user.email.encode('utf-8') + user.password.encode('utf-8')).hexdigest()
        if generated_token != request.cookies.get('token'):
            return abort(400)

        return f(user, *args, **kws)

    return decorated_func


def api_auth(f):
    @wraps(f)
    def decorated_func(*args, **kws):
        auth = request.authorization
        if auth is None:
            return abort(401)

        user = User.query.filter_by(token=auth.token).first()
        if user is None:
            return abort(401)

        return f(user, *args, **kws)
    return decorated_func
