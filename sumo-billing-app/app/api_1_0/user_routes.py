from .errors import *
from flask import jsonify
from app import db
from . import api, get_query_string
from app.main.models import User


@api.route('/users')
def test():
    return jsonify([user.to_json() for user
                    in User.query.filter_by(**get_query_string(User)).all()])
    if get_query_string():
        return jsonify(get_query_string())
    return request.query_string


@api.route('/register', methods=['POST'])
def register():
    json_user = request.json
    user = User.from_json(json_user)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_json()), 201
