"""Server for web app."""

from flask import Flask, render_template, session, redirect, request, flash
from flask_debugtoolbar import DebugToolbarExtension
import os
from jinja2 import StrictUndefined

from model import connect_to_db, db, User
from reservation_functions import get_available_tables, create_reservation


app = Flask(__name__)

app.secret_key = os.environ["SECRET_KEY"]

# Raise error if use undefined variable in Jinja2
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def show_homepage():
    """Show homepage to web app."""

    return render_template("homepage.html")


@app.route("/check-availability", methods=["POST"])
def check_availability():

    date = request.form.get("date")
    time = request.form.get("time")
    username = request.form.get("username")
    num_people = request.form.get("num_people")

    existing_user = User.query.filter(User.username == username).first()

    if not existing_user:
        existing_user = User(username=username)
        db.session.add(existing_user)
        db.session.commit()

    available_tables = get_available_tables(num_people, date, time)
    user_id = existing_user.user_id

    reservation = create_reservation(date, time, num_people, available_tables,
                                     user_id)

    db.session.add(reservation)
    db.session.commit()

    flash("You have successfully reserved a table for {} on {} at {}".format(
        num_people, date, time))

    return redirect("/")





if __name__ == "__main__":

    app.debug = True
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    DebugToolbarExtension(app)

    app.run(port=5000, host="0.0.0.0")
