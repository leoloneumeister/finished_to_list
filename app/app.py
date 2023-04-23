from flask import Flask
from app.extensions.database import db, migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)


# Blueprints
def register_blueprints(app: Flask):
    pass
