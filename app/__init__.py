from flask import Flask


app = Flask(__name__)
app.config.from_object("config")

# This is done to avoid circular imports. To keep Isort from moving this import
# to the top, we need to add the isort:skip. So do not remove this or there will
# be a circular import error.
from app import routes  # isort:skip
