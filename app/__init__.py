import os
import logging

from logging.handlers import SMTPHandler
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask_mail import Mail
from flask_login import LoginManager
from flask_moment import Moment
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
mail = Mail(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

if not app.debug:
    if app.config["MAIL_SERVER"]:
        auth = None
        if app.config["MAIL_USERNAME"] or app.config["MAIL_PASSWORD"]:
            auth = (app.config["MAIL_USERNAME"], app.config["MAIL_PASSWORD"])
        secure = None
        if app.config["MAIL_USE_TLS"]:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config["MAIL_SERVER"], app.config["MAIL_PORT"]),
            fromaddr="no-reply@" + app.config["MAIL_SERVER"],
            toaddrs=app.config["ADMINS"],
            subject="DevLog Failure",
            credentials=auth,
            secure=secure,
        )
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

    if not os.path.exists("logs"):
        os.mkdir("logs")
    file_handler = RotatingFileHandler("logs/DevLog.log", maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info("DevLog startup")
# This is done to avoid circular imports. To keep Isort from moving this import
# to the top, we need to add the isort:skip. So do not remove this or there will
# be a circular import error.
from app import routes, models, errors  # isort:skip
