"""
A simple example of a database interface using SQLite

Create a table to store people and provide functions to
add new records and to run some queries.

"""

import sqlite3


def create_tables(db):
    """Create database tables for our application"""

    sql = """
DROP TABLE IF EXISTS people;
CREATE TABLE people (
    first varchar,
    last varchar,
    age integer);
    """

    db.executescript(sql)
    db.commit()


def add_person(db, first, last, age):
    """Add a person to the database"""



def list_people(db):
    """List all people in the database, return a list
    of tuples (first, last, age)"""



def people_over_21(db):
    """Return a list of people over the age of 21
    as a list of tuples (first, last, age)"""



if __name__=='__main__':

    # here is some test code that should work when you have
    # completed the procedures above
    # note you should also run the unit tests

    db = sqlite3.connect('test.db')
    create_tables(db)

    add_person(db, 'Steve', 'Cassidy', 21)
    add_person(db, 'Mary', 'Jane', 33)

    people = list_people(db)

    for p in people:
        print(p)
