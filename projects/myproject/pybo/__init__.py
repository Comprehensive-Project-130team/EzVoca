from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "fgsfsggsgfssfs"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pybo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    app.config.from_object(config)

    # ORM
    migrate.init_app(app, db)
    from . import models

    # 블루프린트
    from .views import main_views, auth_views, question_views, answer_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime
    
    return app
