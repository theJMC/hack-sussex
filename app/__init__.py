from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')

    app.config["SQLALCHEMY_DATABASE_URI"] = \
        f"mysql+pymysql://root:thisisasupersecurepassword" \
        f"@sussex.thejmc.net:3306/db"
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .plants.plant_api import plant_api as plant_blueprint
    app.register_blueprint(plant_blueprint, url_prefix='/api/plant')

    from .auth_routes import auth_routes as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
