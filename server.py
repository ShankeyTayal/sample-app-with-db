"""Server for web app."""

from flask import Flask, render_template, session, redirect, request, flash
from flask_debugtoolbar import DebugToolbarExtension
import os
from jinja2 import StrictUndefined

from model import connect_to_db, db, User


app = Flask(__name__)

app.secret_key = os.environ["SECRET_KEY"]

# Raise error if use undefined variable in Jinja2
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def show_homepage():
    """Show homepage to web app."""

    return render_template("homepage.html")


if __name__ == "__main__":

    app.debug = True
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    DebugToolbarExtension(app)

    app.run(port=5000, host="0.0.0.0")
