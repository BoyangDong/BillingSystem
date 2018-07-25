import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'deadbeef'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    VICTORY_MAIL_SUBJECT_PREFIX = '[Victory]'
    VICTORY_MAIN_SENDER = 'Victory Admin <jobrunner@victorynetworks.com>'
    VICTORY_ADMIN = os.environ.get('VICTORY_ADMIN') or 'Eric Wang'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = "west.exch028.serverdata.net"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'jobrunner@victorynetworks.com'
    MAIL_PASSWORD = 'Rennurboj1!'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:server@10.60.3.12/dev?charset=utf8'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:server@10.60.3.12/test?charset=utf8'


class ProductionConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:server@10.60.3.12/sumo?charset=utf8'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
