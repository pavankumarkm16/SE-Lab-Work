"""Manage a simple in-memory radio station programme schedule."""

import sqlite3


def create_connection():
    """Create a fresh in-memory database and its schedule table."""
    connection = sqlite3.connect(":memory:")
    connection.execute(
        """CREATE TABLE slots (
            id INTEGER PRIMARY KEY,
            show TEXT NOT NULL,
            host TEXT NOT NULL,
            start_hour INTEGER NOT NULL,
            minutes INTEGER NOT NULL CHECK (minutes > 0)
        )"""
    )
    return connection


def add_slot(connection, show, host, start_hour, minutes):
    """Add a validated programme slot to the schedule."""
    if not show or not host:
        raise ValueError("Show and host names must not be empty.")
    if not 0 <= start_hour <= 23:
        raise ValueError("Start hour must be between 0 and 23.")
    if minutes <= 0:
        raise ValueError("Duration must be a positive number of minutes.")
    connection.execute(
        "INSERT INTO slots (show, host, start_hour, minutes) "
        "VALUES (?, ?, ?, ?)",
        (show, host, start_hour, minutes),
    )


def slot_label(show, host):
    """Return a human-readable label for a programme slot."""
    return f"{show} hosted by {host}"


def overlap_free(start_hour, minutes, next_start_hour):
    """Return whether a slot finishes before the next one begins."""
    return start_hour + minutes / 60 <= next_start_hour


def morning_shows(connection):
    """Return the names of shows that start before noon."""
    rows = connection.execute(
        "SELECT show FROM slots WHERE start_hour < ? ORDER BY start_hour",
        (12,),
    )
    return [row[0] for row in rows]


def remove_slot(connection, slot_id):
    """Remove a programme slot by its database ID."""
    connection.execute("DELETE FROM slots WHERE id = ?", (slot_id,))


def main():
    """Run a short demonstration of schedule operations."""
    connection = create_connection()
    add_slot(connection, "Sunrise Beats", "Vik", 7, 60)
    add_slot(connection, "Midday Talk", "Anu", 13, 45)
    print(slot_label("Sunrise Beats", "Vik"))
    print(
        overlap_free(7, 60, 13),
        morning_shows(connection),
    )
    remove_slot(connection, 2)
    connection.close()


if __name__ == "__main__":
    main()
