from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from common import BooleanConverter
from config import Config

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)

    migrate.init_app(app, db)
    CORS(app)
    from auth.views import auth_blueprint
    from jobs.views import jobs_blueprint, matchs_blueprint

    app.url_map.converters['bool'] = BooleanConverter
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(jobs_blueprint, url_prefix='/jobs')
    app.register_blueprint(matchs_blueprint)
    return app
