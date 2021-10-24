from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config.Config")

    db.init_app(app)

    with app.app_context():
        from . import routes
        from . import lineup
        

        app.register_blueprint(routes.main_bp)
        app.register_blueprint(lineup.lineup_bp)

        db.create_all()

        return app