from model import Reservation, Table, User


def get_available_tables(num_people, date, time):
    """Return all available Tables for date, time, num_people specified."""

    available_tables = []

    all_tables = Table.query.filter(Table.people_count >= num_people).all()

    if all_tables:

        for table in all_tables:
            table_id = table.table_id
            print table_id

            existing_reservation = Reservation.query.filter(
                Reservation.table_id == table_id,
                Reservation.date == date,
                Reservation.time == time).first()
            print existing_reservation

            if not existing_reservation:
                available_tables.append(table)

    return available_tables


def create_reservation(date, time, num_people, available_tables, user_id):
    """Create reservation and return Reservation object."""

    best_table = None

    for table in available_tables:

        if not best_table:
            best_table = table

        elif table.people_count < best_table.people_count:
            best_table = table

    best_table_id = best_table.table_id

    new_reservation = Reservation(date=date, time=time,
        people_in_party=num_people, table_id = best_table_id, user_id=user_id)

    return new_reservation
