'''

@author: steve
'''

import sqlite3
import uuid

# The database name
DATABASE_NAME = 'comp249.db'


def create_tables(db):
    """Create and initialise the database tables
    This will have the effect of overwriting any existing
    data."""

    sql = """
DROP TABLE IF EXISTS likes;
CREATE TABLE likes (
    name text,
    thing text
);
"""
    db.executescript(sql)
    db.commit()


def add_like(db, name, thing):
    """Add a new like to the database"""

    sql = "insert into likes (name, thing) values (?, ?)"

    cursor = db.cursor()
    cursor.execute(sql, [name, thing])

    db.commit()


def get_likes(db):
    """Return a list of likes from the database"""

    sql = "select name, thing from likes"

    cursor = db.cursor()
    cursor.execute(sql)

    result = []
    for row in cursor:
        result.append((row[0], row[1]))

    return result


def add_session(db, name):
    """Add an entry to the sessions table,
     given a name, generate a session id
     add to the database
     return the session id"""


def get_name(db, sessionid):
    """Given a session id, return the name of the user
    it corresponds to or None if we can't find a user"""


if __name__=='__main__':
    # if we call this script directly, create the database and make sample data
    db = sqlite3.connect(DATABASE_NAME)
    create_tables(db)
