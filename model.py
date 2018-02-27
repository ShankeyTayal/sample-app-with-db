"""Data model for PostgreSQL database."""

from flask_sqlalchemy import SQLAlchemy

# create SQLAlchemy object to connect to Postgres database
db = SQLAlchemy()


class User(db.Model):
    """User of web app."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        """Provide human readable representation of User object when printed."""

        return "<User user_id {}, username {}>".format(self.user_id,
                                                       self.username)


def connect_to_db(app):
    """Function for connecting to Postgres database to create tables."""

    # fill in * section with name of database
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///*"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    # Create ability to connect to DB/data model interatively from command line
    from server import app
    connect_to_db(app)
    print "Connected to DB"
