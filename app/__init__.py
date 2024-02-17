from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()

DEV_MODE = False

DB_USER = os.getenv('DB_USER') if not DEV_MODE else 'root'
DB_PASSWORD = os.getenv('DB_PASSWORD') if not DEV_MODE else 'thisisasupersecurepassword'
DB_ADDRESS = os.getenv('DB_ADDRESS') if not DEV_MODE else 'db.sussex.thejmc.net'
DB_PORT = os.getenv('DB_PORT') if not DEV_MODE else '25560'
DB_DATABASE = os.getenv('DB_DATABASE') if not DEV_MODE else 'db'

DB_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}" \
        f"@{DB_ADDRESS}:{DB_PORT}/{DB_DATABASE}"


def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')

    app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL

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
