from flask import request
from flask import url_for
from flask import redirect
from flask import render_template
from flask import send_from_directory

from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Miguel"}
    return render_template("index.html", title="Home", user=user)
