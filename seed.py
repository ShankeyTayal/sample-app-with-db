"""For seeding data into database."""

from model import User
from model import connect_to_db, db
from server import app

# Create functions here to parse and load data to DB
# Each function needs db.session.add(<object>)
# and db.session.commit() at end of function
