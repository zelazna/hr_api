class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost:5432/hr_jobs'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'change me'
    FLASK_ADMIN_SWATCH = 'cerulean'


class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost:5432/hr_jobs_test'
