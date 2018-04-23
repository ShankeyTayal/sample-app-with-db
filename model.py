"""Data model for PostgreSQL database."""

from flask_sqlalchemy import SQLAlchemy

# create SQLAlchemy object to connect to Postgres database
db = SQLAlchemy()


class Reservation(db.Model):
    """Reservation in database - references Table and User objects."""

    __tablename__ = "reservations"

    reservation_id = db.Column(db.Integer, nullable=False, autoincrement=True,
                               primary_key=True)
    date = db.Column(db.String, nullable=False)
    time = db.Column(db.String, nullable=False)
    people_in_party = db.Column(db.Integer, nullable=False)
    table_id = db.Column(db.Integer, db.ForeignKey("tables.table_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    tables = db.relationship("Table", backref="reservation")
    users = db.relationship("User", backref="reservation")


class Table(db.Model):
    """Table in database that can hold a max of 4 people."""

    __tablename__ = "tables"

    table_id = db.Column(db.Integer, nullable=False, autoincrement=True,
                         primary_key=True)
    people_count = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        """Human readable output to print object information."""

        return "<Table table_id{}, people_count{}>".format(self.table_id,
                                                           self.people_count)


class User(db.Model):
    """User of reservation app that can create Reservation."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, nullable=False, autoincrement=True,
                        primary_key=True)
    username = db.Column(db.String(20), nullable=False)


def connect_to_db(app):
    """Function for connecting to Postgres database to create tables."""

    # fill in database parameter with name of database
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///reservations"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    # Create ability to connect to DB/data model interatively from command line
    from server import app
    connect_to_db(app)
    print "Connected to DB"
