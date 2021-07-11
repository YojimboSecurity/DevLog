from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

# This is done to avoid circular imports. To keep Isort from moving this import
# to the top, we need to add the isort:skip. So do not remove this or there will
# be a circular import error.
from app import routes, models  # isort:skip
