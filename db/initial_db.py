import sqlite3
from pathlib import Path
from os import path
from sqlite3 import Error


BASEDIR = Path(__file__).parent.parent.resolve()


def create_connection():
    connection = None
    try:
        connection = sqlite3.connect(path.join(BASEDIR, "sqlite3.db"))
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


def initial_db():
    with create_connection() as con:
        cursor = con.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS people (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                gender TEXT,
                age INTEGER,
                nationality TEXT,
                created_at TEXT
            );"""
        )


if __name__ == '__main__':
    initial_db()
