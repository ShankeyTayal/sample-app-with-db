"""For seeding data into database."""

from model import Table
from model import connect_to_db, db
from server import app

# Create functions here to parse and load data to DB
# Each function needs db.session.add(<object>)
# and db.session.commit() at end of function


def create_tables(num_tables, num_people):
    """Create 'num_tables' Table objects that can hold 'num_people' on each
    Table - commit to database."""

    for i in range(num_tables):

        current = Table(people_count=num_people)

        db.session.add(current)

    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)

    db.create_all()
    create_tables(10, 2)
    create_tables(5, 4)
    create_tables(5, 6)
