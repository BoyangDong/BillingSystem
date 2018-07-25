from flask import g, jsonify, request
from flask_httpauth import HTTPBasicAuth
from app.main.models import User
from .errors import *
from . import api

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(email_or_token, password):
    if request.endpoint == "api.register":
        print('new user registering')
        return True

    t = request.headers.get('Authorization')
    if t is not None and t.split()[0] == 'Bearer' and len(t.split()[1]) > 60:
        email_or_token = t.split()[1]
        password = ""
    if email_or_token == '':
        return False
    if password == '' or password is None:
        g.current_user = User.verify_auth_token(email_or_token)

        g.token_used = True
        return g.current_user is not None
    user = User.query.filter_by(email=email_or_token).first()
    if not user:
        return False
    g.current_user = user
    g.token_used = False
    return user.verify_password(password)


@auth.error_handler
def auth_error():
    return unauthorized('Invalid credentials')


@api.before_request
@auth.login_required
def before_request():
    try:
        print("Current User: ", g.current_user.username)
    except AttributeError:
        print("there's no current_user before request")


@api.route('/token', methods=['GET', 'POST'])
@auth.login_required
def get_token():
    print("auth called")
    return jsonify({'token': g.current_user.generate_auth_token(
        expiration=36000), 'expiration': 36000})


@api.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response
