from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')

    app.config["SQLALCHEMY_DATABASE_URI"] = \
        f"mysql+pymysql://root:thisisasupersecurepassword" \
        f"@sussex.thejmc.net:25560/db"
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    db.init_app(app)
    migrate.init_app(app, db)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .api.plants import plant_api as plant_blueprint
    app.register_blueprint(plant_blueprint, url_prefix='/api/plant')

    from .auth_routes import auth_routes as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
