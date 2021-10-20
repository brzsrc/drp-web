import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    set Flask configuration vars
    """
    # General config
    DEBUG = True
    TESTING = False
    # Database
    SECRET_KEY = os.environ.get('SECRET_KEY', 'this_is_the_secret_key')
    SQLALCHEMY_DATABASE_URI = 'postgresql://g205001009_u:dRp-09-a2Kb79@db.doc.ic.ac.uk:5432/g205001009_u'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    """
    config for test
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_by_name = dict(
    test=TestConfig,
    deploy=Config
)

key = Config.SECRET_KEY
