from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# setup db
db = SQLAlchemy()

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    migrate = Migrate(app, db)
    from counter.views import counter_app

    app.register_blueprint(counter_app)

    return app
