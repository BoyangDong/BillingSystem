import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import datetime
from app.exceptions import ValidationError
from flask import current_app
from flask_login import UserMixin
from app import login_manager
from app import db


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.String(38), primary_key=True)
    email = db.Column(db.String(38), unique=True, index=True)
    username = db.Column(db.String(38))
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer)
    isVarified = db.Column(db.Boolean)
    Created = db.Column(db.DateTime)

    def __init__(self, email, username, password):
        self.id = str(uuid.uuid4())
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.role_id = 1
        self.isVarified = False
        self.Created = datetime.now().strftime("%Y-%m-%d %H:%M%:%S")
        if email == 'eric.wang@victorynetworks.com' or \
           email == 'techsupport@victorynetworks.com' or \
           email == 'sup551@gmail.com':
            self.isVarified = True

    @property
    def password(self):
        raise AttributeError('password is not readable attriburte')

    @password.setter
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    def generate_auth_token(self, expiration):
        s = Serializer(current_app.config['SECRET_KEY'],
                       expires_in=expiration)
        return s.dumps(self.to_json())

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None

        return User.query.filter_by(email=data['Email']).first()

    def to_json(self):
        return {
            'ID': self.id,
            'Email': self.email,
            'UserName': self.username,
            "role_id": self.role_id,
            'Created': str(self.Created)
        }

    @staticmethod
    def from_json(json_user):

        email = json_user.get('Email')
        username = json_user.get('UserName')
        password = json_user.get('Password')
        try:
            user = User(email, username, password)
        except:
            raise ValidationError('Failed Creating User')
        return user
