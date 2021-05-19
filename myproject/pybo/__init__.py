from flask import Flask, app
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
import config
db = SQLAlchemy()
migrate = Migrate()

app.secret_key = b'dhdjd$ah#q89hwu&.ihr'#세션 비밀번호

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
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
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)


    from . import models

    # 블루프린트
    from .views import main_views, auth_views, question_views, answer_views, voca_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(voca_views.bp)

    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    return app

